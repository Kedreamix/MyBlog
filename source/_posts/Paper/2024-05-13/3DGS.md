
---
title: 3DGS
date: 2024-05-13 16:18:16
author: Kedreamix
cover: https://pic1.zhimg.com/v2-b3dd2127ce2dbe6cdafc1b40d9cc2fb2.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-05-13  OneTo3D One Image to Re-editable Dynamic 3D Model and Video Generation  
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
---

>⚠️ 以下所有内容总结都来自于 Google的大语言模型[Gemini-Pro](https://ai.google.dev/)的能力，如有错误，仅供参考，谨慎使用
>🔴 请注意：千万不要用于严肃的学术场景，只能用于论文阅读前的初筛！
>💗 如果您觉得我们的项目对您有帮助 [ChatPaperFree](https://github.com/Kedreamix/ChatPaperFree) ，还请您给我们一些鼓励！⭐️ [HuggingFace免费体验](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)

# 2024-05-13 更新


## OneTo3D: One Image to Re-editable Dynamic 3D Model and Video Generation

**Authors:Jinwei Lin**

One image to editable dynamic 3D model and video generation is novel direction and change in the research area of single image to 3D representation or 3D reconstruction of image. Gaussian Splatting has demonstrated its advantages in implicit 3D reconstruction, compared with the original Neural Radiance Fields. As the rapid development of technologies and principles, people tried to used the Stable Diffusion models to generate targeted models with text instructions. However, using the normal implicit machine learning methods is hard to gain the precise motions and actions control, further more, it is difficult to generate a long content and semantic continuous 3D video. To address this issue, we propose the OneTo3D, a method and theory to used one single image to generate the editable 3D model and generate the targeted semantic continuous time-unlimited 3D video. We used a normal basic Gaussian Splatting model to generate the 3D model from a single image, which requires less volume of video memory and computer calculation ability. Subsequently, we designed an automatic generation and self-adaptive binding mechanism for the object armature. Combined with the re-editable motions and actions analyzing and controlling algorithm we proposed, we can achieve a better performance than the SOTA projects in the area of building the 3D model precise motions and actions control, and generating a stable semantic continuous time-unlimited 3D video with the input text instructions. Here we will analyze the detailed implementation methods and theories analyses. Relative comparisons and conclusions will be presented. The project code is open source. 

[PDF](http://arxiv.org/abs/2405.06547v1) 24 pages, 13 figures, 2 tables

**Summary**
一个图像到可编辑动态 3D 模型和视频生成是图像到 3D 表示或图像 3D 重建研究领域的新颖方向和变革。

**Key Takeaways**

* 采用高斯溅射法，可实现隐式 3D 重建，并优于原始神经辐射场。
* 借助技术和原理的快速发展，人们尝试使用稳定扩散模型通过文本指令生成目标模型。
* 然而，使用常规隐式机器学习方法难以获得精确的动作和动作控制，且难以生成内容长且语义连续的 3D 视频。
* 研究者提出 OneTo3D 方法，使用单张图像生成可编辑 3D 模型和目标语义连续且时间无限的 3D 视频。
* 研究者采用普通基本高斯溅射模型从单张图像生成 3D 模型，该模型对视频内存和计算机运算能力要求较低。
* 研究者针对对象骨架设计了自动生成和自适应绑定机制。
* 结合研究者提出的可重新编辑的动作和动作分析控制算法，在 3D 模型精确动作和动作控制以及根据输入文本指令生成稳定的语义连续且时间无限的 3D 视频方面取得了优于 SOTA 项目的性能。
* 研究者分析了详细的实现方法和理论分析，并将给出相关的比较和结论。
* 该项目代码开源。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>论文标题：OneTo3D：单幅图像生成可编辑动态 3D 模型和视频</p>
</li>
<li>
<p>作者：JINWEI LIN</p>
</li>
<li>
<p>第一作者单位：莫纳什大学</p>
</li>
<li>
<p>关键词：3D、单幅图像、可编辑、动态、生成、自动化、视频、自适应、骨架</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.06547，Github 链接：无</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>(1)：研究背景：3D 表征或 3D 重建是计算机视觉领域长期以来的挑战。目前实现 3D 重建的方法可分为两类：传统显式方法和机器学习隐式方法。近年来，神经辐射场 (NeRF) 作为一种突出的隐式方法，在渲染和表示真实场景视图方面取得了优异的性能。</p>
<p>(2)：过去方法：基于 NeRF，出现了各种隐式 3D 表征或重建的研究项目。然而，现有的方法在精确运动和动作控制以及生成连续语义 3D 视频方面存在困难。</p>
<p>(3)：本文方法：本文提出 OneTo3D 方法，利用单幅图像生成可编辑 3D 模型和连续语义 3D 视频。该方法使用基本的 Gaussian Splatting 模型从单幅图像生成 3D 模型，并设计了一种自动生成和自适应绑定机制来创建对象骨架。结合可编辑运动和动作分析控制算法，OneTo3D 在 3D 模型精确运动和动作控制以及根据文本指令生成稳定连续的语义 3D 视频方面取得了优于现有技术的性能。</p>
<p>(4)：任务和性能：本文方法在生成可编辑动态 3D 模型和视频的任务上取得了以下性能：
- 实现了精确的运动和动作控制，超越了现有技术。
- 能够根据文本指令生成稳定连续的语义 3D 视频。
- 这些性能支持了本文提出的目标。</p>
<ol>
<li>方法：</li>
</ol>
<p>(1)：生成初始 3D 模型：利用 Gaussian Splatting 模型从输入图像生成初始 3D 模型，不包含动态或可编辑因素。</p>
<p>(2)：生成并绑定自适应骨架：分析初始 3D 模型的几何参数信息，构建适合的骨架，并根据输入图像中的姿态、形状和关键点信息微调骨架参数，使其与物体身体贴合。</p>
<p>(3)：文本到动作：分析用户文本指令的命令意图，提取相对骨骼的特定运动和修改数据，控制特定骨骼在 Blender 中实现相对运动，考虑运动量化、运动次数、运动方向和运动范围等参数。</p>
<p>(4)：可重新编辑运动控制：配合 Blender 界面实现运动可重新编辑控制，将当前姿态作为关键帧插入，结合连续关键帧生成最终 3D 视频，Blender 文件保存为可重新编辑的 3D 编辑文件。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种生成可编辑动态 3D 模型和视频的新方法 OneTo3D。该方法具有以下优点：
- 实现了精确的运动和动作控制，超越了现有技术。
- 能够根据文本指令生成稳定连续的语义 3D 视频。
- 这些性能支持了本文提出的目标。</p>
<p>（2）：创新点：
- 利用单幅图像生成可编辑 3D 模型和视频。
- 设计了一种自动生成和自适应绑定机制来创建对象骨架。
- 结合可编辑运动和动作分析控制算法，实现精确的运动和动作控制。</p>
<p>性能：
- 在生成可编辑动态 3D 模型和视频的任务上取得了优异的性能。
- 超越了现有技术在精确运动和动作控制方面的性能。</p>
<p>工作量：
- 该方法需要大量的训练数据和计算资源。
- 生成可编辑动态 3D 模型和视频的过程需要大量的时间。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-8729865363a1dfddc21dff54a70072f2.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-02dad34b1d632546ae26f127a58c9c0f.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f635130d270abd57752edb234d2c8a48.jpg" align="middle">
</details>




## MGS-SLAM: Monocular Sparse Tracking and Gaussian Mapping with Depth   Smooth Regularization

**Authors:Pengcheng Zhu, Yaoming Zhuang, Baoquan Chen, Li Li, Chengdong Wu, Zhanlin Liu**

This letter introduces a novel framework for dense Visual Simultaneous Localization and Mapping (VSLAM) based on Gaussian Splatting. Recently Gaussian Splatting-based SLAM has yielded promising results, but rely on RGB-D input and is weak in tracking. To address these limitations, we uniquely integrates advanced sparse visual odometry with a dense Gaussian Splatting scene representation for the first time, thereby eliminating the dependency on depth maps typical of Gaussian Splatting-based SLAM systems and enhancing tracking robustness. Here, the sparse visual odometry tracks camera poses in RGB stream, while Gaussian Splatting handles map reconstruction. These components are interconnected through a Multi-View Stereo (MVS) depth estimation network. And we propose a depth smooth loss to reduce the negative effect of estimated depth maps. Furthermore, the consistency in scale between the sparse visual odometry and the dense Gaussian map is preserved by Sparse-Dense Adjustment Ring (SDAR). We have evaluated our system across various synthetic and real-world datasets. The accuracy of our pose estimation surpasses existing methods and achieves state-of-the-art performance. Additionally, it outperforms previous monocular methods in terms of novel view synthesis fidelity, matching the results of neural SLAM systems that utilize RGB-D input. 

[PDF](http://arxiv.org/abs/2405.06241v1) This work has been submitted to the IEEE for possible publication.   Copyright may be transferred without notice, after which this version may no   longer be accessible

**Summary**
基于高斯分布的稠密视觉SLAM新框架，集成了稀疏视觉里程计和稠密场景表示，增强了鲁棒性和准确性。

**Key Takeaways**
* 结合了稀疏视觉里程计和高斯分布的稠密场景表示。
* 消除了对深度图的依赖，增强了跟踪的鲁棒性。
* 多视图立体（MVS）深度估计网络连接了稀疏视觉里程计和高斯分布。
* 提出深度平滑损失，减少估计深度图的负面影响。
* 通过稀疏-稠密调整环（SDAR）保持了稀疏视觉里程计和高斯分布的地图之间的规模一致性。
* 在合成数据集和真实世界数据集上评估，姿势估计的准确性超过了现有方法，达到最先进的水平。
* 在新视图合成保真度方面优于之前的单目方法，达到利用RGB-D输入的神经SLAM系统的效果。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>Title: MGS-SLAM: 单目稀疏跟踪和高斯映射与深度平滑正则化</li>
<li>Authors: Pengcheng Zhu, Yaoming Zhuang, Baoquan Chen, Li Li, Chengdong Wu, Zhanlin Liu</li>
<li>Affiliation: 东北大学机器人科学与工程学院</li>
<li>Keywords: Visual SLAM, Gaussian Splatting, Sparse Visual Odometry, Multi-View Stereo, Depth Smooth Regularization</li>
<li>Urls: Paper: https://arxiv.org/abs/2405.06241, Github: None</li>
<li>Summary:</li>
</ol>
<p>(1):该文章的研究背景是：随着深度学习的快速发展，一种利用可微渲染的新型 SLAM 技术应运而生。基于可微渲染的 SLAM 技术最初使用神经辐射场 (NeRF) 作为其基础构建方法。NeRF 利用神经网络表示 3D 场景，能够合成高质量图像并从多视图中恢复密集的几何结构。基于 NeRF 的 SLAM 系统在制图过程中保留了详细的场景信息，增强了对后续导航和路径规划的支持。然而，NeRF 的方法在图像渲染过程中需要对每个像素进行多次前向预测，导致大量的计算冗余。因此，这种低效性阻碍了基于 NeRF 的 SLAM 实时运行，从而限制了其在直接下游任务中的实用性。</p>
<p>(2):过去的方法是基于高斯散射的 SLAM 系统依赖于 RGB-D 相机的深度图输入，这限制了它们的应用范围。问题是跟踪能力弱。该方法的动机很好，它将基于高斯散射的技术与稀疏视觉里程计相结合，消除了对基于高斯散射的 SLAM 系统中典型的深度图的依赖性，并增强了跟踪鲁棒性。</p>
<p>(3):本文提出的研究方法是：提出了一种新颖的单目高斯散射 SLAM 系统 MGS-SLAM。该工作在 SLAM 领域引入了多项突破性进展，包括将基于高斯散射的技术与稀疏视觉里程计相结合，采用预训练的多视图立体 (MVS) 深度估计网络，开创了一种几何平滑深度损失，并开发了稀疏 -密集调整环 (SDAR) 以确保尺度一致性。这些创新共同显着提高了仅依赖 RGB 图像输入的 SLAM 系统的准确性和功能性。</p>
<p>(4):本文的方法在以下任务和性能上取得了成就：在各种合成和真实世界数据集上对我们的系统进行了评估。我们的位姿估计的准确度超过了现有方法，并取得了最先进的性能。此外，它在新的视图合成保真度方面优于之前的单目方法，与利用 RGB-D 输入的神经 SLAM 系统的结果相匹配。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出了一种新颖的单目高斯散射 SLAM 系统 MGS-SLAM，将基于高斯散射的技术与稀疏视觉里程计相结合，消除了对基于高斯散射的 SLAM 系统中典型的深度图的依赖性，并增强了跟踪鲁棒性；</p>
<p>（2）：采用预训练的多视图立体（MVS）深度估计网络，为后端密集映射提供几何深度监督；</p>
<p>（3）：开创了一种几何平滑深度损失，以减轻先验深度图误差对高斯地图几何重建的影响；</p>
<p>（4）：开发了稀疏-密集调整环（SDAR），以确保稀疏点云地图和密集高斯地图之间的尺度一致性。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：该工作提出了一种新颖的单目高斯散射 SLAM 系统 MGS-SLAM，该系统将基于高斯散射的技术与稀疏视觉里程计相结合，消除了对基于高斯散射的 SLAM 系统中典型的深度图的依赖性，并增强了跟踪鲁棒性。此外，该工作还采用预训练的多视图立体（MVS）深度估计网络，开创了一种几何平滑深度损失，并开发了稀疏-密集调整环（SDAR），以确保稀疏点云地图和密集高斯地图之间的尺度一致性。这些创新共同显着提高了仅依赖 RGB 图像输入的 SLAM 系统的准确性和功能性。</p>
<p>（2）：创新点：将基于高斯散射的技术与稀疏视觉里程计相结合，消除了对深度图的依赖性，并增强了跟踪鲁棒性；采用预训练的多视图立体（MVS）深度估计网络，为后端密集映射提供几何深度监督；开创了一种几何平滑深度损失，以减轻先验深度图误差对高斯地图几何重建的影响；开发了稀疏-密集调整环（SDAR），以确保稀疏点云地图和密集高斯地图之间的尺度一致性。</p>
<p>性能：在各种合成和真实世界数据集上对我们的系统进行了评估。我们的位姿估计的准确度超过了现有方法，并取得了最先进的性能。此外，它在新的视图合成保真度方面优于之前的单目方法，与利用 RGB-D 输入的神经 SLAM 系统的结果相匹配。</p>
<p>工作量：该方法需要预训练的多视图立体（MVS）深度估计网络，并且需要开发稀疏-密集调整环（SDAR）来确保稀疏点云地图和密集高斯地图之间的尺度一致性。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-9c81783ec5cc64db3f3888e91459cd94.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-5722638fadf13564cb13427fd8d4410c.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-ea1359ff05ba09f3fd64460b9bd9878a.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-940291f15a48e90bf4dec39f8ee7ddd2.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-d5bc3a1c2278602383a64b530b3dd889.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-e517184c75aa28276e746751c5d28917.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-e89f79eb15cc3b181f2efde56510f1d8.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-5713c30b73286985fa8f2ff3f7ac2e21.jpg" align="middle">
</details>




## FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic   Gaussian Splatting

**Authors:Yikun Ma, Dandan Zhan, Zhi Jin**

Text-driven 3D indoor scene generation holds broad applications, ranging from gaming and smart homes to AR/VR applications. Fast and high-fidelity scene generation is paramount for ensuring user-friendly experiences. However, existing methods are characterized by lengthy generation processes or necessitate the intricate manual specification of motion parameters, which introduces inconvenience for users. Furthermore, these methods often rely on narrow-field viewpoint iterative generations, compromising global consistency and overall scene quality. To address these issues, we propose FastScene, a framework for fast and higher-quality 3D scene generation, while maintaining the scene consistency. Specifically, given a text prompt, we generate a panorama and estimate its depth, since the panorama encompasses information about the entire scene and exhibits explicit geometric constraints. To obtain high-quality novel views, we introduce the Coarse View Synthesis (CVS) and Progressive Novel View Inpainting (PNVI) strategies, ensuring both scene consistency and view quality. Subsequently, we utilize Multi-View Projection (MVP) to form perspective views, and apply 3D Gaussian Splatting (3DGS) for scene reconstruction. Comprehensive experiments demonstrate FastScene surpasses other methods in both generation speed and quality with better scene consistency. Notably, guided only by a text prompt, FastScene can generate a 3D scene within a mere 15 minutes, which is at least one hour faster than state-of-the-art methods, making it a paradigm for user-friendly scene generation. 

[PDF](http://arxiv.org/abs/2405.05768v1) Accepted by IJCAI-2024

**摘要**
文本驱动的3D室内场景生成在游戏、智能家居和AR/VR应用中有着广泛的应用，快速且高保真场景生成对确保用户友好体验至关重要。

**要点**
- 3D室内场景生成有着广泛的应用。
- 现有的方法生成过程耗时或需要用户手动指定运动参数，给用户带来不便。
- 现有的方法专注于窄视域观点迭代生成，影响全局一致性和整体场景质量。
- FastScene框架可在保持场景一致性的情况下快速生成更高质量的3D场景。
- 根据文本提示生成全景图并估计其深度，因为全景图包含整个场景信息并展示明确的几何约束。
- 引入粗视图合成（CVS）和渐进式新视图修复（PNVI）策略来获得高质量的新视角，确保场景一致性和视图质量。
- 使用多视图投影（MVP）形成透视视图，并应用3D高斯散射（3DGS）进行场景重建。
- 全面实验表明，FastScene在生成速度和质量上都超过了其他方法，并具有更好的场景一致性。
- FastScene仅通过文本提示就可以在短短15分钟内生成3D场景，比最先进的方法快至少1小时，使其成为用户友好场景生成范例。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：FastScene：文本驱动的快速 3D 室内场景生成</p>
</li>
<li>
<p>作者：Yikun Ma，Dandan Zhan，Zhi Jin</p>
</li>
<li>
<p>单位：中山大学</p>
</li>
<li>
<p>关键词：文本驱动的 3D 场景生成，全景图，高斯体素渲染</p>
</li>
<li>
<p>论文链接：Paper_info，Github 链接：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：文本驱动的 3D 室内场景生成在游戏、智能家居、AR/VR 等领域有着广泛的应用。快速、高保真的场景生成对于确保用户友好的体验至关重要。然而，现有方法的特点是生成过程冗长或需要复杂的手动指定运动参数，给用户带来不便。此外，这些方法通常依赖于窄视场视点迭代生成，影响了全局一致性和整体场景质量。</p>
<p>（2）：过去的方法及问题：Set-the-Scene 从文本提示和 3D 对象代理进行全局局部训练，生成可控场景。但由于缺乏相应的几何信息，生成场景的质量和分辨率不佳。SceneScape 生成长距离视图，生成风格多样。但由于内绘和深度估计误差的积累，其视图质量会随着时间的推移而降低。Text2Room 和 Text2NeRF 逐步生成透视新视图。但其增量局部操作难以保证场景一致性和连贯性。Ctrl-Room 对 ControlNet 进行微调以生成可编辑的全景图，然后执行网格重建。但由于 Ctrl-Room 难以生成多视图图像，因此它倾向于将 3D 模型扁平化，场景质量有限。</p>
<p>（3）：提出的研究方法：本文提出了一种新颖的文本到 3D 场景框架，称为 FastScene，旨在快速生成一致、真实且高质量的场景。如图 1 所示，我们的方法主要包括三个阶段。1）在第一阶段，给定一个文本提示，我们利用预训练的 Diffusion360 生成全景图。选择全景图是因为它能够捕获全局信息并表现出明确的几何约束。2）在第二阶段，我们利用全景图及其深度估计来生成粗略视图。然后，我们引入粗略视图合成 (CVS) 和渐进式新视图内绘 (PNVI) 策略来细化粗略视图，同时确保场景一致性和视图质量。3）在第三阶段，我们利用多视图投影 (MVP) 形成透视视图，并应用 3D 高斯体素渲染 (3DGS) 进行场景重建。</p>
<p>（4）：方法在什么任务上取得了什么性能：综合实验表明，FastScene 在生成速度和质量方面都优于其他方法，并且场景一致性更好。值得注意的是，FastScene 仅在文本提示的指导下，可以在短短 15 分钟内生成一个 3D 场景，这比最先进的方法至少快一个小时，使其成为用户友好场景生成的一个典范。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：Diffusion360生成全景图，EGformer估计深度图；</p>
<p>（2）：CVS生成带有孔洞的新全景图，PNVI逐步修复孔洞；</p>
<p>（3）：MVP生成透视视图，3DGS进行场景重建。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种快速文本到 3D 室内场景生成框架 FastScene，展示了令人满意的场景质量和一致性。对于用户而言，FastScene 只需要一个文本提示，无需设计运动参数，即可在短短 15 分钟内提供一个完整的高质量 3D 场景。提出的 PNVI 与 CVS 可以生成一致的新全景视图，而 MVP 将其投影到透视视图，促进了 3DGS 重建。大量的实验证明了我们方法的有效性。FastScene 提供了一个用户友好的场景生成范例，我们相信它具有广泛的潜在应用。在未来的工作中，我们将重点关注 3D 场景编辑和多模态学习。致谢 本工作得到了国家自然科学基金（No.62071500）和深圳市科技计划（Grant No. JCYJ20230807111107015）的支持。</p>
<p>（2）：创新点：提出了一种基于全景图的快速文本到 3D 室内场景生成框架 FastScene；性能：FastScene 在生成速度和质量方面均优于其他方法，并且场景一致性更好；工作量：FastScene 仅在文本提示的指导下，可以在短短 15 分钟内生成一个 3D 场景，这比最先进的方法至少快一个小时。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-9ae84b1fe141ce2458a3514ff61edab5.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-9516335b56aaf68e720f85429fe6d949.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-fcf104105c3e3c0c631f51aa64860b19.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-6035d44b6617ded58ccc09ecb36f41eb.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-2f44233f42fcbaf0d92844c77c24e8b3.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-a657f39b3ff13b487d3da4b747083bfc.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-30b15f3bf60cdbeb4ed8595da183fcab.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-66a918dd33cc4c399a7322eb37b47e0d.jpg" align="middle">
</details>




## Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review

**Authors:Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård**

Image-based 3D reconstruction is a challenging task that involves inferring the 3D shape of an object or scene from a set of input images. Learning-based methods have gained attention for their ability to directly estimate 3D shapes. This review paper focuses on state-of-the-art techniques for 3D reconstruction, including the generation of novel, unseen views. An overview of recent developments in the Gaussian Splatting method is provided, covering input types, model structures, output representations, and training strategies. Unresolved challenges and future directions are also discussed. Given the rapid progress in this domain and the numerous opportunities for enhancing 3D reconstruction methods, a comprehensive examination of algorithms appears essential. Consequently, this study offers a thorough overview of the latest advancements in Gaussian Splatting. 

[PDF](http://arxiv.org/abs/2405.03417v1) 24 pages

**Summary**
基于图像的3D重建是一项颇具挑战的任务，涉及从一组输入图像中推断物体的3D形状。基于学习的方法因其直接估计3D形状的能力而备受关注。本文重点介绍3D重建的最先进技术，包括生成新颖的、未曾见过的视图。概述了高斯散布方法的最新发展，涵盖输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的发展方向。鉴于该领域的快速发展以及提高3D重建方法的众多机会，对算法进行全面检查至关重要。因此，本研究对高斯散布的最新进展进行了全面概述。

**Key Takeaways**
- 图像-基于3D重建包括从一组输入图像推断对象的3D形状。
- 学习-基于方法因其直接估计3D形状的能力备受关注。
- 高斯散布是一个用于3D重建的最先进技术。
- 高斯散布输入类型包括单目和多目图像。
- 高斯散布模型结构包括编码器-解码器和Transformer。
- 高斯散布输出表示包括体素网格和点云。
- 高斯散布训练策略包括监督学习和自监督学习。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review</p>
</li>
<li>
<p>Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård</p>
</li>
<li>
<p>Affiliation: Department of Engineering Sciences, University of Agder, Grimstad, Norway</p>
</li>
<li>
<p>Keywords: 3D Reconstruction, Computer Vision, Deep Learning, Gaussian Splatting, Novel view synthesis, Optimization, Rendering</p>
</li>
<li>
<p>Urls: Paper_info:Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.
Digital Object Identifier xxxx</p>
</li>
<li>
<p>Summary:</p>
<pre><code>           (1):Image-based 3D reconstruction is a challenging task that involves inferring the 3D shape of an object or scene from a set of input images. Learning-based methods have gained attention for their ability to directly estimate 3D shapes. This review paper focuses on state-of-the-art techniques for 3D reconstruction, including the generation of novel, unseen views. An overview of recent developments in the Gaussian Splatting method is provided, covering input types, model structures, output representations, and training strategies. Unresolved challenges and future directions are also discussed. Given the rapid progress in this domain and the numerous opportunities for enhancing 3D reconstruction methods, a comprehensive examination of algorithms appears essential. Consequently, this study offers a thorough overview of the latest advancements in Gaussian Splatting.;

           (2):Traditional approaches to 3D reconstruction, such as photogrammetry and multi-view stereo (MVS) algorithms, often suffer from artifacts, failure cases, and slow training times. Gaussian Splatting is a novel method that addresses these limitations by representing 3D objects as a collection of Gaussians. This representation allows for efficient rendering and interpolation, resulting in high-quality novel views.;

           (3):The Gaussian Splatting method involves an iterative refinement process, where multiple Gaussians are optimized to match the input images. The model is trained using a combination of supervised and unsupervised losses, which encourage consistency with the input images and smoothness in the 3D space. The output of the model is a volumetric point cloud, where each point represents a Gaussian with parameters such as color, spread, and location.;

           (4):Gaussian Splatting has been shown to achieve state-of-the-art results on a variety of 3D reconstruction and novel view synthesis tasks. The method outperforms previous approaches in terms of rendering quality, training time, and robustness to challenging scenes. These results demonstrate the potential of Gaussian Splatting for a wide range of applications, including virtual reality, augmented reality, and computer-aided design.
</code></pre>
</li>
<li>
<p>方法：</p>
<pre><code>           (1):本文首先介绍了高斯散点法，这是一种使用高斯函数集合表示 3D 物体的创新方法。这种表示形式允许高效渲染和插值，从而产生高质量的新颖视图；

           (2):高斯散点法涉及一个迭代细化过程，其中优化多个高斯函数以匹配输入图像。模型使用监督和无监督损失的组合进行训练，这鼓励与输入图像的一致性和 3D 空间中的平滑度。模型的输出是体积点云，其中每个点表示一个具有颜色、扩展和位置等参数的高斯函数；

           (3):高斯散点法已被证明在各种 3D 重建和新颖视图合成任务上实现了最先进的结果。该方法在渲染质量、训练时间和对具有挑战性场景的鲁棒性方面优于以前的方法。这些结果证明了高斯散点法在广泛的应用中的潜力，包括虚拟现实、增强现实和计算机辅助设计。
</code></pre>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）：本文从功能和应用角度对高斯散点法在三维重建和新颖视图合成中的应用进行了全面的综述，涵盖了动态建模、变形建模、运动跟踪、非刚性/可变形物体、表情/情绪变化、基于文本的生成扩散、降噪、优化、虚拟形象、可动画对象、头部建模、同步定位与规划、网格提取与物理、优化技术、编辑能力、渲染方法、压缩等方面。特别是，本文深入探讨了图像三维重建中的挑战和进展，学习型方法在三维形状估计中的作用，以及高斯散点法在三维重建中的优势和局限性。</p>
<p>（2）：创新点：高斯散点法是一种使用高斯函数集合表示三维物体的创新方法，这种表示形式允许高效渲染和插值，从而产生高质量的新颖视图；性能：高斯散点法在三维重建和新颖视图合成方面取得了最先进的结果，在渲染质量、训练时间和对具有挑战性场景的鲁棒性方面优于以前的方法；工作量：高斯散点法涉及一个迭代细化过程，其中优化多个高斯函数以匹配输入图像，训练过程需要较大的计算资源。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-48d38462ddefdcfe75129220282e7a18.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-712a52026b682e9ab729dccf592cc5f7.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-14985716143782f83102a5633ec37c23.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-b3dd2127ce2dbe6cdafc1b40d9cc2fb2.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-2f865d904180e8ed6511d41dac5f81c0.jpg" align="middle">
</details>




## RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting

**Authors:Zhexi Peng, Tianjia Shao, Yong Liu, Jingke Zhou, Yin Yang, Jingdong Wang, Kun Zhou**

We present Real-time Gaussian SLAM (RTG-SLAM), a real-time 3D reconstruction system with an RGBD camera for large-scale environments using Gaussian splatting. The system features a compact Gaussian representation and a highly efficient on-the-fly Gaussian optimization scheme. We force each Gaussian to be either opaque or nearly transparent, with the opaque ones fitting the surface and dominant colors, and transparent ones fitting residual colors. By rendering depth in a different way from color rendering, we let a single opaque Gaussian well fit a local surface region without the need of multiple overlapping Gaussians, hence largely reducing the memory and computation cost. For on-the-fly Gaussian optimization, we explicitly add Gaussians for three types of pixels per frame: newly observed, with large color errors, and with large depth errors. We also categorize all Gaussians into stable and unstable ones, where the stable Gaussians are expected to well fit previously observed RGBD images and otherwise unstable. We only optimize the unstable Gaussians and only render the pixels occupied by unstable Gaussians. In this way, both the number of Gaussians to be optimized and pixels to be rendered are largely reduced, and the optimization can be done in real time. We show real-time reconstructions of a variety of large scenes. Compared with the state-of-the-art NeRF-based RGBD SLAM, our system achieves comparable high-quality reconstruction but with around twice the speed and half the memory cost, and shows superior performance in the realism of novel view synthesis and camera tracking accuracy. 

[PDF](http://arxiv.org/abs/2404.19706v3) To be published in ACM SIGGRAPH 2024

**Summary**
实时高斯 SLAM 系统使用高斯点云表示方式实现了大规模 RGBD 图像序列的重建，并采用高效的高斯优化方法实时生成连续的三维重建结果。

**Key Takeaways**
- 使用高斯点云表示环境，紧凑高效。
- 将高斯点云分为不透明和半透明两种，不透明点云拟合表面和主要颜色，半透明点云拟合残差颜色。
- 通过深度渲染和颜色渲染分离，单个不透明高斯点云就能拟合局部表面区域，减少了高斯点云数量、存储空间和计算成本。
- 实时高斯优化，针对新观测到的像素、颜色误差大的像素和深度误差大的像素添加高斯点云。
- 将高斯点云分为稳定和不稳定两种，仅优化不稳定的高斯点云，仅渲染不稳定高斯点云覆盖的像素。
- 与基于 NeRF 的 RGBD SLAM 系统相比，该系统重建质量相当，但速度提高约一倍，内存成本减半，并且在新的视图合成真实感和相机跟踪准确性方面表现更出色。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: RTG-SLAM：使用高斯渲染的大规模实时三维重建</p>
</li>
<li>
<p>Authors: Zhexi Peng, Tianjia Shao, Yong Liu, Jingke Zhou, Yin Yang, Jingdong Wang, Kun Zhou</p>
</li>
<li>
<p>Affiliation: 浙江大学计算机辅助设计与图形学国家重点实验室</p>
</li>
<li>
<p>Keywords: RGBD SLAM, 3D reconstruction, Gaussian splatting</p>
</li>
<li>
<p>Urls: Paper: https://arxiv.org/abs/2404.19706, Github: None</p>
</li>
<li>
<p>Summary:</p>
</li>
</ol>
<p>(1): 该文章的研究背景是随着 RGBD 相机的发展，实时三维重建技术得到了广泛应用。然而，现有的方法在处理大规模环境时，往往面临内存消耗大、计算成本高的问题。</p>
<p>(2): 过去的方法主要使用神经辐射场（NeRF）来表示三维场景，但 NeRF 需要大量的高斯体素来拟合表面，导致内存消耗大。</p>
<p>(3): 该文章提出了一种基于高斯渲染的实时三维重建系统 RTG-SLAM。RTG-SLAM 使用高斯体素来表示三维场景，并通过强制每个高斯体素要么不透明要么近乎透明，来减少内存消耗。此外，RTG-SLAM 采用了一种高效的在线高斯优化方案，只优化不稳定的高斯体素，进一步降低了计算成本。</p>
<p>(4): 在大规模环境重建任务上，RTG-SLAM 实现了与 NeRF-SLAM 相当的重建质量，但速度提高了约两倍，内存消耗减少了一半。</p>
<ol>
<li>
<p>方法：</p>
<pre><code>           (1): 该方法使用高斯体素表示三维场景，并通过强制每个高斯体素要么不透明要么近乎透明，来减少内存消耗。

           (2): 该方法采用了一种高效的在线高斯优化方案，只优化不稳定的高斯体素，进一步降低了计算成本。

           (3): 该方法在大规模环境重建任务上，实现了与 NeRF-SLAM 相当的重建质量，但速度提高了约两倍，内存消耗减少了一半。
</code></pre>
</li>
<li>
<p>结论：</p>
<pre><code>           （1）：本文提出了一种基于高斯渲染的大规模实时三维重建系统 RTG-SLAM，该系统通过使用高斯体素表示三维场景，并强制每个高斯体素要么不透明要么近乎透明，来减少内存消耗，并采用了一种高效的在线高斯优化方案，只优化不稳定的高斯体素，进一步降低了计算成本，在保证重建质量的情况下，提高了重建速度，降低了内存消耗。

           （2）：创新点：提出了一种基于高斯渲染的大规模实时三维重建系统，该系统通过使用高斯体素表示三维场景，并强制每个高斯体素要么不透明要么近乎透明，来减少内存消耗，并采用了一种高效的在线高斯优化方案，只优化不稳定的高斯体素，进一步降低了计算成本。

           性能：在保证重建质量的情况下，提高了重建速度，降低了内存消耗。

           工作量：需要对不稳定的高斯体素进行优化，需要渲染不稳定的高斯体素占据的像素。
</code></pre>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-0eaefb973e265febe848896437a17659.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-9a058fc44423666e88d6baa1e211422b.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-3e7c959078c5d5d3548984d92ce2a3ec.jpg" align="middle">
</details>




