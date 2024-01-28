---
title: Linux中的SSH密钥登录连接
date: 2024-01-01 00:00:00
author: Kedreamix
cover: https://pic1.zhimg.com/80/v2-e62d325d3c609b70f5a297322c8739be_720w.png
categories: Linux
tags:
    - Linux
toc:
toc_number: false
toc_style_simple: true
---



# 简单两步走

如果不想看那么多原理，可以简单两步走

1. **输入以下命令**
```bash
ssh-keygen
cd .ssh
cat id_rsa.pub >> authorized_keys
chmod 600 authorized_keys
chmod 700 ~/.ssh
```

2. **下载对应密钥id_rsa即可，后续就可以密钥登录**

# 设置 SSH 通过密钥登录

![](https://pic1.zhimg.com/80/v2-e62d325d3c609b70f5a297322c8739be.png)

我们一般使用 PuTTY 等 SSH 客户端来远程管理 Linux 服务器。但是，一般的密码方式登录，容易有密码被暴力破解的问题。所以，一般我们会将 SSH 的端口设置为默认的 22 以外的端口，或者禁用 root 账户登录。其实，有一个更好的办法来保证安全，而且让你可以放心地用 root 账户从远程登录——那就是通过密钥方式登录。
密钥形式登录的原理是：利用密钥生成器制作一对密钥——一只公钥和一只私钥。将公钥添加到服务器的某个账户上，然后在客户端利用私钥即可完成认证并登录。这样一来，没有私钥，任何人都无法通过 SSH 暴力破解你的密码来远程登录到系统。此外，如果将公钥复制到其他账户甚至主机，利用私钥也可以登录。
下面来讲解如何在 Linux 服务器上制作密钥对，将公钥添加给账户，设置 SSH，最后通过客户端登录。

## 1. 制作密钥对
首先在服务器上制作密钥对。首先用密码登录到你打算使用密钥登录的账户，然后执行以下命令：
```bash
[root@host ~]$ ssh-keygen  <== 建立密钥对
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): <== 按 Enter
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase): <== 输入密钥锁码，或直接按 Enter 留空
Enter same passphrase again: <== 再输入一遍密钥锁码
Your identification has been saved in /root/.ssh/id_rsa. <== 私钥
Your public key has been saved in /root/.ssh/id_rsa.pub. <== 公钥
The key fingerprint is:
0f:d3:e7:1a:1c:bd:5c:03:f1:19:f1:22:df:9b:cc:08 root@host
```
密钥锁码在使用私钥时必须输入，这样就可以保护私钥不被盗用。当然，也可以留空，实现无密码登录。
现在，在 root 用户的家目录中生成了一个 .ssh 的隐藏目录，内含两个密钥文件。id_rsa 为私钥，id_rsa.pub 为公钥。
这个在windows也可以制作自己的密钥对
## 2. 在服务器上安装公钥
键入以下命令，在服务器上安装公钥：
```bash
[root@host ~]$ cd .ssh
[root@host .ssh]$ cat id_rsa.pub >> authorized_keys
```
这一部分相当于，将自己的公钥写到了ssh服务器中，写到authorized_keys中，这样只要有密钥对，就能正常连接，VScode也是
如此便完成了公钥的安装。为了确保连接成功，请保证以下文件权限正确：
```bash
[root@host .ssh]$ chmod 600 authorized_keys
[root@host .ssh]$ chmod 700 ~/.ssh
```
## 3. 设置 SSH，打开密钥登录功能 （管理员可以设置仅仅密钥登录）
编辑 /etc/ssh/sshd_config 文件，进行如下设置：
```bash
RSAAuthentication yes
PubkeyAuthentication yes
```
另外，请留意 root 用户能否通过 SSH 登录：
```bash
PermitRootLogin yes
```
当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：
```bash
PasswordAuthentication no
```
最后，重启 SSH 服务：
```bash
[root@host .ssh]$ service sshd restart
```
```bash
#允许root认证登录
PermitRootLogin yes
#允许密钥认证
RSAAuthentication yes
PubkeyAuthentication yes
```
## 4. 将私钥下载到客户端，然后转换为 PuTTY 能使用的格式
使用 WinSCP、SFTP 等工具将私钥文件 id_rsa 下载到客户端机器上。然后打开 PuTTYGen，单击 Actions 中的 Load 按钮，载入你刚才下载到的私钥文件。如果你刚才设置了密钥锁码，这时则需要输入。
载入成功后，PuTTYGen 会显示密钥相关的信息。在 Key comment 中键入对密钥的说明信息，然后单击 Save private key 按钮即可将私钥文件存放为 PuTTY 能使用的格式。
今后，当你使用 PuTTY 登录时，可以在左侧的 Connection -> SSH -> Auth 中的 Private key file for authentication: 处选择你的私钥文件，然后即可登录了，过程中只需输入密钥锁码即可。
## 参考
[https://wangdoc.com/ssh/key#ssh-keygen%E5%91%BD%E4%BB%A4%E7%94%9F%E6%88%90%E5%AF%86%E9%92%A5](https://wangdoc.com/ssh/key#ssh-keygen%E5%91%BD%E4%BB%A4%E7%94%9F%E6%88%90%E5%AF%86%E9%92%A5)
## 补充
其实可以一个密钥多个服务器，只要把公钥输入到authorized_keys中，这样只要有密钥对，就能正常连接，所以可以用很多个即可，不过为了安全，可以只用一个密钥
