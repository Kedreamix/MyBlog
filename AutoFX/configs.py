# =============== 网络代理 ================
# proxy = None
proxy = {"http": "socks5://127.0.0.1:7890", "https": "socks5://127.0.0.1:7890"}
proxy_gpt = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
# =============== 保存文件根目录 ================
root_path = r"D:\MyBlog\AutoFX\arxiv"
# root_blog = "/home/ubuntu/blogs/source/_posts"
# root_blog_images = '/home/ubuntu/blogs/source/images'
root_blog = r"D:\MyBlog\source\_posts\Paper"
temp_dir = r"D:\MyBlog\AutoFX\temp"
# root_blog_images = r'C:\Backup\blog_imgs\images'
# =============== DNN模型推理配置信息 ================
threshold = 0.5
enable_mkldnn = True
enforce_cpu = True
thread_num = 4
GOOGLE_API_KEY = 'AIzaSyALrVIKu8GEMwQB1o8cqe5LZbgg7H3-a-A'
summary_prompt= '''User
    Ignore all previous instructions. You are a highly proficient researcher that can read and write properly and fluently, and can extract all important information from any text. Your task is to summarize and extract all key takeaways of the following text delimited by triple backticks in all relevant aspects. 

    Output a summary and a list of key takeaways respectively. The summary should be a one-liner in at most 200 words. The key takeaways should be in up to seven bulletpoints, the fewer the better.

    Use the following format:
    #### Summary
    <summary of the text>

    #### Key Takeaways
    <list of key takeaways>

    Respond in Simplified Chinese.

    Text:
    ```
    %s
    ```
    '''
summary_prompt = '''User
    Ignore all previous instructions. Your new role is that of an exceptional bilingual expert researcher with fluency in both English and Simplified Chinese and  a researcher in the field of [ %s ] who is good at summarizing papers using concise statements. Your skill set includes the unique ability to distill complex documents into their most essential elements. You will be supplied with a specific excerpt of text framed within triple backticks. Your assignment involves two critical tasks:
    Output a summary and a list of key takeaways respectively.
    1. Craft a summary in Simplified Chinese, encapsulated in one line, that encapsulates the core message of the provided text. Ensure that this summary is concise, not exceeding 100 characters in length.
    2. Extract and articulate up to the seven most significant insights from the text as bullet points, written in Simplified Chinese. Focus on brevity and clarity to emphasize the text's crucial components.

    Your deliverables should be formatted precisely as below:

    **Summary**
    <summary of the text>

    **Key Takeaways**
    <list of key takeaways>

    Make sure your analysis is sharp and incisive, perfectly capturing the main thrust and subtle nuances of the original text, all while strictly adhering to the requested structure.
        
    Text:
    ```
    %s
    ```
    '''



keep_subjects = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL', 'eess.AS']
keywords_dict = {
    # 'LLM': ['ti:LLM+OR+abs:"Large Language Models"'
    #         'ti:GPT',
    #         'ti:LLM'],
    # 'MMT': ['abs:multimodal+AND+abs:machine+AND+abs:translation'],
    # 'Domain Adaptation': ['ti:Domain+AND+ti:Adaptation', 'abs:Domain+AND+abs:Adaptation'],
    '元宇宙/虚拟人': ['ti:"Virtual Avatar"+OR+ti:"Virtual Avatar"', 
                'ti:Metaverse', 
                'ti:Avatar'],
    # 'Open-Set': ['ti:Open+AND+ti:Set'],
    # '强化学习': ['ti:reinforcement+AND+ti:learning'],
    # 'Few-Shot': ['ti:few+AND+ti:shot', 'abs:few+AND+abs:shot'],
    # '场景文本检测识别': ['ti:Scene+AND+ti:Text', 'abs:Text+AND+abs:detection+AND+abs:End-to-End+AND+abs:scene'],
    # 'I2I Translation': ['abs:image+AND+abs:translation', 'ti:image+AND+ti:translation'],
    # '视频理解': ['ti:video+AND+ti:understanding'],
    # 'Anti-Spoofing': ['ti:anti+AND+ti:spoofing', 'abs:anti+AND+abs:spoofing'],
    # 'Vision Transformer': ['abs:ViT+AND+abs:image', 'abs:prompt+AND+abs:learning+AND+abs:image+AND+abs:vision'],
    # '检测/分割/跟踪': ['ti:object+AND+ti:detection+AND+abs:image', 'ti:semantic+AND+ti:segmentation+AND+abs:image',
    #              'ti:instance+AND+ti:segmentation+AND+abs:image', 'ti:object+AND+ti:tracking+AND+image'],
    # '对抗攻击': ['ti:attack+AND+abs:adversarial+AND+abs:attack+AND+image',
    #          'ti:example+AND+abs:adversarial+AND+abs:attack+AND+abs:example+AND+image'],
    # '人脸相关': ['ti:face+AND+ti:recognition+AND+abs:image', 'ti:face+AND+ti:detection+AND+abs:image',
    #          'ti:face+AND+ti:parse+AND+abs:image'],
    # '无监督/半监督/对比学习': ['ti:contrastive+AND+abs:image'],
    # '医学影像/息肉检测分割': ['ti:polyp+AND+ti:segmentation+AND+abs:polyp', 'all:polyp+AND+all:classification'],
    # '医学影像/Breast Ultrasound': ['all:breast+AND+all:ultrasound'],
    # 'Speech': ['abs:speech+AND+all:enhancement', 'abs:self-supervised+AND+abs:speech',
    #            'abs:speech+AND+abs:separation', 'abs:speech+AND+abs:recognition'],
    
    # 'Face Swapping': ['ti:Swapping+AND+abs:face+AND+abs:swapping', 'abs:face+AND+abs:swap',
    #                   'all:face+AND+all:swapping', 'all:head+AND+all:swapping'],
    # 'GAN': ['abs:image+AND+abs:GAN', 
    #         'abs:StyleGAN+OR+abs:StyleGAN2+OR+abs:StyleGAN3'],
    'Diffusion Models': ['abs:"Diffusion Model"+AND+abs:"Image"',
                        #  'ti:"generative"+OR+abs:"score-base"',
                        #  'ti:"Diffusion"+OR+abs:"score-base"',
                            'ti:"diffusion model"+AND+ti:"style transfer"+OR+all:"medical image translation"',
                            'ti:"diffusion model"+AND+ti:"style transfer"'],
    'Talking Head Generation': ['abs:"Talking Head"+OR+ti:"Talking Head"',
                                'all:"Talking Portrait"+OR+all:"Talking Face"+OR+all:"Talking Human"+OR+all:"talking avatar"+OR+all:"talking video"',
                                'all:"Audio-Driven"+OR+all:"Speech Driven"',
                                '(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven"+OR+all:"talking avatar"+OR+all:"talking video")+AND+(ti:NeRF+OR+ti:"Neural Radiance")',
                                '(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven"+OR+all:"talking avatar"+OR+all:"talking video")+AND+(ti:Diffusion+OR+ti:Diffuse)',
                                '(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven"+OR+all:"talking avatar"+OR+all:"talking video")+AND+(all:"Gaussian Splatting")',
                                'ti:Talker+OR+ti:Talk',
    ],
    "3DGS": ['ti:"Gaussian Splatting"+OR+abs:"Gaussian Splatting"+OR+ti:"3D Gaussian"+OR+abs:"3D Gaussian"', 
                            '(ti:"Gaussian Splatting"+OR+abs:"Gaussian Splatting")+AND+(ti:Head+OR+ti:Avatar+OR+ti:Human)'],
    'NeRF': ['ti:NeRF', 'ti:NeRF+AND+(all:Face+OR+all:Human+OR+all:Avatar+OR+all:Head)', 
                'abs:"Neural Radiance Field"+OR+ti:"Neural Radiance"', 
                'ti:GAN-NeRF'],
    # '3D reconstruction': ['all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction"',
    #                         'all:"human-object interaction reconstruction"+OR+all:"hand-object interaction reconstruction"+OR+all:"human reconstruction"+OR+all:"object reconstruction"',
    #                         'all:"shape generation"+OR+all:"shape synthesis"',
    #                         'all:"implicit field"+OR+all:"deformation"',
    #                         'all:"image-to-3d"+OR+all:"text-to-3d"',
    #                         '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                         '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                         'all:"Gaussian Splatting"+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                     ],
}


keywords_daily_dict = {
    # 'GAN': ['GAN', 'Generative Adversarial Network', 'stylegan'],
    'Diffusion Models': ['diffusion model', 'diffusion based'],
    # 'Transformer/多模态/动态网络': ['vision transformer', 'Vision MLP', 'ViT', 'prompt learning',
    #                          'image caption', 'Modality', 'dynamic network architecture'],
    # '检测/分割/跟踪': ['object detection', 'semantic segmentation', 'instance segmentation', 'object tracking'],
    # '对抗攻击': ['adversarial attack', 'adversarial example', 'DeepFake'],
    # '人脸相关': ['face recognition', 'face detection', 'face parse', 'face landmark', 'face localization',
    #          'head pose estimation', 'kinship', 'Descendant'],
    # '无监督/半监督/对比学习': ['unsupervised learning', 'semi-supervised learning', 'contrastive learning',
    #                  'zero shot', 'few shot']
    'Audio Driven Generation': ["Talking Head","Talking Portrait","Talking Face", "Audio-driven","Speech Driven","Talk"], 
    "Gaussian Splatting": ["Gaussian Splatting", "Splatting", "Gaussian", "Gaussian-based"],
    'NeRF': ['NeRF', 'Neural Radiance Field', 'Neural Radiance', 'GAN-NeRF'],
    # '3D reconstruction': ['all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction"',
    #                         'all:"human-object interaction reconstruction"+OR+all:"hand-object interaction reconstruction"+OR+all:"human reconstruction"+OR+all:"object reconstruction"',
    #                         'all:"shape generation"+OR+all:"shape synthesis"',
    #                         'all:"implicit field"+OR+all:"deformation"',
    #                         'all:"image-to-3d"+OR+all:"text-to-3d"',
    #                         '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                         '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                         'all:"Gaussian Splatting"+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
    #                     ],
}