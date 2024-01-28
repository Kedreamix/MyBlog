---
title: Tmux使用教程
date: 2024-01-01 00:00:00
author: Kedreamix
cover: https://picx.zhimg.com/80/v2-2d713640912c8cfbd1ab4e7b9e2cfa5b_720w.png
categories: Linux
tags:
    - Linux
toc:
toc_number: false
toc_style_simple: true
---

## 1. tmux介绍

### 1.1 会话与进程

命令行的典型使用方式是，打开一个终端窗口（terminal window，以下简称“窗口”），在里面输入命令。**用户与计算机的这种临时的交互，称为一次“会话”（session）** 。

会话的一个重要特点是，窗口与其中启动的进程是[连在一起](https://www.ruanyifeng.com/blog/2016/02/linux-daemon.html)的。打开窗口，会话开始；关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完。

一个典型的例子就是，[SSH 登录](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)远程计算机，打开一个远程窗口执行命令。这时，网络突然断线，再次登录的时候，是找不回上一次执行的命令的。因为上一次 SSH 会话已经终止了，里面的进程也随之消失了。

为了解决这个问题，会话与窗口可以“解绑”：窗口关闭时，会话并不终止，而是继续运行，等到以后需要的时候，再让会话“绑定”其他窗口。

### 1.2 Tmux 的作用

**Tmux 就是会话与窗口的“解绑”工具，将它们彻底分离。**

（1）它允许在单个窗口中，同时访问多个会话。这对于同时运行多个命令行程序很有用。


（2） 它可以让新窗口“接入”已经存在的会话。

（3）它允许每个会话有多个连接窗口，因此可以多人实时共享会话。

（4）它还支持窗口任意的垂直和水平拆分。


类似的终端复用器还有 GNU Screen。Tmux 与它功能相似，但是更易用，也更强大。二、基本用法

## 2. tmux安装

### 2.1 安装

Tmux 一般需要自己安装。

# Ubuntu 或 Debian

```bash
sudo apt-get install tmux
# CentOS 或 Fedora
sudo yum install tmux
# Mac
brew install tmux
```

### 2.2 启动与退出

安装完成后，键入`tmux`命令，就进入了 Tmux 窗口。

```bash
tmux
```


上面命令会启动 Tmux 窗口，底部有一个状态栏。状态栏的左侧是窗口信息（编号和名称），右侧是系统信息。

![](https://picx.zhimg.com/v2-3a8a91db08866f19a26aa93ac8b40fc4.png)

按下`Ctrl+d`或者显式输入`exit`命令，就可以退出 Tmux 窗口。

exit


### 2.3 前缀键

Tmux 窗口有大量的快捷键。所有快捷键都要通过前缀键唤起。默认的前缀键是`Ctrl+b`，即先按下`Ctrl+b`，快捷键才会生效。

举例来说，帮助命令的快捷键是`Ctrl+b ?`。它的用法是，在 Tmux 窗口中，先按下`Ctrl+b`，再按下`?`，就会显示帮助信息。

然后，按下 ESC 键或`q`键，就可以退出帮助。

## 3. 常用命令

### 3.1 新建会话

第一个启动的 Tmux 窗口，编号是`0`，第二个窗口的编号是`1`，以此类推。这些窗口对应的会话，就是 0 号会话、1 号会话。

使用编号区分会话，不太直观，更好的方法是为会话起名。

```bash
tmux new -s <session-name>
```


上面命令新建一个指定名称的会话。

### 3.2 分离会话

在 Tmux 窗口中，按下`Ctrl+b d`或者输入`tmux detach`命令，就会将当前会话与窗口分离。

```bash
tmux detach
```


上面命令执行后，就会退出当前 Tmux 窗口，但是会话和里面的进程仍然在后台运行。

`tmux ls`命令可以查看当前所有的 Tmux 会话。

```bash
tmux ls
# ortmux list-session
```




### 3.3 接入会话

`tmux attach`命令用于重新接入某个已存在的会话。

```bash
# 使用会话编号
tmux attach -t 0
# 使用会话名称
tmux attach -t <session-name>
```

### 3.4 杀死会话

`tmux kill-session`命令用于杀死某个会话。

# 使用会话编号
```bash
tmux kill-session -t 0
# 使用会话名称
tmux kill-session -t <session-name>
```

### 3.5 切换会话

`tmux switch`命令用于切换会话。

```bash
# 使用会话编号
tmux switch -t 0
# 使用会话名称
tmux switch -t <session-name>
```


### 3.6 重命名会话

`tmux rename-session`命令用于重命名会话。

```bash
tmux rename-session -t 0 <new-name>
```


上面命令将0号会话重命名。

### 3.7 会话快捷键

下面是一些会话相关的快捷键。

Ctrl+b d：分离当前会话。Ctrl+b s：列出所有会话。Ctrl+b $：重命名当前会话。


## 4. 最简操作流程

综上所述，以下是 Tmux 的最简操作流程。

新建会话`tmux new -s my_session`,在 Tmux 窗口运行所需的程序。按下快捷键`Ctrl+b d`将会话分离。下次使用时，重新连接到会话`tmux attach-session -t my_session`。

### 窗格快捷键

下面是一些窗格操作的快捷键。

| 快捷键                  | 功能                                                         |
| ----------------------- | ------------------------------------------------------------ |
| Ctrl+b %                | 划分左右两个窗格                                             |
| Ctrl+b "                | 划分上下两个窗格                                             |
| Ctrl+b <arrow key>      | 光标切换到其他窗格。<arrow key>是指向要切换到的窗格的方向键，比如切换到下方窗格，就按方向键↓ |
| Ctrl+b ;                | 光标切换到上一个窗格                                         |
| Ctrl+b o                | 光标切换到下一个窗格                                         |
| Ctrl+b {                | 当前窗格与上一个窗格交换位置                                 |
| Ctrl+b }                | 当前窗格与下一个窗格交换位置                                 |
| Ctrl+b Ctrl+o           | 所有窗格向前移动一个位置，第一个窗格变成最后一个窗格         |
| Ctrl+b Alt+o            | 所有窗格向后移动一个位置，最后一个窗格变成第一个窗格         |
| Ctrl+b x                | 关闭当前窗格                                                 |
| Ctrl+b !                | 将当前窗格拆分为一个独立窗口                                 |
| Ctrl+b z                | 当前窗格全屏显示，再使用一次会变回原来大小                   |
| Ctrl+b Ctrl+<arrow key> | 按箭头方向调整窗格大小                                       |
| Ctrl+b q                | 显示窗格编号                                                 |