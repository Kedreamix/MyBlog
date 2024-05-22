
---
title: Talking Head Generation
date: 2024-05-22 12:29:06
author: Kedreamix
cover: https://picx.zhimg.com/v2-55d3ca2d04e45a757c657d4be241bba9.jpg
categories: Paper
tags:
    - Talking Head Generation
description: Talking Head Generation 方向最新论文已更新，请持续关注 Update in 2024-05-22  Listen, Disentangle, and Control Controllable Speech-Driven Talking   Head Generation  
keywords: Talking Head Generation
toc:
toc_number: false
toc_style_simple: true
copyright:
copyright_author:
copyright_author_href:
copyright_url:
copyright_info:
mathjax: true
katex:
aplayer:
highlight_shrink:
aside:
---

>⚠️ 以下所有内容总结都来自于 Google的大语言模型[Gemini-Pro](https://ai.google.dev/)的能力，如有错误，仅供参考，谨慎使用
>🔴 请注意：千万不要用于严肃的学术场景，只能用于论文阅读前的初筛！
>💗 如果您觉得我们的项目对您有帮助 [ChatPaperFree](https://github.com/Kedreamix/ChatPaperFree) ，还请您给我们一些鼓励！⭐️ [HuggingFace免费体验](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)

# 2024-05-22 更新


## Listen, Disentangle, and Control: Controllable Speech-Driven Talking   Head Generation

**Authors:Changpeng Cai, Guinan Guo, Jiao Li, Junhao Su, Chenghao He, Jing Xiao, Yuanxu Chen, Lei Dai, Feiyu Zhu**

Most earlier investigations on talking face generation have focused on the synchronization of lip motion and speech content. However, human head pose and facial emotions are equally important characteristics of natural human faces. While audio-driven talking face generation has seen notable advancements, existing methods either overlook facial emotions or are limited to specific individuals and cannot be applied to arbitrary subjects. In this paper, we propose a one-shot Talking Head Generation framework (SPEAK) that distinguishes itself from general Talking Face Generation by enabling emotional and postural control. Specifically, we introduce the Inter-Reconstructed Feature Disentanglement (IRFD) method to decouple human facial features into three latent spaces. We then design a face editing module that modifies speech content and facial latent codes into a single latent space. Subsequently, we present a novel generator that employs modified latent codes derived from the editing module to regulate emotional expression, head poses, and speech content in synthesizing facial animations. Extensive trials demonstrate that our method can generate realistic talking head with coordinated lip motions, authentic facial emotions, and smooth head movements. The demo video is available at the anonymous link: https://anonymous.4open.science/r/SPEAK-F56E 

[PDF](http://arxiv.org/abs/2405.07257v1) 

**Summary**
语音驱动的说话人头像生成框架，实现了说话人头像表情情绪和姿势控制

**Key Takeaways**
- 注重唇部动作和语音内容同步
- 人类头部姿势和面部表情也是自然人脸的重要特征
- 现有方法忽视面部表情或局限于特定个体
- 提出了一次性说话人头像生成框架 (SPEAK)
- 引入了互重构特征分离 (IRFD) 方法
- 设计了一个面部编辑模块，将语音内容和面部潜在编码修改为一个潜在空间
- 提出了一种新颖的生成器，利用编辑模块派生的修改后的潜在编码来调节合成面部动画中的情绪表达、头部姿势和语音内容

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: 聆听、解耦和控制：可控语音驱动说话人头部生成（中文翻译：聆听、解耦和控制：可控语音驱动说话人头部生成）</p>
</li>
<li>
<p>Authors: Changpeng Cai, Guinan Guo, Jiao Li, Junhao Su, Chenghao He, Jing Xiao, Yuanxu Chen, Lei Dai, Feiyu Zhu</p>
</li>
<li>
<p>Affiliation: 东南大学（中文翻译：东南大学）</p>
</li>
<li>
<p>Keywords: Speech-driven talking head generation, Facial emotion control, Head pose control, Latent space disentanglement, Generative adversarial networks</p>
</li>
<li>
<p>Urls: Paper: https://arxiv.org/abs/2405.07257, Github: None</p>
</li>
<li>
<p>Summary:</p>
<p>(1): 人类头部姿势和面部表情是自然人脸的重要特征，而现有的方法要么忽略面部表情，要么仅限于特定个体，无法应用于任意主体。</p>
<p>(2): 现有的方法要么忽略面部表情，要么仅限于特定个体，无法应用于任意主体。</p>
<p>(3): 本文提出了一种单次说话人头部生成框架（SPEAK），通过引入互重构特征解耦（IRFD）方法将人脸特征解耦为三个潜在空间，设计了一个面部编辑模块，将语音内容和面部潜在码修改为一个潜在空间，并提出一个新颖的生成器，利用编辑模块修改后的潜在码调节合成面部动画中的情感表达、头部姿势和语音内容。</p>
<p>(4): SPEAK在协调的唇部动作、真实的面部表情和平滑的头部动作下生成逼真的说话人头部，在多个数据集上的实验结果表明，SPEAK在情感可控性和头部姿势可控性方面优于现有方法。</p>
</li>
<li>
<p>方法：</p>
<p>（1）：IRFD：通过引入互重构特征解耦（IRFD）方法将人脸特征解耦为三个潜在空间，分别反映头部姿势、面部表情和身份；</p>
<p>（2）：音频编码器：使用 wav2vec 2.0 提取音频内容特征；</p>
<p>（3）：编辑模块：将音频内容和面部潜在码修改为一个潜在空间，从而对齐音频内容和面部信息模态；</p>
<p>（4）：生成器：利用编辑模块修改后的潜在码调节合成面部动画中的情感表达、头部姿势和语音内容。</p>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）本文提出了一种技术，可以从其他视频中生成准确的唇形同步、具有自由姿势和情绪控制的情感说话人头部。我们设计了一个新颖的解耦模块 IRFD，用于将输入样本分解为情绪、身份和姿势嵌入。然后，为了生成说话头部，我们提供了一个新颖的说话头部生成框架 SPEAK。定性和定量实验表明，我们的方法在具有挑战性的场景中表现得非常稳健，例如显着的姿势和情绪表达变化。</p>
<p>（2）创新点：提出了 IRFD 解耦模块，将人脸特征解耦为三个潜在空间，分别反映头部姿势、面部表情和身份；设计了 SPEAK 说话头部生成框架，利用编辑模块修改后的潜在码调节合成面部动画中的情感表达、头部姿势和语音内容。
性能：在协调的唇部动作、真实的面部表情和平滑的头部动作下生成逼真的说话人头部；在多个数据集上的实验结果表明，SPEAK 在情感可控性和头部姿势可控性方面优于现有方法。
工作量：需要训练 IRFD 解耦模块和 SPEAK 说话头部生成框架，工作量较大。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-4cef68701eebad9ead106562636697ea.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-0c56dd339a6a2635e58337d5b57ea661.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-af84f0c9842d1a0bd09b78951550dfc4.jpg" align="middle">
</details>




## Deepfake Generation and Detection: A Benchmark and Survey

**Authors:Gan Pei, Jiangning Zhang, Menghan Hu, Zhenyu Zhang, Chengjie Wang, Yunsheng Wu, Guangtao Zhai, Jian Yang, Chunhua Shen, Dacheng Tao**

Deepfake is a technology dedicated to creating highly realistic facial images and videos under specific conditions, which has significant application potential in fields such as entertainment, movie production, digital human creation, to name a few. With the advancements in deep learning, techniques primarily represented by Variational Autoencoders and Generative Adversarial Networks have achieved impressive generation results. More recently, the emergence of diffusion models with powerful generation capabilities has sparked a renewed wave of research. In addition to deepfake generation, corresponding detection technologies continuously evolve to regulate the potential misuse of deepfakes, such as for privacy invasion and phishing attacks. This survey comprehensively reviews the latest developments in deepfake generation and detection, summarizing and analyzing current state-of-the-arts in this rapidly evolving field. We first unify task definitions, comprehensively introduce datasets and metrics, and discuss developing technologies. Then, we discuss the development of several related sub-fields and focus on researching four representative deepfake fields: face swapping, face reenactment, talking face generation, and facial attribute editing, as well as forgery detection. Subsequently, we comprehensively benchmark representative methods on popular datasets for each field, fully evaluating the latest and influential published works. Finally, we analyze challenges and future research directions of the discussed fields. 

[PDF](http://arxiv.org/abs/2403.17881v4) We closely follow the latest developments in   https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection

**Summary**
近年来，深度学习推动了深度伪造生成和检测技术的发展，带动了影视娱乐、人像合成等领域的研究应用。

**Key Takeaways**
- 深度伪造技术包含人脸替换、人脸重现、说话人脸生成、人脸属性编辑四大类。
- 深度学习技术，如变分自编码器、生成对抗网络、扩散模型推动了深度伪造生成技术的进步。
- 对应检测技术不断发展，以规范深度伪造的潜在滥用，例如用于隐私入侵和网络钓鱼攻击。
- 研究人员统一了任务定义，全面介绍了数据集和度量标准，并讨论了发展中的技术。
- 代表性方法在流行数据集上进行了全面基准测试，以全面评估最新和有影响力的已发表作品。
- 深入分析了所讨论领域的挑战和未来研究方向。
- 搜集整理了用于培训和评估的深度伪造数据集，并给出了如何获取途径。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：深度伪造生成与检测：基准与综述</p>
</li>
<li>
<p>作者：Gan Pei、Jiangning Zhang、Menghan Hu、Zhenyu Zhang、Chengjie Wang、Yunsheng Wu、Guangtao Zhai、Jian Yang、Chunhua Shen、Dacheng Tao</p>
</li>
<li>
<p>第一作者单位：华东师范大学</p>
</li>
<li>
<p>关键词：深度伪造生成、人脸替换、人脸重现、说话人脸生成、面部属性编辑、伪造检测、综述</p>
</li>
<li>
<p>论文链接：arXiv:2403.17881v4  [cs.CV]  16 May 2024
Github：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：深度伪造技术可以生成高度逼真的面部图像和视频，在娱乐、电影制作、数字人创建等领域具有重要的应用潜力。随着深度学习的进步，以变分自编码器和生成对抗网络为代表的技术取得了令人印象深刻的生成效果。最近，具有强大生成能力的扩散模型的出现引发了新一轮的研究浪潮。除了深度伪造生成之外，相应的检测技术也在不断发展，以规范深度伪造的潜在滥用，例如隐私入侵和网络钓鱼攻击。</p>
<p>（2）：过去方法及其问题：早期方法采用先进的变分自编码器（VAE）和生成对抗网络（GAN）技术，实现了看似逼真的图像生成，但其性能仍不令人满意，限制了实际应用。</p>
<p>（3）：本文提出的研究方法：本文全面回顾了深度伪造生成和检测的最新进展，总结和分析了这一快速发展领域的当前最先进技术。首先，我们统一任务定义，全面介绍数据集和指标，并讨论发展技术。然后，我们讨论了几个相关子领域的进展，并重点研究了四个人脸伪造领域：人脸替换、人脸重现、说话人脸生成和面部属性编辑以及伪造检测。随后，我们对每个领域的流行数据集对代表性方法进行了全面基准测试，全面评估了最新和最有影响力的已发表作品。最后，我们分析了所讨论领域的挑战和未来研究方向。我们密切关注该项目的最新进展。</p>
<p>（4）：本文方法在什么任务上取得了什么性能：本文在人脸替换、人脸重现、说话人脸生成、面部属性编辑和伪造检测方面取得了最先进的性能，证明了其方法的有效性。这些性能支持了他们在生成逼真面部媒体内容和检测深度伪造方面的目标。</p>
<ol>
<li>Methods:</li>
</ol>
<p>(1): 本文全面回顾了深度伪造生成和检测的最新进展，总结和分析了这一快速发展领域的当前最先进技术。</p>
<p>(2): 统一任务定义，全面介绍数据集和指标，并讨论发展技术。</p>
<p>(3): 讨论了几个相关子领域的进展，并重点研究了四个人脸伪造领域：人脸替换、人脸重现、说话人脸生成和面部属性编辑以及伪造检测。</p>
<p>(4): 对每个领域的流行数据集对代表性方法进行了全面基准测试，全面评估了最新和最有影响力的已发表作品。</p>
<p>(5): 分析了所讨论领域的挑战和未来研究方向。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文的意义在于全面回顾了深度伪造生成和检测的最新进展，总结和分析了这一快速发展领域的当前最先进技术，为研究人员和从业人员提供了宝贵的参考。</p>
<p>（2）：创新点：本文统一了任务定义，全面介绍了数据集和指标，并讨论了发展技术，为深度伪造生成和检测的研究提供了统一的框架。</p>
<p>性能：本文在人脸替换、人脸重现、说话人脸生成、面部属性编辑和伪造检测方面取得了最先进的性能，证明了其方法的有效性。</p>
<p>工作量：本文涉及的领域广泛，包括深度伪造生成和检测的各个方面，工作量较大。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-bd825fe7701ae1269a03cc9fcd2ebfab.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-6cb44fca6ef288c86ccb3c8e9f12f528.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-6f39a46c1332d51ffe66df4c9815557d.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-55d3ca2d04e45a757c657d4be241bba9.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-2b43074324cef40fcdbcefe9ae1bd2a0.jpg" align="middle">
</details>




