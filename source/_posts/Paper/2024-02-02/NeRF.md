
---
title: NeRF
date: 2024-02-02 22:27:07
author: Kedreamix
cover: https://picx.zhimg.com/v2-f5c934d1ebae9f51cda700d605228196.jpg
categories: Paper
tags:
    - NeRF
description: NeRF 方向最新论文已更新，请持续关注 Update in 2024-02-02  ViCA-NeRF View-Consistency-Aware 3D Editing of Neural Radiance Fields  
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
---

>⚠️ 以下所有内容总结都来自于 Google的大语言模型[Gemini-Pro](https://ai.google.dev/)的能力，如有错误，仅供参考，谨慎使用
>🔴 请注意：千万不要用于严肃的学术场景，只能用于论文阅读前的初筛！
>💗 如果您觉得我们的项目对您有帮助 [ChatPaperFree](https://github.com/Kedreamix/ChatPaperFree) ，还请您给我们一些鼓励！⭐️ [HuggingFace免费体验](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)

# 2024-02-02 更新


## ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields

**Authors:Jiahua Dong, Yu-Xiong Wang**

We introduce ViCA-NeRF, the first view-consistency-aware method for 3D editing with text instructions. In addition to the implicit neural radiance field (NeRF) modeling, our key insight is to exploit two sources of regularization that explicitly propagate the editing information across different views, thus ensuring multi-view consistency. For geometric regularization, we leverage the depth information derived from NeRF to establish image correspondences between different views. For learned regularization, we align the latent codes in the 2D diffusion model between edited and unedited images, enabling us to edit key views and propagate the update throughout the entire scene. Incorporating these two strategies, our ViCA-NeRF operates in two stages. In the initial stage, we blend edits from different views to create a preliminary 3D edit. This is followed by a second stage of NeRF training, dedicated to further refining the scene's appearance. Experimental results demonstrate that ViCA-NeRF provides more flexible, efficient (3 times faster) editing with higher levels of consistency and details, compared with the state of the art. Our code is publicly available. 

[PDF](http://arxiv.org/abs/2402.00864v1) Neurips2023; project page: https://github.com/Dongjiahua/VICA-NeRF

**Summary**
文本引入了一种新的方法 ViCA-NeRF，该方法可以利用文本编辑进行 3D 编辑，并使用几何和学习正则化来确保编辑的多视图一致性。

**Key Takeaways**
- ViCA-NeRF 是一种新颖的基于文本的 3D 编辑方法，利用 NeRF 进行隐式神经辐射场建模。
- ViCA-NeRF 的关键思想是利用两种正则化来源，明确地在不同视图之间传播编辑信息，确保多视图一致性。
- ViCA-NeRF 利用从 NeRF 推导出的深度信息来建立不同视图之间的图像对应关系，用于几何正则化。
- ViCA-NeRF 对经过编辑和未经过编辑的图像在 2D 扩散模型中的潜在编码进行对齐，实现编辑关键视图并更新整个场景。
- ViCA-NeRF 采用两个阶段的工作流程，第一阶段将来自不同视图的编辑融合，创建初步的 3D 编辑。
- 第二阶段进行 NeRF 训练，进一步优化场景的外观。
- 与现有技术相比，ViCA-NeRF 提供更灵活、更高效（速度提升 3 倍）、更一致且更详细的编辑。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：ViCA-NeRF：基于视图一致性的神经辐射场三维编辑</li>
<li>作者：Jiahua Dong, Yu-Xiong Wang</li>
<li>单位：伊利诺伊大学厄巴纳-香槟分校</li>
<li>关键词：三维编辑、神经辐射场、视图一致性、文本指令</li>
<li>论文链接：https://arxiv.org/abs/2402.00864
Github 链接：https://dongjiahua.github.io/VICA-NeRF</li>
<li>
<p>摘要：
(1)：随着神经辐射场（NeRF）及其变体的最新进展，收集真实世界三维场景数据变得更加便捷。然而，现有的三维编辑方法通常缺乏视图一致性，导致编辑结果在不同视角下可能出现不一致的情况。
(2)：过去的方法主要包括基于几何的正则化和基于学习的正则化。几何正则化利用 NeRF 提取的深度信息来建立不同视角之间的图像对应关系，从而确保视图一致性。学习正则化则通过对编辑图像和未编辑图像的潜在代码进行对齐，使编辑信息能够在整个场景中传播。
(3)：本文提出的 ViCA-NeRF 是一种基于视图一致性的三维编辑方法，它结合了几何正则化和学习正则化两种策略。ViCA-NeRF 首先通过融合来自不同视角的编辑结果来创建初步的三维编辑，然后通过 NeRF 训练进一步细化场景的外观，从而确保视图一致性和细节丰富。
(4)：实验结果表明，与现有方法相比，ViCA-NeRF 提供了更加灵活、高效（速度提高 3 倍）的编辑方式，并且具有更高的视图一致性和细节水平。</p>
</li>
<li>
<p>方法：
(1) ViCA-NeRF 首先从不同视角收集输入图像，并使用 NeRF 从这些图像中提取深度信息。
(2) 然后，ViCA-NeRF 利用提取的深度信息来建立不同视角之间的图像对应关系，并使用这些对应关系来融合来自不同视角的编辑结果，从而创建初步的三维编辑。
(3) 最后，ViCA-NeRF 通过 NeRF 训练进一步细化场景的外观，从而确保视图一致性和细节丰富。</p>
</li>
<li>
<p>结论：
（1）：本文提出了 ViCA-NeRF，一种基于视图一致性的三维编辑框架，用于文本引导的 NeRF 编辑。给定文本指令，我们可以高效地编辑 NeRF。除了像人类风格化和天气变化这样的简单任务外，我们还支持上下文相关的操作，例如“添加一些花朵”和编辑高度详细的纹理。我们的方法在各种场景和文本提示上优于几个基线。未来，我们将继续提高三维编辑的可控性和真实性。
（2）：创新点：
ViCA-NeRF 结合了几何正则化和学习正则化两种策略，以确保视图一致性和细节丰富。
ViCA-NeRF 利用提取的深度信息来建立不同视角之间的图像对应关系，并使用这些对应关系来融合来自不同视角的编辑结果，从而创建初步的三维编辑。
ViCA-NeRF 通过 NeRF 训练进一步细化场景的外观，从而确保视图一致性和细节丰富。
性能：
ViCA-NeRF 在各种场景和文本提示上优于几个基线。
ViCA-NeRF 的速度提高了 3 倍。
工作量：
ViCA-NeRF 的实现相对简单。
ViCA-NeRF 的训练和推理速度较快。</p>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-b3cbdca659df3ac2eb7b2521752d1c8e.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f5c934d1ebae9f51cda700d605228196.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-40418c9a6b8bcda24387d9b40ab2cd3a.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1ff0299de61f2dcce94a6f84b195a4b3.jpg" align="middle">
</details>




