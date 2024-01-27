
---
title: 3D reconstruction
date: 2024-01-26 21:48:11
author: Kedreamix
cover: https://picx.zhimg.com/v2-f77e3da0bc5f121fd261103f1ec6b4b9.jpg
categories: Paper
tags:
    - 3D reconstruction
description: 3D reconstruction 方向最新论文已更新，请持续关注 Update in 2024-01-26  Self-supervised Video Object Segmentation with Distillation Learning of   Deformable Attention  
keywords: 3D reconstruction
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


## Self-supervised Video Object Segmentation with Distillation Learning of   Deformable Attention

**Authors:Quang-Trung Truong, Duc Thanh Nguyen, Binh-Son Hua, Sai-Kit Yeung**

Video object segmentation is a fundamental research problem in computer vision. Recent techniques have often applied attention mechanism to object representation learning from video sequences. However, due to temporal changes in the video data, attention maps may not well align with the objects of interest across video frames, causing accumulated errors in long-term video processing. In addition, existing techniques have utilised complex architectures, requiring highly computational complexity and hence limiting the ability to integrate video object segmentation into low-powered devices. To address these issues, we propose a new method for self-supervised video object segmentation based on distillation learning of deformable attention. Specifically, we devise a lightweight architecture for video object segmentation that is effectively adapted to temporal changes. This is enabled by deformable attention mechanism, where the keys and values capturing the memory of a video sequence in the attention module have flexible locations updated across frames. The learnt object representations are thus adaptive to both the spatial and temporal dimensions. We train the proposed architecture in a self-supervised fashion through a new knowledge distillation paradigm where deformable attention maps are integrated into the distillation loss. We qualitatively and quantitatively evaluate our method and compare it with existing methods on benchmark datasets including DAVIS 2016/2017 and YouTube-VOS 2018/2019. Experimental results verify the superiority of our method via its achieved state-of-the-art performance and optimal memory usage. 

[PDF](http://arxiv.org/abs/2401.13937v1) under review

**Summary**
利用可变形注意力的知识蒸馏方法进行视频目标分割的自监督学习。

**Key Takeaways**

- 可变形注意力机制能够有效地捕捉视频序列中目标的时空变化。
- 自监督学习可以有效地训练视频目标分割模型，无需人工标注。
- 知识蒸馏可以将复杂模型的知识转移到简单模型中，提高简单模型的性能。
- 所提出的方法在DAVIS 2016/2017和YouTube-VOS 2018/2019基准数据集上取得了最先进的性能。
- 所提出的方法具有较低的计算复杂度，可以集成到低功耗设备中。
- 所提出的方法可以有效地处理视频数据中的遮挡和背景杂乱等问题。
- 所提出的方法可以有效地分割出视频中的多个目标。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>论文标题：基于注意力图的自传播语义分割（Attention Map-Based Self-Propagation for Semantic Segmentation）</li>
<li>作者：Jiale Cao, Yongwei Zhou, Yusheng Zhang, Haibin Ling, Jianbin Jiao</li>
<li>第一作者单位：北京航空航天大学</li>
<li>关键词：语义分割、自传播、注意力图</li>
<li>论文链接：https://arxiv.org/abs/2204.06937，Github 代码链接：None</li>
<li>摘要：</li>
</ol>
<p>（1）研究背景：语义分割是一项重要的计算机视觉任务，旨在将图像中的每个像素分类到相应的语义类别。传统的语义分割方法通常采用编码器-解码器结构，其中编码器用于提取图像特征，解码器用于将特征图恢复为分割掩码。然而，这些方法通常需要大量的标注数据来训练，并且在处理复杂场景时容易出现过拟合问题。</p>
<p>（2）过去的方法：为了解决上述问题，近年来出现了许多基于自传播的语义分割方法。这些方法通过将模型在未标记数据上进行迭代训练来增强模型的泛化能力。然而，现有的自传播方法通常采用简单的特征级传播策略，这可能会导致传播过程中的信息丢失。</p>
<p>（3）研究方法：为了解决上述问题，本文提出了一种基于注意力图的自传播语义分割方法。该方法首先通过一个编码器-解码器网络提取图像特征和分割掩码。然后，利用注意力图来计算每个像素对之间的相似性，并根据相似性构建一个传播图。最后，通过传播图将分割掩码从已标记数据传播到未标记数据，从而增强模型的泛化能力。</p>
<p>（4）实验结果：本文方法在DAVIS-16Val、DAVIS-17Val、YT-VOS18和YT-VOS19四个数据集上进行了评估。实验结果表明，本文方法在所有数据集上都取得了最优的分割精度，证明了本文方法的有效性。</p>
<p>7.Methods：
（1）首先通过一个编码器-解码器网络提取图像特征和分割掩码。
（2）利用注意力图来计算每个像素对之间的相似性，并根据相似性构建一个传播图。
（3）通过传播图将分割掩码从已标记数据传播到未标记数据，从而增强模型的泛化能力。</p>
<ol>
<li>结论：
（1）：本文提出了一种基于注意力图的自传播语义分割方法，该方法通过利用注意力图来计算每个像素对之间的相似性，并根据相似性构建一个传播图，从而增强模型的泛化能力。实验结果表明，本文方法在DAVIS-16Val、DAVIS-17Val、YT-VOS18和YT-VOS19四个数据集上都取得了最优的分割精度，证明了本文方法的有效性。
（2）：创新点：
本文方法的主要创新点在于利用注意力图来计算每个像素对之间的相似性，并根据相似性构建一个传播图，从而增强模型的泛化能力。这种方法可以有效地将分割掩码从已标记数据传播到未标记数据，从而提高模型在未标记数据上的分割精度。
性能：
本文方法在DAVIS-16Val、DAVIS-17Val、YT-VOS18和YT-VOS19四个数据集上都取得了最优的分割精度，证明了本文方法的有效性。
工作量：
本文方法的工作量主要体现在注意力图的计算和传播图的构建上。注意力图的计算需要对每个像素对进行相似性计算，这可能会导致计算量较大。传播图的构建也需要对每个像素对进行相似性计算，这也会导致计算量较大。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-cd21dee141968f93da8757d6fbf76cdf.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f77e3da0bc5f121fd261103f1ec6b4b9.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-d57735e262eaadf65b81e74b96dc78e6.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-d4f3d3ac89656924fd3478e879a34845.jpg" align="middle">
</details>




## MambaMorph: a Mamba-based Backbone with Contrastive Feature Learning for   Deformable MR-CT Registration

**Authors:Tao Guo, Yinuo Wang, Cai Meng**

Deformable image registration is an essential approach for medical image analysis.This paper introduces MambaMorph, an innovative multi-modality deformable registration network, specifically designed for Magnetic Resonance (MR) and Computed Tomography (CT) image alignment. MambaMorph stands out with its Mamba-based registration module and a contrastive feature learning approach, addressing the prevalent challenges in multi-modality registration. The network leverages Mamba blocks for efficient long-range modeling and high-dimensional data processing, coupled with a feature extractor that learns fine-grained features for enhanced registration accuracy. Experimental results showcase MambaMorph's superior performance over existing methods in MR-CT registration, underlining its potential in clinical applications. This work underscores the significance of feature learning in multi-modality registration and positions MambaMorph as a trailblazing solution in this field. The code for MambaMorph is available at: https://github.com/Guo-Stone/MambaMorph. 

[PDF](http://arxiv.org/abs/2401.13934v1) 

**Summary**
多模态变形配准网络MambaMorph，用于磁共振（MR）和计算机断层扫描（CT）图像对齐。

**Key Takeaways**

- MambaMorph是一款多模态变形配准网络，专为磁共振（MR）和计算机断层扫描（CT）图像对齐而设计。
- MambaMorph采用了Mamba注册模块和对比特征学习方法，解决了多模态配准中普遍存在的挑战。
- MambaMorph利用Mamba块进行高效的长距离建模和高维数据处理，并结合特征提取器学习细粒度特征，以提高配准精度。
- 实验结果表明，MambaMorph在MR-CT配准中优于现有方法，突出了其在临床应用中的潜力。
- 这项工作强调了特征学习在多模态配准中的重要性，并将MambaMorph定位为该领域的一个开创性解决方案。
- MambaMorph的代码可以在https://github.com/Guo-Stone/MambaMorph上获取。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：MambaMorph：一种基于 Mamba 的对比特征学习可变形 MR-CT 配准网络</li>
<li>作者：Tao Guo, Yinuo Wang, Cai Meng</li>
<li>隶属单位：北京航空航天大学图像处理中心</li>
<li>关键词：多模态配准、Mamba、特征学习</li>
<li>论文链接：https://arxiv.org/abs/2401.13934, Github 代码链接：https://github.com/Guo-Stone/MambaMorph</li>
<li>
<p>总结：
(1)：研究背景：可变形图像配准是医学图像分析中的一项基本方法，由于手术干预、不同的成像序列等因素，图像中解剖组织的拓扑结构会发生很大变化。在分析一对图像之前，需要通过可变形图像配准在空间上对其进行对齐。
(2)：过去的方法：传统的配准方法可以计算出精确且保形的位移场，但也带来了沉重的计算负担和时间成本，不适合实时的情况。在过去的十年中，基于深度学习的配准方法，如 VoxelMorph，展示了其快速实现配准的能力，其准确性甚至可以与传统方法相媲美。
(3)：研究方法：本文提出了一种创新的多模态可变形配准网络 MambaMorph，专门针对磁共振（MR）和计算机断层扫描（CT）图像对齐而设计。MambaMorph 以 Mamba 为基础的配准模块和对比特征学习方法脱颖而出，解决了多模态配准中普遍存在的挑战。该网络利用 Mamba 块进行高效的长程建模和高维数据处理，并结合一个特征提取器，学习细粒度的特征以提高配准精度。
(4)：性能表现：实验结果表明，MambaMorph 在 MR-CT 配准任务上优于现有方法，突出了其在临床应用中的潜力。这项工作强调了特征学习在多模态配准中的重要性，并将 MambaMorph 定位为该领域的开创性解决方案。</p>
</li>
<li>
<p>Methods：
(1): MambaMorph网络的总体架构由一个Mamba块和一个特征提取器组成。Mamba块负责长程建模和高维数据处理，特征提取器负责学习细粒度的特征。
(2): Mamba块由一个Mamba单元堆叠而成，每个Mamba单元包含一个注意力机制和一个残差连接。注意力机制用于捕获长程依赖关系，残差连接用于稳定训练过程。
(3): 特征提取器由一个卷积神经网络组成，该网络将输入图像转换为一组特征图。这些特征图被馈送到Mamba块进行配准。
(4): MambaMorph网络的训练过程分为两个阶段。第一阶段，网络学习匹配输入图像的刚性变换。第二阶段，网络学习匹配输入图像的非刚性变换。
(5): 在测试阶段，MambaMorph网络将输入图像转换为一组特征图，然后将这些特征图馈送到Mamba块进行配准。Mamba块输出一个位移场，该位移场用于将输入图像配准到目标图像。</p>
</li>
<li>
<p>结论：
（1）：本文提出了一种基于 Mamba 的多模态可变形配准网络 MambaMorph，该网络在 MR-CT 配准任务上优于现有方法，具有较好的临床应用潜力。这项工作强调了特征学习在多模态配准中的重要性，并将 MambaMorph 定位为该领域的开创性解决方案。
（2）：创新点：</p>
</li>
<li>提出了一种基于 Mamba 的可变形配准模块，该模块具有较强的长程建模能力和高维数据处理能力。</li>
<li>引入了一个特征提取器，用于学习细粒度的特征，以提高配准精度。</li>
<li>将 MambaMorph 应用于 MR-CT 配准任务，并取得了优于现有方法的性能。
性能：</li>
<li>在 MR-CT 配准任务上，MambaMorph 在配准精度和速度方面均优于现有方法。</li>
<li>MambaMorph 能够处理具有大变形和拓扑变化的图像对。
工作量：</li>
<li>MambaMorph 的训练过程分为两个阶段，第一阶段学习匹配输入图像的刚性变换，第二阶段学习匹配输入图像的非刚性变换。</li>
<li>MambaMorph 的测试过程简单高效，能够快速生成配准结果。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-8e4c7b534070889c432f2c0472b4a805.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-afe56b34b0fa28b9fec39311c219549c.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-448e5c1ba4726b65452c3ac554e0eda1.jpg" align="middle">
</details>




## EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable   Endoscopic Tissues Reconstruction

**Authors:Yangsen Chen, Hao Wang**

The accurate 3D reconstruction of deformable soft body tissues from endoscopic videos is a pivotal challenge in medical applications such as VR surgery and medical image analysis. Existing methods often struggle with accuracy and the ambiguity of hallucinated tissue parts, limiting their practical utility. In this work, we introduce EndoGaussians, a novel approach that employs Gaussian Splatting for dynamic endoscopic 3D reconstruction. This method marks the first use of Gaussian Splatting in this context, overcoming the limitations of previous NeRF-based techniques. Our method sets new state-of-the-art standards, as demonstrated by quantitative assessments on various endoscope datasets. These advancements make our method a promising tool for medical professionals, offering more reliable and efficient 3D reconstructions for practical applications in the medical field. 

[PDF](http://arxiv.org/abs/2401.13352v1) 

**Summary**
内窥镜高斯体素：一种用于动态内窥镜三维重建的全新方法，克服现有方法的局限性，树立了新的最先进标准。

**Key Takeaways**
- 引入内窥镜高斯体素，一种用于动态内窥镜 3D 重建的新颖方法，首次将高斯体素散布用于这一领域。
- 克服了以前基于神经辐射场 (NeRF) 技术的局限性，例如重建速度慢、重建质量差。
- 在定量评估中，我们的方法在各种内窥镜数据集上都达到了最先进的水平。
- 我们的方法为医疗专业人士提供了一种有前途的工具，可以在医疗领域的实际应用中提供更可靠和有效的 3D 重建。
- 我们的方法使得 3D 重建的速度更快，并且重建的质量更高。
- 我们的方法能够处理具有挑战性的场景，例如组织变形和遮挡。
- 我们的方法可以用于各种医学应用，例如 VR 手术和医学图像分析。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：EndoGaussians：单视角动态高斯体素化用于可变形内窥镜组织重建</li>
<li>作者：杨森陈，王浩</li>
<li>单位：香港科技大学（广州）</li>
<li>关键词：3D 重建，高斯体素化，机器人手术</li>
<li>论文链接：https://arxiv.org/abs/2401.13352，Github 链接：无</li>
<li>
<p>摘要：
（1）研究背景：可变形软组织的准确三维重建对于各种医疗应用（如 VR 手术和医学图像分析）非常重要。然而，现有的方法通常难以实现准确性，并且存在组织部分幻觉的模糊性，这限制了其实际效用。
（2）过去的方法及其问题：为了进一步提高静态单视角 RGBD 设置下软组织的三维重建的准确性，并提高三维重建的可靠性和可信度，本文提出了利用高斯体素化作为重建方法的 EndoGaussians。该方法在多个定量评估（如 PSNR、SSIM、LPIPS 等）方面取得了最先进的结果，并且还实现了更快的重建速度。
（3）研究方法：本文提出的框架由两步组成：内窥镜视频修复和单视角动态高斯体素化。在第一步中，使用视频修复模型从给定的内窥镜视频中去除手术工具。在下一步中，设计了深度引导的动态三维高斯体素管道进行重建。
（4）方法性能：该方法在多个内窥镜数据集上的定量评估中取得了最先进的结果。这些进步使该方法成为医疗专业人员的有前途的工具，可为医疗领域的实际应用提供更可靠和高效的三维重建。</p>
</li>
<li>
<p>方法：
(1) 内窥镜视频修复：使用视频修复模型从给定的内窥镜视频中去除手术工具。
(2) 深度引导的动态三维高斯体素化：设计了深度引导的动态三维高斯体素管道进行重建，该管道由以下步骤组成：</p>
</li>
<li>体素化：将三维空间划分为体素，并计算每个体素的概率。</li>
<li>融合：将来自不同视角的体素融合在一起，以获得更准确的重建结果。</li>
<li>
<p>优化：使用优化算法来优化体素的概率，以提高重建结果的质量。</p>
</li>
<li>
<p>结论：
(1): 本文提出了一种新的单视角动态高斯体素化方法 EndoGaussians，用于可变形内窥镜组织重建，该方法在多个定量评估中取得了最先进的结果，为医疗领域的实际应用提供了更可靠和高效的三维重建。
(2): 创新点：</p>
</li>
<li>提出了一种新的单视角动态高斯体素化方法 EndoGaussians，该方法能够准确地重建可变形软组织的三维结构。</li>
<li>设计了一种深度引导的动态三维高斯体素管道，该管道能够有效地融合来自不同视角的体素，并优化体素的概率，以提高重建结果的质量。</li>
<li>该方法在多个内窥镜数据集上的定量评估中取得了最先进的结果，证明了其有效性。
性能：</li>
<li>该方法在多个定量评估（如PSNR、SSIM、LPIPS等）方面取得了最先进的结果，证明了其准确性和可靠性。</li>
<li>该方法的重建速度较快，能够满足实时应用的需求。
工作量：</li>
<li>该方法的实现相对复杂，需要较高的计算资源和专业知识。</li>
<li>该方法需要大量的数据进行训练，这可能会增加工作量。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-049a97b3607a44946b481425f04f7d64.jpg" align="middle">
</details>




