
---
title: NeRF
date: 2024-01-26 21:40:03
author: Kedreamix
cover: https://pic1.zhimg.com/v2-55f96488825fc7af3820d32c3f4ac6ff.jpg
categories: Paper
tags:
    - NeRF
description: NeRF 方向最新论文已更新，请持续关注 Update in 2024-01-26  Sketch2NeRF Multi-view Sketch-guided Text-to-3D Generation  
keywords: NeRF
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


## Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation

**Authors:Minglin Chen, Longguang Wang, Weihao Yuan, Yukun Wang, Zhe Sheng, Yisheng He, Zilong Dong, Liefeng Bo, Yulan Guo**

Recently, text-to-3D approaches have achieved high-fidelity 3D content generation using text description. However, the generated objects are stochastic and lack fine-grained control. Sketches provide a cheap approach to introduce such fine-grained control. Nevertheless, it is challenging to achieve flexible control from these sketches due to their abstraction and ambiguity. In this paper, we present a multi-view sketch-guided text-to-3D generation framework (namely, Sketch2NeRF) to add sketch control to 3D generation. Specifically, our method leverages pretrained 2D diffusion models (e.g., Stable Diffusion and ControlNet) to supervise the optimization of a 3D scene represented by a neural radiance field (NeRF). We propose a novel synchronized generation and reconstruction method to effectively optimize the NeRF. In the experiments, we collected two kinds of multi-view sketch datasets to evaluate the proposed method. We demonstrate that our method can synthesize 3D consistent contents with fine-grained sketch control while being high-fidelity to text prompts. Extensive results show that our method achieves state-of-the-art performance in terms of sketch similarity and text alignment. 

[PDF](http://arxiv.org/abs/2401.14257v1) 11 pages, 9 figures

**Summary**
手绘草图引导文本生成三维内容，兼顾写实和可控。

**Key Takeaways**
- 基于文本描述生成三维内容的技术取得了很大进展，但生成的物体缺乏微观控制。
- 草图可以提供一种低成本的微观控制方法，但由于草图的抽象性和模糊性，难以实现灵活的控制。
- 提出了一种多视图草图引导文本生成三维内容的框架，利用预训练的二维扩散模型来监督神经辐射场 (NeRF) 表示的三维场景的优化。
- 设计了一种新颖的同步生成和重建方法来有效地优化 NeRF。
- 收集了两种多视图草图数据集来评估所提出的方法，结果表明该方法可以合成具有精细草图控制且对文本提示具有高保真的三维一致内容。
- 大量的实验结果表明，该方法在草图相似性和文本对齐方面取得了最先进的性能。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：Sketch2NeRF：多视图草图引导的文本到 3D 生成</li>
<li>作者：Minglin Chen, Longguang Wang, Weihao Yuan, Yukun Wang, Zhe Sheng, Yisheng He, Zilong Dong, Liefeng Bo, Yulan Guo</li>
<li>单位：中山大学深圳校区</li>
<li>关键词：文本到 3D、草图控制、神经辐射场</li>
<li>论文链接：https://arxiv.org/abs/2401.14257</li>
<li>摘要：
(1) 研究背景：文本到 3D 方法已经取得了很大的进展，但生成的 3D 对象往往随机且缺乏细粒度的控制。草图提供了一种引入这种细粒度控制的廉价方法。
(2) 过去的方法及其问题：目前的方法难以从草图中实现灵活的控制，因为草图具有抽象性和模糊性。
(3) 论文提出的研究方法：提出了一种多视图草图引导的文本到 3D 生成框架（Sketch2NeRF），将草图控制添加到 3D 生成中。该方法利用预训练的 2D 扩散模型来监督由神经辐射场 (NeRF) 表示的 3D 场景的优化。
(4) 方法在任务和性能上的表现：在两个多视图草图数据集上评估了该方法。结果表明，该方法能够合成与草图一致的 3D 内容，同时对文本提示具有很高的保真度。该方法在草图相似性和文本对齐方面取得了最先进的性能。</li>
</ol>
<p><Methods>:
(1): 我们提出了一种多视图草图引导的文本到3D生成框架（Sketch2NeRF），将草图控制添加到3D生成中。该方法利用预训练的2D扩散模型来监督由神经辐射场(NeRF)表示的3D场景的优化。
(2): 我们使用神经辐射场（NeRF）来表示3D对象，NeRF是一种灵活且能够渲染出逼真图像的表示方法。
(3): 为了将草图约束纳入多视图中，我们使用了一个预训练的2D草图条件扩散模型。
(4): 我们提出了一种同步生成和重建方法来有效地优化具有ControlNet引导的NeRF。
(5): 在生成阶段，我们使用ControlNet在草图的特定姿势下生成真实图像，同时使用Stable Diffusion在随机采样的姿势下生成真实图像。
(6): 在重建阶段，我们更新NeRF参数，使生成的图像和渲染的图像之间的重建损失最小化。</p>
<ol>
<li>结论：
（1）：本文提出了一种新颖的多视图草图引导的文本到3D生成方法（即 Sketch2NeRF），该方法能够生成与给定草图高度相似的 3D 内容，并且对文本提示具有很高的保真度。
（2）：创新点：</li>
<li>提出了一种多视图草图引导的文本到 3D 生成框架，将草图控制添加到 3D 生成中。</li>
<li>使用预训练的 2D 扩散模型来监督由神经辐射场 (NeRF) 表示的 3D 场景的优化。</li>
<li>提出了一种同步生成和重建方法来有效地优化具有 ControlNet 引导的 NeRF。
性能：</li>
<li>在两个多视图草图数据集上评估了该方法。</li>
<li>结果表明，该方法能够合成与草图一致的 3D 内容，同时对文本提示具有很高的保真度。</li>
<li>该方法在草图相似性和文本对齐方面取得了最先进的性能。
工作量：</li>
<li>该方法需要预训练一个 2D 扩散模型和一个 ControlNet。</li>
<li>该方法需要对 NeRF 进行优化，这可能需要大量的时间和计算资源。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-9b87019fdc56ce6a98f7417d87e3eeb3.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1b34892d79bbf579fd2106569ec88f5d.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-c252ac3ea2c0fd943decf528877343ee.jpg" align="middle">
</details>




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
- <ol>
  <li><p>标题：DREAM-Talk：基于扩散的逼真情感音频驱动的单张图像说话人脸生成方法</p>
  </li>
  <li><p>作者：陈旭章<em>, 王超</em>, 张建峰, 徐鸿毅, 宋国贤, 谢宇, 罗林杰, 田亚鹏, 郭晓虎, 冯佳世</p>
  </li>
  <li><p>单位：字节跳动公司</p>
  </li>
  <li><p>关键词：情感说话人脸生成；扩散模型；音频驱动；唇形同步</p>
  </li>
  <li><p>论文链接：https://arxiv.org/abs/2312.13578</p>
  </li>
  <li><p>摘要：
  (1) 研究背景：从单张人像图像生成情感说话人脸仍然是一项重大挑战。同时实现富有表现力的情感说话和准确的唇形同步尤其困难，因为表现力通常会因唇形同步的准确性而受到损害。LSTM 网络被许多先前的工作广泛采用，但往往无法捕捉情感表达的细微差别和变化。
  (2) 过去的方法及其问题：为了解决这些挑战，我们引入了 DREAM-Talk，这是一个两阶段的基于扩散的音频驱动框架，专门用于同时生成多样化的表情和准确的唇形同步。在第一阶段，我们提出了 EmoDiiff，一个新颖的扩散模块，该模块根据音频和参考情感风格生成多样化的高度动态情感表达和头部姿势。鉴于唇部运动与音频之间存在很强的相关性，我们随后使用音频特征和情感风格来增强唇形同步准确性，从而优化动态效果。为此，我们部署了一个视频到视频渲染模块，将我们代理 3D 头像的表情和唇部动作转移到任意人像上。
  (3) 本文提出的研究方法：在定量和定性方面，DREAM-Talk 在表现力、唇形同步准确性和感知质量方面都优于最先进的方法。
  (4) 方法在什么任务上取得了什么性能？性能是否支持其目标：该方法在情感说话人脸生成任务上取得了很好的性能。在定量评估中，DREAM-Talk 在三个基准数据集上实现了最先进的结果，在情感多样性、唇形同步准确性和感知质量方面均优于现有方法。在定性评估中，DREAM-Talk 生成的说话人脸具有逼真的情感表达、准确的唇形同步和很高的视觉质量。这些结果支持了该方法的目标，即生成具有多样化情感表达和准确唇形同步的逼真说话人脸。</p>
  </li>
  <li><p>方法：
  (1) 提出EmoDiff，一个新颖的扩散模块，根据音频和参考情感风格生成多样化的高度动态情感表达和头部姿势。
  (2) 部署视频到视频渲染模块，将代理3D头像的表情和唇部动作转移到任意人像上。
  (3) 使用音频特征和情感风格来增强唇形同步准确性，从而优化动态效果。</p>
  </li>
  <li><p>结论：
  （1）：本文提出了一种名为DREAM-Talk的创新框架，该框架专为生成具有精确唇形同步的情感表达说话人脸而设计。我们的两阶段方法，包括EmoDiff模块和唇形细化，有效地捕捉了情感细微差别并确保了准确的唇形同步。利用情感条件扩散模型和唇形细化网络，我们的方法优于现有技术。我们的结果表明，在保持高视频质量的同时，面部情感表达能力得到了提高。DREAM-Talk代表了情感说话人脸生成领域向前迈出的重要一步，它使跨越广泛应用范围的逼真且情感参与的数字人形表征的创建成为可能。
  （2）：创新点：
  提出了一种新颖的扩散模块EmoDiff，该模块根据音频和参考情感风格生成多样化的高度动态情感表达和头部姿势。
  部署了一个视频到视频渲染模块，将代理3D头像的表情和唇部动作转移到任意人像上。
  使用音频特征和情感风格来增强唇形同步准确性，从而优化动态效果。
  性能：
  在定量评估中，DREAM-Talk在三个基准数据集上实现了最先进的结果，在情感多样性、唇形同步准确性和感知质量方面均优于现有方法。
  在定性评估中，DREAM-Talk生成的说话人脸具有逼真的情感表达、准确的唇形同步和很高的视觉质量。
  工作量：
  该方法需要大量的数据和计算资源来训练模型。
  该方法需要专业知识来实现和部署。</p>
  </li>
  </ol>

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


## IPR-NeRF: Ownership Verification meets Neural Radiance Field

**Authors:Win Kent Ong, Kam Woh Ng, Chee Seng Chan, Yi Zhe Song, Tao Xiang**

Neural Radiance Field (NeRF) models have gained significant attention in the computer vision community in the recent past with state-of-the-art visual quality and produced impressive demonstrations. Since then, technopreneurs have sought to leverage NeRF models into a profitable business. Therefore, NeRF models make it worth the risk of plagiarizers illegally copying, re-distributing, or misusing those models. This paper proposes a comprehensive intellectual property (IP) protection framework for the NeRF model in both black-box and white-box settings, namely IPR-NeRF. In the black-box setting, a diffusion-based solution is introduced to embed and extract the watermark via a two-stage optimization process. In the white-box setting, a designated digital signature is embedded into the weights of the NeRF model by adopting the sign loss objective. Our extensive experiments demonstrate that not only does our approach maintain the fidelity (\ie, the rendering quality) of IPR-NeRF models, but it is also robust against both ambiguity and removal attacks compared to prior arts. 

[PDF](http://arxiv.org/abs/2401.09495v3) Error on result tabulation for the state of the art method which   might cause misleading to the readers

**摘要**
利用水印优化与签署保护 NeRF 模型的知识产权。

**要点**

- IPR-NeRF 框架在黑盒和白盒设置中提供了 NeRF 模型的知识产权保护。
- 在黑盒设置中，使用基于扩散的解决方案通过两阶段优化过程嵌入和提取水印。
- 在白盒设置中，通过采用符号损失目标，将指定的数字签名嵌入到 NeRF 模型的权重中。
- IPR-NeRF 模型不仅保持了渲染质量，而且与现有技术相比，它还具有鲁棒性，可抵抗模糊和移除攻击。
- IPR-NeRF 模型在用于生成合成数据的视觉效果时，能够有效防止模型窃取和误用。
- IPR-NeRF 模型还可用于保护 NeRF 模型在商业环境中的知识产权。
- IPR-NeRF 模型为 NeRF 模型的知识产权保护提供了一种通用解决方案。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li><p>题目：IPR-NeRF：所有权验证满足神经辐射场（中文翻译：IPR-NeRF：所有权验证满足神经辐射场）</p>
</li>
<li><p>作者：Kent Ong、Kam Woh Ng、Chee Seng Chan、Yi Zhe Song、Tao Xiang</p>
</li>
<li><p>第一作者单位：马来亚大学图像与信号处理中心（中文翻译：马来亚大学图像与信号处理中心）</p>
</li>
<li><p>关键词：神经辐射场、知识产权保护、数字水印、数字签名</p>
</li>
<li><p>论文链接：https://arxiv.org/abs/2401.09495，Github 代码链接：无</p>
</li>
<li><p>摘要：
（1）研究背景：神经辐射场 (NeRF) 模型因其出色的视觉质量和令人印象深刻的演示而在计算机视觉领域引起了广泛关注。NeRF 模型的商业价值也引起了技术企业家的注意，但这也使得 NeRF 模型面临被非法复制、再分发或滥用的风险。
（2）过去的方法及其问题：目前还没有针对 NeRF 模型的知识产权保护框架。现有的保护方案主要针对卷积神经网络 (CNN)、生成对抗网络 (GAN) 和循环神经网络 (RNN)。这些方法在设计 NeRF 模型的保护框架时面临诸多挑战，例如现有黑盒保护方法在 NeRF 渲染过程中会导致水印无法恢复。
（3）提出的研究方法：本文提出了一种针对 NeRF 模型的综合知识产权保护框架，称为 IPR-NeRF。在黑盒设置中，引入了一种基于扩散的解决方案，通过两阶段优化过程嵌入和提取水印。在白盒设置中，通过采用符号损失目标函数，将指定数字签名嵌入 NeRF 模型的权重中。
（4）方法在任务和性能上的表现：实验结果表明，IPR-NeRF 方法不仅保持了 NeRF 模型的保真度（即渲染质量），而且在面对模糊性和去除攻击时也表现出比以往方法更强的鲁棒性。这些性能支持了本文提出的方法的目标。</p>
</li>
<li><p>方法：
(1) IPR-NeRF 框架概述：IPR-NeRF 框架包含两个主要模块：黑盒保护模块和白盒保护模块。黑盒保护模块旨在保护未经授权访问的 NeRF 模型，而白盒保护模块旨在保护经授权访问的 NeRF 模型。
(2) 黑盒保护模块：黑盒保护模块采用基于扩散的解决方案，通过两阶段优化过程嵌入和提取水印。在嵌入阶段，将水印嵌入到 NeRF 模型的权重中，在提取阶段，从渲染的图像中提取水印。
(3) 白盒保护模块：白盒保护模块采用符号损失目标函数，将指定数字签名嵌入 NeRF 模型的权重中。符号损失目标函数旨在最小化数字签名与 NeRF 模型权重的差异，从而确保数字签名被嵌入到 NeRF 模型中。
(4) 实验结果：实验结果表明，IPR-NeRF 方法不仅保持了 NeRF 模型的保真度，而且在面对模糊性和去除攻击时也表现出比以往方法更强的鲁棒性。</p>
</li>
<li><p>结论：
（1）：IPR-NeRF：所有权验证满足神经辐射场，提出了一种针对 NeRF 模型的全面且鲁棒的知识产权保护方案，在黑盒和白盒场景中均能有效保护模型。综合实验结果表明，该方案在抵抗嵌入水印的模糊性和去除攻击方面表现出优异的性能，同时保持了渲染性能。然而，该方案在计算能力和黑盒保护方面存在局限性，当攻击者拥有受保护模型的详细信息时，该方案无法抵御覆盖攻击。未来的研究将集中在改进这些方面。
（2）：创新点：</p>
</li>

<ul>
<li>提出了一种综合的 NeRF 模型知识产权保护框架，该框架在黑盒和白盒场景中均能有效保护模型。</li>
<li>引入了一种基于扩散的解决方案，通过两阶段优化过程嵌入和提取水印，在黑盒设置中保护未经授权访问的 NeRF 模型。</li>
<li>采用符号损失目标函数，将指定数字签名嵌入 NeRF 模型的权重中，在白盒设置中保护经授权访问的 NeRF 模型。</li>
</ul>
<p>性能：</p>
<ul>
<li>实验结果表明，该方案不仅保持了 NeRF 模型的保真度，而且在面对模糊性和去除攻击时也表现出比以往方法更强的鲁棒性。</li>
</ul>
<p>工作量：</p>
<ul>
<li>该方案在计算能力和黑盒保护方面存在局限性，当攻击者拥有受保护模型的详细信息时，该方案无法抵御覆盖攻击。</li>
</ul>




<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-7702dd0580aeb20d2469586499df517d.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-b6cd7f525efd45ad04614d4ae868c5ff.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-cd4e10da5a013a99ebc46d33f1e102a8.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-ed46804675ae115b408ec3a1b30d40dd.jpg" align="middle">
</details>

​    

