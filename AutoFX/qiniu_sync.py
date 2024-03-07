from qiniu import Auth, put_file, etag, urlsafe_base64_encode, BucketManager, CdnManager
from typing import List, Dict
import os
from qiniu import build_batch_delete


def chunks(lst, n):
    if len(lst) == 0: return lst
    splited = []
    step = int(len(lst) / n) + 1
    for i in range(0, len(lst), step):
        splited.append(lst[i: i + step])
    return splited


class Sync:
    """
    同步目录至七牛云
    """

    def __init__(
            self,
            access_key: str,
            secret_key: str,
            bucket_name: str,
            sync_dir: str,
            exclude: List,
            cover: bool,
            remove_redundant: bool,
    ):
        self.bucket_name = bucket_name
        self.q = Auth(access_key, secret_key)
        self.bucket = BucketManager(self.q)
        self.sync_dir = sync_dir
        self.exclude = exclude
        self.cover = cover
        self.remove_redundant = remove_redundant
        self.sync()
        self.refresh_cdn_dir()

    def sync(self):
        """
        同步操作
        :return:
        """
        remote_files = self.list_remote()
        local_files = self.list_local()

        # 首先删除远端仓库中多余的文件
        remove_remote_files = []
        for remote_filename in remote_files:
            if remote_filename not in local_files:
                remove_remote_files.append(remote_filename)
                if not remote_filename.__contains__("jpg"):
                    print(remote_filename)
        print("远程文件数：", len(remote_files), "本地文件数：", len(local_files), "远程待删除文件数：", len(remove_remote_files))

        for batch in chunks(remove_remote_files, int(len(remove_remote_files) / 50) + 1):
            if len(batch) > 0:
                self.bucket.batch(build_batch_delete(self.bucket_name, batch))

        # 上传本地文件到远端(仅上传远端不存在的以及修改过的)
        for local_filename in local_files:
            if (
                    local_filename not in remote_files
                    or local_files[local_filename]["hash"]
                    != remote_files[local_filename]["hash"]
            ):
                print("puting " + local_filename)
                ret, info = put_file(
                    self.q.upload_token(self.bucket_name, local_filename, 3600),
                    local_filename,
                    local_files[local_filename]["fullpath"],
                )

    def refresh_cdn_dir(self):
        cdn_manager = CdnManager(self.q)
        dirs = [
            'https://ipaper.today/'
        ]

        _, refresh_dir_result = cdn_manager.refresh_dirs(dirs)
        if refresh_dir_result.ok():
            print('refresh CDN dirs success!')

    def list_remote(self) -> Dict:
        """
        列出远程仓库所有的文件信息
        :return: List
        """
        result = {}
        marker = None
        while True:
            responses = self.bucket.list(self.bucket_name, marker=marker)
            items = responses[0]["items"]
            for file in items:
                result[file["key"]] = file
            if 'marker' not in responses[0].keys():
                return result
            else:
                marker = responses[0]["marker"]

    def list_local(self) -> Dict:
        """
        列出本地仓库所有的文件信息
        """
        files = {}

        def get_files(path):
            for filename in os.listdir(path):
                if filename in self.exclude:
                    continue
                fullpath = os.path.join(path, filename).replace('\\', '/')
                if os.path.isfile(fullpath):
                    key = fullpath.split(self.sync_dir)[1]
                    files[key] = {"fullpath": fullpath, "hash": etag(fullpath)}
                else:
                    get_files(fullpath)

        get_files(self.sync_dir)
        return files


if __name__ == "__main__":
    sync_dir = r"C:/Backup/blogs/public/"

    Sync(
        access_key="9gthfNqzOiOOAP3ZrPeDscx-4bF6VY6a6U3r8WJ8",  # access_key
        secret_key="cTKHAJb4azTcPH1o7-C5JTpaPZ6ymHzC8dYEEQ7i",  # secret_key
        bucket_name="ipaper",  # bucket_name
        sync_dir=sync_dir,  # 静态文件目录(后面必须有斜杠/)
        exclude=[".DS_Store"],
        cover=True,
        remove_redundant=True,
    )
