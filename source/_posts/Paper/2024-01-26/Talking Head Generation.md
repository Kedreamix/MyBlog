
---
title: Talking Head Generation
date: 2024-01-26 21:23:09
author: Kedreamix
cover: https://pica.zhimg.com/v2-d53c04a42d143a126e5b391f40684f6a.jpg
categories: Paper
tags:
    - Talking Head Generation
description: Talking Head Generation 方向最新论文已更新，请持续关注 Update in 2024-01-26  NeRF-AD Neural Radiance Field with Attention-based Disentanglement for   Talking Face Synthesis  
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
abcjs:
---

>⚠️ 以下所有内容总结都来自于 Google的大语言模型[Gemini-Pro](https://ai.google.dev/)的能力，如有错误，仅供参考，谨慎使用
>🔴 请注意：千万不要用于严肃的学术场景，只能用于论文阅读前的初筛！
>💗 如果您觉得我们的项目对您有帮助 [ChatPaperFree](https://github.com/Kedreamix/ChatPaperFree) ，还请您给我们一些鼓励！⭐️ [HuggingFace免费体验](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)

# 2024-01-26 更新



## NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for   Talking Face Synthesis

**Authors:Chongke Bi, Xiaoxing Liu, Zhilei Liu**

Talking face synthesis driven by audio is one of the current research hotspots in the fields of multidimensional signal processing and multimedia. Neural Radiance Field (NeRF) has recently been brought to this research field in order to enhance the realism and 3D effect of the generated faces. However, most existing NeRF-based methods either burden NeRF with complex learning tasks while lacking methods for supervised multimodal feature fusion, or cannot precisely map audio to the facial region related to speech movements. These reasons ultimately result in existing methods generating inaccurate lip shapes. This paper moves a portion of NeRF learning tasks ahead and proposes a talking face synthesis method via NeRF with attention-based disentanglement (NeRF-AD). In particular, an Attention-based Disentanglement module is introduced to disentangle the face into Audio-face and Identity-face using speech-related facial action unit (AU) information. To precisely regulate how audio affects the talking face, we only fuse the Audio-face with audio feature. In addition, AU information is also utilized to supervise the fusion of these two modalities. Extensive qualitative and quantitative experiments demonstrate that our NeRF-AD outperforms state-of-the-art methods in generating realistic talking face videos, including image quality and lip synchronization. To view video results, please refer to https://xiaoxingliu02.github.io/NeRF-AD. 

[PDF](http://arxiv.org/abs/2401.12568v1) Accepted by ICASSP 2024

**摘要**
神经辐射场与注意力机制相结合，用于说话人脸合成，实现了准确的唇形生成。

**要点**

- 神经辐射场 (NeRF) 已用于说话人脸合成，以增强生成的面的真实感和 3D 效果。
- 现有的大多数 NeRF 方法要么给 NeRF 带来了复杂的学习任务，而缺乏对多模态特征融合的监督方法，要么无法将音频精确定位到与语音相关的面部区域。
- 这些问题导致现有方法产生了不准确的唇形。
- 该研究提出了一种基于 NeRF 和注意力机制解耦的说话人脸合成方法 (NeRF-AD)。
- 注意力机制解耦模块用于将面部分解为音频面部和身份面部，通过言语相关的面部动作单元 (AU) 信息。
- 为了精确地调节音频对说话人脸的影响，音频面部仅与音频特征融合。
- 大量的定性和定量实验表明，NeRF-AD 在生成逼真的说话人脸视频方面优于最先进的方法，包括图像质量和唇形同步。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：基于注意力机制的解耦的神经辐射场说话人面部合成（NeRF-AD）</li>
<li>作者：Chongke Bi，Xiaoxing Liu，Zhilei Liu</li>
<li>单位：天津大学智能与计算学院</li>
<li>关键词：说话人面部合成，神经辐射场，面部解耦</li>
<li>论文链接：https://arxiv.org/abs/2401.12568
    Github 链接：无</li>
<li>
<p>摘要：
（1）：说话人面部合成是多维信号处理和多媒体领域当前的研究热点之一。为了增强生成面部的真实感和 3D 效果，神经辐射场（NeRF）最近被引入到该研究领域。然而，大多数现有的基于 NeRF 的方法要么让 NeRF 承担复杂的学习任务，同时缺乏监督式多模态特征融合的方法，要么无法将音频精确映射到与语音运动相关的面部区域。这些原因最终导致现有方法生成的唇形不准确。
（2）：为了解决上述问题，本文提出了一种基于注意力机制的解耦的神经辐射场说话人面部合成方法（NeRF-AD）。具体来说，我们引入了一个基于注意力的解耦模块，利用与语音相关的面部动作单元（AU）信息将面部解耦为音频面部和身份面部。为了精确地调节音频如何影响说话的面部，我们只将音频面部与音频特征融合。此外，AU 信息还用于监督这两个模态的融合。
（3）：为了减少 NeRF 的学习负担并提高面部渲染的准确性，我们对说话的面部进行了分解，并为 NeRF 提供了两个分解的精确条件。我们提出了一个基于注意力的解耦模块，允许音频与与语音运动相关的面部区域精确融合。同时，我们采用一系列方法来监督整个过程。
（4）：广泛的定性和定量实验表明，NeRF-AD 在生成逼真的说话人面部视频方面优于最先进的方法，包括图像质量和唇形同步。</p>
</li>
<li>
<p>方法：
（1）：提出了一种基于注意力机制的解耦的神经辐射场说话人面部合成方法（NeRF-AD）。
（2）：引入了一个基于注意力的解耦模块，利用与语音相关的面部动作单元（AU）信息将面部解耦为音频面部和身份面部。
（3）：只将音频面部与音频特征融合，并利用AU信息监督这两个模态的融合。
（4）：对说话的面部进行了分解，并为NeRF提供了两个分解的精确条件。
（5）：提出了一个基于注意力的解耦模块，允许音频与与语音运动相关的面部区域精确融合。
（6）：采用一系列方法来监督整个过程。</p>
</li>
<li>
<p>结论：
（1）本工作提出了一种基于注意力机制的解耦神经辐射场说话人面部合成方法（NeRF-AD），该方法通过注意力解耦模块将说话人面部解耦为音频面部和身份面部，并仅将音频面部与音频特征融合，利用动作单元信息监督两个模态的融合，降低了 NeRF 的学习负担，提高了面部渲染的准确性，在图像质量和唇形同步方面优于最先进的方法。
（2）创新点：</p>
</li>
<li>提出了一种基于注意力机制的解耦神经辐射场说话人面部合成方法（NeRF-AD）。</li>
<li>引入了一个基于注意力的解耦模块，利用与语音相关的面部动作单元（AU）信息将面部解耦为音频面部和身份面部。</li>
<li>只将音频面部与音频特征融合，并利用 AU 信息监督这两个模态的融合。</li>
<li>对说话的面部进行了分解，并为 NeRF 提供了两个分解的精确条件。</li>
<li>提出了一个基于注意力的解耦模块，允许音频与与语音运动相关的面部区域精确融合。</li>
<li>采用一系列方法来监督整个过程。
性能：</li>
<li>在图像质量和唇形同步方面优于最先进的方法。
工作量：</li>
<li>需要收集和预处理说话人面部数据和音频数据。</li>
<li>需要训练 NeRF 模型和注意力解耦模块。</li>
<li>需要渲染合成说话人面部视频。</li>
</ol>



<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-964938af99e1099b95b512a910ce466c.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-39deb199fcbfcf9dedfebf11b5272218.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-d53c04a42d143a126e5b391f40684f6a.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-55f96488825fc7af3820d32c3f4ac6ff.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-1072a698b0f056bb4d49ab4715962395.jpg" align="middle">
</details>
