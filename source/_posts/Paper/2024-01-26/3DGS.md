
---
title: 3DGS
date: 2024-01-26 21:31:01
author: Kedreamix
cover: https://pic1.zhimg.com/v2-e297ea1e2c85e96907865cc0d6107864.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-01-26  EndoGaussians Single View Dynamic Gaussian Splatting for Deformable   Endoscopic Tissues Reconstruction  
keywords: 3DGS
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


## EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable   Endoscopic Tissues Reconstruction

**Authors:Yangsen Chen, Hao Wang**

The accurate 3D reconstruction of deformable soft body tissues from endoscopic videos is a pivotal challenge in medical applications such as VR surgery and medical image analysis. Existing methods often struggle with accuracy and the ambiguity of hallucinated tissue parts, limiting their practical utility. In this work, we introduce EndoGaussians, a novel approach that employs Gaussian Splatting for dynamic endoscopic 3D reconstruction. This method marks the first use of Gaussian Splatting in this context, overcoming the limitations of previous NeRF-based techniques. Our method sets new state-of-the-art standards, as demonstrated by quantitative assessments on various endoscope datasets. These advancements make our method a promising tool for medical professionals, offering more reliable and efficient 3D reconstructions for practical applications in the medical field. 

[PDF](http://arxiv.org/abs/2401.13352v1) 

**摘要**
高斯放射技术助力打造动态内窥镜三维重建新标杆。

**要点**

- 基于神经辐射场（NeRF）的方法在动态内窥镜三维重建任务中存在重建精度低、易产生模糊组织结构等局限性。
- 本文首次将高斯放射技术应用于动态内窥镜三维重建任务，提出了名为EndoGaussians的新方法，克服了NeRF方法的局限性。
- EndoGaussians方法在各项内窥镜数据集上均取得了最先进的重建效果。
- EndoGaussians方法可为医疗专业人士提供更加可靠、高效的三维重建结果，有助于该技术在医疗领域的实际应用。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：EndoGaussians：单视图动态高斯体素重建</li>
<li>作者：Yangsen Chen, Hao Wang</li>
<li>单位：香港科技大学（广州）</li>
<li>关键词：3D 重建、高斯体素、机器人手术</li>
<li>论文链接：https://arxiv.org/abs/2401.13352v1，Github 链接：无</li>
<li>
<p>摘要：
（1）研究背景：准确地从内窥镜视频中重建可变形软体组织的 3D 模型对于医学应用（如 VR 手术和医学图像分析）至关重要。现有的方法通常难以达到精度要求，并且存在组织部分出现模糊的情况，限制了其实际应用。
（2）过去的方法及其问题：深度估计方法和 SLAM 方法对于重建复杂场景的准确性较差；基于稀疏扭曲场的重建方法在变形超出非拓扑变化范围时会退化；基于神经辐射场的重建方法存在重建结果中哪些部分基于真实数据、哪些部分是虚构的不明确的问题。
（3）研究方法：本文提出了一种新的方法 EndGaussians，它利用高斯体素进行动态内窥镜 3D 重建。该方法是首次将高斯体素应用于此场景，克服了以前基于神经辐射场技术的局限性。
（4）方法性能：在多个内窥镜数据集上进行的定量评估表明，该方法达到了最先进的水平。这些进步使该方法成为医疗专业人员的有力工具，为医学领域的实际应用提供了更可靠、更高效的 3D 重建。</p>
</li>
<li>
<p>Methods:
(1): 该方法将高斯体素应用于动态内窥镜3D重建，克服了以前基于神经辐射场技术的局限性。
(2): 该方法通过将高斯体素作为隐式表示来建模场景，并使用神经网络来预测高斯体素的参数。
(3): 该方法使用一种新的损失函数来训练神经网络，该损失函数可以同时优化重建的质量和高斯体素的分布。
(4): 该方法使用一种新的采样策略来生成高斯体素，该采样策略可以提高重建的效率和准确性。
(5): 该方法使用一种新的融合策略来融合来自不同视图的高斯体素，该融合策略可以提高重建的鲁棒性和完整性。</p>
</li>
<li>
<p>结论：
（1）：本文提出了一种新的方法EndGaussians，它利用高斯体素进行动态内窥镜3D重建。该方法是首次将高斯体素应用于此场景，克服了以前基于神经辐射场技术的局限性。在多个内窥镜数据集上进行的定量评估表明，该方法达到了最先进的水平。这些进步使该方法成为医疗专业人员的有力工具，为医学领域的实际应用提供了更可靠、更高效的3D重建。
（2）：创新点：</p>
</li>
<li>将高斯体素应用于动态内窥镜3D重建，克服了以前基于神经辐射场技术的局限性。</li>
<li>使用一种新的损失函数来训练神经网络，该损失函数可以同时优化重建的质量和高斯体素的分布。</li>
<li>使用一种新的采样策略来生成高斯体素，该采样策略可以提高重建的效率和准确性。</li>
<li>使用一种新的融合策略来融合来自不同视图的高斯体素，该融合策略可以提高重建的鲁棒性和完整性。
性能：</li>
<li>在多个内窥镜数据集上进行的定量评估表明，该方法达到了最先进的水平。</li>
<li>该方法可以生成高质量的3D重建，并且可以很好地处理复杂场景和变形组织。</li>
<li>该方法具有较高的效率和准确性，可以满足医疗应用的要求。
工作量：</li>
<li>该方法的实现难度较高，需要较强的编程能力和数学基础。</li>
<li>该方法的训练时间较长，需要较大的计算资源。</li>
<li>该方法的应用场景有限，目前仅适用于医疗领域。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-049a97b3607a44946b481425f04f7d64.jpg" align="middle">
</details>




## EndoGaussian: Gaussian Splatting for Deformable Surgical Scene   Reconstruction

**Authors:Yifan Liu, Chenxin Li, Chen Yang, Yixuan Yuan**

Reconstructing deformable tissues from endoscopic stereo videos is essential in many downstream surgical applications. However, existing methods suffer from slow inference speed, which greatly limits their practical use. In this paper, we introduce EndoGaussian, a real-time surgical scene reconstruction framework that builds on 3D Gaussian Splatting. Our framework represents dynamic surgical scenes as canonical Gaussians and a time-dependent deformation field, which predicts Gaussian deformations at novel timestamps. Due to the efficient Gaussian representation and parallel rendering pipeline, our framework significantly accelerates the rendering speed compared to previous methods. In addition, we design the deformation field as the combination of a lightweight encoding voxel and an extremely tiny MLP, allowing for efficient Gaussian tracking with a minor rendering burden. Furthermore, we design a holistic Gaussian initialization method to fully leverage the surface distribution prior, achieved by searching informative points from across the input image sequence. Experiments on public endoscope datasets demonstrate that our method can achieve real-time rendering speed (195 FPS real-time, 100$\times$ gain) while maintaining the state-of-the-art reconstruction quality (35.925 PSNR) and the fastest training speed (within 2 min/scene), showing significant promise for intraoperative surgery applications. Code is available at: \url{https://yifliu3.github.io/EndoGaussian/}. 

[PDF](http://arxiv.org/abs/2401.12561v1) 

**Summary**
实时三维手术场景重构算法EndoGaussian可实现实时渲染，并享有优异的重建质量，为术中手术应用提供强劲支持。

**Key Takeaways**

- EndoGaussian 是一种创新的实时手术场景重建框架，基于 3D 高斯散点图构建。
- 该框架将动态手术场景表示为典型高斯分布和时间相关变形场，可在新时间戳预测高斯变形。
- 高效的高斯表示和并行渲染管道，使该框架的渲染速度显著加快。
- 该框架采用轻量级编码体素和极小 MLP 相结合的方式设计变形场，带来高效的高斯跟踪与小幅渲染负担。
- 提供了一种整体高斯初始化方法，可从整个输入图像序列搜索信息点以充分利用表面分布先验。
- 在公开内窥镜数据集上的实验表明，该方法可实现实时的渲染速度（195 FPS 实时，100 倍提升），同时保持最先进的重建质量（35.925 PSNR）和最快的训练速度（2 分钟/场 景以内），为术中手术应用展现了巨大的前景。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：EndoGaussian：用于可变形手术场景重建的高斯飞溅</li>
<li>作者：Yifan Liu、Chenxin Li、Chen Yang 和 Yixuan Yuan</li>
<li>隶属关系：香港中文大学</li>
<li>关键词：3D 重建·高斯飞溅·机器人手术</li>
<li>论文链接：https://arxiv.org/abs/2401.12561，Github 代码链接：https://yifliu3.github.io/EndoGaussian/</li>
<li>
<p>摘要：
（1）研究背景：从内窥镜立体视频中重建手术场景对于许多下游手术应用至关重要。然而，现有方法的推理速度慢，极大地限制了其实际使用。
（2）过去的方法及其问题：以往的方法存在推理速度慢的问题，限制了其实际使用。本文提出的方法动机明确，旨在解决这一问题。
（3）研究方法：本文提出了一种基于 3D 高斯飞溅的实时手术场景重建框架 EndoGaussian。该框架将动态手术场景表示为规范高斯和时间相关变形场，预测新时间戳下的高斯变形。由于高效的高斯表示和并行渲染管道，该框架与以前的方法相比显着提高了渲染速度。此外，本文将变形场设计为轻量级编码体素和极小 MLP 的组合，从而实现高效的高斯跟踪，且渲染负担很小。此外，本文设计了一种整体高斯初始化方法，通过搜索输入图像序列中的信息点来充分利用表面分布先验。
（4）方法性能：在公共内窥镜数据集上的实验表明，本文方法可以实现实时渲染速度（195 FPS 实时，100 倍提升），同时保持最先进的重建质量（35.925 PSNR）和最快的训练速度（2 分钟/场景以内），为术中手术应用展示出巨大的前景。</p>
</li>
<li>
<p>方法：
(1)：提出基于 3D 高斯飞溅的实时手术场景重建框架 EndoGaussian，将动态手术场景表示为规范高斯和时间相关变形场，预测新时间戳下的高斯变形，利用高效的高斯表示和并行渲染管道大幅提升渲染速度。
(2)：将变形场设计为轻量级编码体素和极小 MLP 的组合，实现高效的高斯跟踪，且渲染负担很小。
(3)：设计整体高斯初始化方法，通过搜索输入图像序列中的信息点充分利用表面分布先验。</p>
</li>
<li>
<p>结论：
（1）本工作提出了一种实时且高质量的 4D 重建框架，用于动态手术场景重建。通过利用基于体素的高斯跟踪和整体高斯初始化，我们可以处理组织变形和非平凡的高斯初始化问题。综合实验表明，我们的 EndoGaussian 可以实现最先进的重建质量和实时的渲染速度，比以前的方法快 100 倍以上。我们希望新兴的基于高斯飞溅的重建技术可以为机器人手术场景理解提供新的途径，并增强各种下游临床任务，尤其是术中应用。
（2）创新点：
提出了一种基于 3D 高斯飞溅的实时手术场景重建框架 EndoGaussian，将动态手术场景表示为规范高斯和时间相关变形场，预测新时间戳下的高斯变形，利用高效的高斯表示和并行渲染管道大幅提升渲染速度。
将变形场设计为轻量级编码体素和极小 MLP 的组合，实现高效的高斯跟踪，且渲染负担很小。
设计整体高斯初始化方法，通过搜索输入图像序列中的信息点充分利用表面分布先验。
性能：
在公共内窥镜数据集上的实验表明，本文方法可以实现实时渲染速度（195FPS 实时，100 倍提升），同时保持最先进的重建质量（35.925PSNR）和最快的训练速度（2分钟/场景以内），为术中手术应用展示出巨大的前景。
工作量：
本文方法的实现复杂度较高，需要较高的计算资源和专业知识。</p>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-0b9bca825762ac8e0bbad3078a233ed1.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-e1d91551398571ef4d862b170f54e4fc.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-d93c7e9f9dfadf417d2add6f22082d7e.jpg" align="middle">
</details>




## CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians with   Dual Feature Fusion

**Authors:Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan**

We propose Compact and Swift Segmenting 3D Gaussians(CoSSegGaussians), a method for compact 3D-consistent scene segmentation at fast rendering speed with only RGB images input. Previous NeRF-based segmentation methods have relied on time-consuming neural scene optimization. While recent 3D Gaussian Splatting has notably improved speed, existing Gaussian-based segmentation methods struggle to produce compact masks, especially in zero-shot segmentation. This issue probably stems from their straightforward assignment of learnable parameters to each Gaussian, resulting in a lack of robustness against cross-view inconsistent 2D machine-generated labels. Our method aims to address this problem by employing Dual Feature Fusion Network as Gaussians' segmentation field. Specifically, we first optimize 3D Gaussians under RGB supervision. After Gaussian Locating, DINO features extracted from images are applied through explicit unprojection, which are further incorporated with spatial features from the efficient point cloud processing network. Feature aggregation is utilized to fuse them in a global-to-local strategy for compact segmentation features. Experimental results show that our model outperforms baselines on both semantic and panoptic zero-shot segmentation task, meanwhile consumes less than 10\% inference time compared to NeRF-based methods. Code and more results will be available at https://David-Dou.github.io/CoSSegGaussians. 

[PDF](http://arxiv.org/abs/2401.05925v2) Correct writing details

**Summary**
针对3D高斯体素方法中零样本分割效果欠佳的问题，提出了一种紧凑的快速3D高斯体素分割方法，在保证快速渲染速度的同时，仅使用RGB图像即可实现紧凑的3D一致场景分割效果。

**Key Takeaways**
- 我们提出了一种紧凑的快速3D高斯体素分割方法（CoSSegGaussians）。
- CoSSegGaussians仅使用RGB图像作为输入，即可实现快速的3D一致场景分割。
- CoSSegGaussians采用双特征融合网络作为高斯体素的分割域，以解决传统方法中存在的问题。
- CoSSegGaussians通过显式反投影将从图像中提取的DINO特征应用到空间特征中，以实现全局到局部的融合策略。
- 实验结果表明，CoSSegGaussians在语义和全景零样本分割任务上均优于基线方法，同时推理时间仅为基于NeRF方法的10%。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：紧凑而快速的场景分割 3D 高斯体与双重特征融合</li>
<li>作者：Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan</li>
<li>单位：西安交通大学人工智能与机器人研究所</li>
<li>关键词：神经辐射场、3D 高斯体、场景分割、无监督学习</li>
<li>论文链接：https://arxiv.org/abs/2401.05925
Github 代码链接：None</li>
<li>摘要：
(1)：近年来，计算机视觉和计算机图形学取得了显着进步，特别是在神经渲染领域。神经辐射场 (NeRF) 及其后续方法推动了神经场景表示的发展，这些方法已显示出显着的用于新视图合成的能力。
(2)：以往基于 NeRF 的分割方法依赖于耗时的神经场景优化。虽然最近的 3D 高斯体 splatting 显着提高了速度，但现有的基于高斯体的分割方法难以生成紧凑的掩码，尤其是在零样本分割中。这个问题可能源于它们将可学习参数直接分配给每个高斯体，导致对跨视图不一致的 2D 机器生成的标签缺乏鲁棒性。
(3)：本文提出了一种紧凑而快速的 3D 高斯体分割方法 (CoSSegGaussians)，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度很快。具体来说，我们首先在 RGB 监督下优化 3D 高斯体。在高斯体定位之后，通过显式反投影应用从图像中提取的 DINO 特征，这些特征进一步与来自高效点云处理网络的空间特征结合。利用特征聚合以全局到局部策略将它们融合用于紧凑分割特征。
(4)：实验结果表明，我们的模型在语义和全景零样本分割任务上优于基线，同时与基于 NeRF 的方法相比，推理时间缩短了 90% 以上。</li>
</ol>
<p>7.Methods:
(1): 本文提出了一种紧凑而快速的 3D 高斯体分割方法 (CoSSegGaussians)，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度很快。
(2): 首先在 RGB 监督下优化 3D 高斯体。在高斯体定位之后，通过显式反投影应用从图像中提取的 DINO 特征，这些特征进一步与来自高效点云处理网络的空间特征结合。利用特征聚合以全局到局部策略将它们融合用于紧凑分割特征。
(3): 实验结果表明，我们的模型在语义和全景零样本分割任务上优于基线，同时与基于 NeRF 的方法相比，推理时间缩短了 90% 以上。</p>
<ol>
<li>结论：
（1）：本文提出了一种紧凑而快速的 3D 高斯体分割方法 CoSSegGaussians，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度很快。
（2）：创新点：</li>
<li>将 3D 高斯体与双重特征融合网络相结合，用于分割场。</li>
<li>利用反投影将 DINO 特征引入定位的 3D 高斯体，并进一步与高斯体的空间信息相结合。</li>
<li>应用全局到局部聚合模块生成紧凑的分割逻辑。
性能：</li>
<li>在语义和全景零样本分割任务上优于基线。</li>
<li>与基于 NeRF 的方法相比，推理时间缩短了 90% 以上。
工作量：</li>
<li>实验表明，该方法能够可靠且高效地完成零样本分割任务。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-7b3b4f44e1bfaba57c660121007fee8a.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-222c4f05c24f306aefd909de021e726c.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-e297ea1e2c85e96907865cc0d6107864.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-27a48d664aab4676f21f642635ecb972.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-8a12edf74e5d62d5f426b60407d904ab.jpg" align="middle">
</details>




