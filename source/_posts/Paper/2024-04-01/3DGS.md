
---
title: 3DGS
date: 2024-04-01 11:33:57
author: Kedreamix
cover: https://pic1.zhimg.com/v2-1d255548bb663bfdfcb547c6dee7c3f0.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-04-01  Snap-it, Tap-it, Splat-it Tactile-Informed 3D Gaussian Splatting for   Reconstructing Challenging Surfaces  
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

# 2024-04-01 更新


## Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for   Reconstructing Challenging Surfaces

**Authors:Mauro Comi, Alessio Tonioni, Max Yang, Jonathan Tremblay, Valts Blukis, Yijiong Lin, Nathan F. Lepora, Laurence Aitchison**

Touch and vision go hand in hand, mutually enhancing our ability to understand the world. From a research perspective, the problem of mixing touch and vision is underexplored and presents interesting challenges. To this end, we propose Tactile-Informed 3DGS, a novel approach that incorporates touch data (local depth maps) with multi-view vision data to achieve surface reconstruction and novel view synthesis. Our method optimises 3D Gaussian primitives to accurately model the object's geometry at points of contact. By creating a framework that decreases the transmittance at touch locations, we achieve a refined surface reconstruction, ensuring a uniformly smooth depth map. Touch is particularly useful when considering non-Lambertian objects (e.g. shiny or reflective surfaces) since contemporary methods tend to fail to reconstruct with fidelity specular highlights. By combining vision and tactile sensing, we achieve more accurate geometry reconstructions with fewer images than prior methods. We conduct evaluation on objects with glossy and reflective surfaces and demonstrate the effectiveness of our approach, offering significant improvements in reconstruction quality. 

[PDF](http://arxiv.org/abs/2403.20275v1) 17 pages

**Summary**
多模态方法将触觉信息与多视角视觉数据相结合，以实现表面重建和新视角合成。

**Key Takeaways**
- 触觉和视觉相互补充，共同提升我们对世界的理解。
- 触觉信息（局部深度图）与多视角视觉数据相结合，实现了表面重建和新视角合成。
- 3D 高斯原语优化，精确建模接触点的物体几何。
- 触觉位置的透射率降低，提升表面重建精度，保证深度图均匀平滑。
- 触觉对非朗伯物体（如光泽或反光表面）尤为有用，因为传统方法难以真实重建镜面高光。
- 结合视觉和触觉传感，可使用比以前的方法更少的图像实现更准确的几何重建。
- 在光泽和反光表面的物体上进行评估，证明了我们方法的有效性，在重建质量上取得了显著改善。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：触觉信息 3D 高斯溅射：用于重建具有挑战性的表面的触觉信息 3D 高斯溅射</li>
<li>作者：Mauro Comi、Alessio Tonioni、Max Yang、Jonathan Tremblay、Valts Blukis、Yijiong Lin、Nathan F. Lepora、Laurence Aitchison</li>
<li>第一作者单位：布里斯托大学</li>
<li>关键词：3D 重建、触觉传感、高斯溅射、新视角合成</li>
<li>论文链接：https://arxiv.org/abs/2403.20275</li>
<li>摘要：
(1) 研究背景：触觉和视觉相互作用，共同增强我们理解世界的能力。从研究的角度来看，将触觉和视觉结合起来是一个尚未充分探索的问题，并提出了有趣的挑战。
(2) 过去方法及其问题：本文提出了一种新颖的方法 Tactile-Informed 3DGS，该方法将触觉数据（局部深度图）与多视角视觉数据相结合，以实现曲面重建和新视角合成。现有方法在重建具有镜面高光的非朗伯物体时往往无法忠实地重建，而触觉在这种情况下特别有用。
(3) 本文方法：本文方法优化 3D 高斯基元，以准确建模接触点处的物体几何形状。通过创建一个在触觉位置降低透射率的框架，本文方法实现了精细的表面重建，确保了均匀平滑的深度图。
(4) 方法性能：本文方法在具有光泽和反光表面的物体上进行评估，证明了其有效性，在重建质量方面提供了显着的改进。</li>
</ol>
<p>7.方法：
（1）：从局部深度图中生成初始点云，并使用高斯基元优化和正则化来精确建模物体表面；
（2）：通过提取 COLMAP 中的点云并初始化高斯基元的均值和颜色属性，生成初始高斯基元集合；
（3）：使用光学触觉传感器收集的点集初始化另一组高斯基元，并使用 3D 透射率损失对高斯基元进行正则化；
（4）：利用边缘感知平滑损失和距离过滤准则，进一步优化高斯基元，并通过最小化预测图像和真实 RGB 图像之间的光度损失来优化高斯基元；
（5）：通过限制考虑每个点的具有最高空间影响的高斯基元数量，并排除超出一定阈值距离的高斯基元，来管理计算负载并优先优化触觉位置周围的高斯基元；
（6）：使用距离衰减函数或离散阈值掩码将边缘感知平滑损失与基于接近的掩码相结合，以减少远离触觉点的 Gaussians 的影响。</p>
<ol>
<li>结论：
（1）：本文的工作意义在于首次探索了同时看到和触摸的物体的重建和新视角合成问题，并提出了触觉信息 3D 高斯溅射（Tactile-Informed 3D GS）方法，该方法将触觉数据与多视角视觉数据相结合，在具有镜面高光的非朗伯物体重建方面取得了显着的改进。
（2）：创新点：
本文方法将触觉数据与多视角视觉数据相结合，提出了一种新颖的物体重建方法，该方法在具有镜面高光的非朗伯物体重建方面表现出了优异的性能。
性能：
本文方法在具有光泽和反光表面的物体上进行评估，证明了其有效性，在重建质量方面提供了显着的改进。
工作量：
本文方法通过限制考虑每个点的具有最高空间影响的高斯基元数量，并排除超出一定阈值距离的高斯基元，来管理计算负载并优先优化触觉位置周围的高斯基元，从而降低了计算工作量。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-8c866c0054577dbf0ede9d1aca4b7f2f.jpg" align="middle">
</details>




## HGS-Mapping: Online Dense Mapping Using Hybrid Gaussian Representation   in Urban Scenes

**Authors:Ke Wu, Kaizhao Zhang, Zhiwei Zhang, Shanshuai Yuan, Muer Tie, Julong Wei, Zijun Xu, Jieru Zhao, Zhongxue Gan, Wenchao Ding**

Online dense mapping of urban scenes forms a fundamental cornerstone for scene understanding and navigation of autonomous vehicles. Recent advancements in mapping methods are mainly based on NeRF, whose rendering speed is too slow to meet online requirements. 3D Gaussian Splatting (3DGS), with its rendering speed hundreds of times faster than NeRF, holds greater potential in online dense mapping. However, integrating 3DGS into a street-view dense mapping framework still faces two challenges, including incomplete reconstruction due to the absence of geometric information beyond the LiDAR coverage area and extensive computation for reconstruction in large urban scenes. To this end, we propose HGS-Mapping, an online dense mapping framework in unbounded large-scale scenes. To attain complete construction, our framework introduces Hybrid Gaussian Representation, which models different parts of the entire scene using Gaussians with distinct properties. Furthermore, we employ a hybrid Gaussian initialization mechanism and an adaptive update method to achieve high-fidelity and rapid reconstruction. To the best of our knowledge, we are the first to integrate Gaussian representation into online dense mapping of urban scenes. Our approach achieves SOTA reconstruction accuracy while only employing 66% number of Gaussians, leading to 20% faster reconstruction speed. 

[PDF](http://arxiv.org/abs/2403.20159v1) 

**Summary**
3DGS大规模场景在线稠密映射框架HGS-Mapping首次集成高斯表示，实现完整重建，重构精度优于SOTA，速度提升20%。

**Key Takeaways**
- 3DGS在线大规模场景稠密映射面临不完整重建和高计算量挑战。
- HGS-Mapping引入了混合高斯表示，针对不同场景部分建模不同性质的高斯。
- 使用混合高斯初始化机制和自适应更新方法，实现高保真、快速重建。
- 首次将高斯表示集成到城市场景在线稠密映射中。
- 重建精度超越SOTA，高斯数量减少66%，重建速度提升20%。
- 能有效处理激光雷达覆盖区域外的几何信息缺失问题。
- 适用于大规模城市场景在线稠密重建任务。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：HGS-Mapping：城市场景中的在线稠密重建使用混合高斯表示</li>
<li>作者：Ke Wu、Kaizhao Zhang、Zhiwei Zhang、Shanshuai Yuan、Muer Tie、Julong Wei、Zijun Xu、Jieru Zhao、Zhongxue Gan、Wenchao Ding</li>
<li>第一作者单位：复旦大学</li>
<li>关键词：高斯溅射、稠密重建、自动驾驶</li>
<li>论文链接：https://arxiv.org/abs/2403.20159</li>
<li>摘要：
（1）研究背景：在线稠密重建是自动驾驶车辆理解复杂环境和有效导航的基础，需要持续创建车辆周围环境的详细地图，以实现对几乎所有可见表面和物体的全面和高保真表示。
（2）过去方法及其问题：传统方法直接融合时空传感器数据构建地图，但此类地图稀疏，无法捕捉丰富的场景细节；基于NeRF的最新方法渲染速度太慢，无法满足在线要求；3D高斯溅射（3DGS）渲染速度比NeRF快数百倍，在在线稠密重建中具有更大潜力，但集成到街景稠密重建框架中仍面临两大挑战：一是由于LiDAR覆盖区域之外缺乏几何信息导致重建不完整；二是大型城市场景中重建计算量大。
（3）本文方法：提出HGS-Mapping，一种在大规模场景中的在线稠密重建框架。为了实现重建完整性，引入混合高斯表示，使用具有不同属性的高斯模型化整个场景的不同部分。此外，采用混合高斯初始化机制和自适应更新方法，以实现高保真和快速重建。
（4）方法性能：在保证重建精度的同时，仅使用66%的高斯数量，重建速度提高20%，达到最先进的重建精度。</li>
</ol>
<p>7.方法：
（1）高斯初始化：利用激光雷达点初始化高斯模型，并通过轻量级特征匹配网络提取相邻 RGB 帧中的匹配像素，计算光流值，确定匹配像素的空间位置。对于光流值小于阈值的像素，通过近似计算方法估计远距离特征点的深度。
（2）球面高斯：将天空建模为附加在半径为 R 的巨大球面 S 表面上的高斯模型，即球面高斯 Gsky。Gsky 仅具有两个平移自由度和一个旋转自由度，并具有固定的径向厚度。
（3）2D 高斯平面：将道路表面建模为平面上的扁平高斯模型，即 2D 高斯平面 Ginlier。Ginlier 仅具有两个平移自由度和一个旋转自由度，并具有固定的厚度。
（4）3D 高斯：利用椭球形高斯模型 Goutlier 来表示路边景观。Goutlier 具有 14 个可学习属性，包括位置、尺度、颜色和不透明度。
（5）混合 RGBD 光栅化器：设计了专门针对混合高斯表示的混合 RGBD 光栅化器。通过计算每个像素在 3D 空间中的权重，独立评估每个图块中的三种类型的高斯模型。然后，分别对 Gsky 和 Goutlier 进行排序，并将其连接在一起。最后，通过直接计算与该像素重叠的 N 个排序高斯模型的加权和来渲染一个像素的 RGB 值和深度值。
（6）优化关键帧列表：为了防止在线映射过程中历史帧的重建质量下降，维护了一个全局关键帧列表。每次迭代，从关键帧列表中随机选择一个帧进行优化。关键帧列表包含 K 帧，其中 K-2 帧从所有与当前帧重叠的帧中随机选择，并将当前帧和前一帧添加到列表中。每 n 帧更新一次关键帧列表。
（7）损失函数：损失函数包括光度损失、几何损失和正则化损失。光度损失由 L1 和 D-SSIM 项组成。激光雷达损失是稀疏深度（激光雷达）和预测深度之间的 L1 损失。正则化损失旨在提高渲染深度的质量，包括深度平滑损失和各向异性损失。</p>
<p><strong>8. 结论</strong></p>
<p>(1) 意义：本文提出了 HGS-Mapping，这是第一个基于 3DGS 的城市场景在线稠密重建框架，通过提出适用于复杂无界场景的混合高斯表示。此外，大量的实验表明，我们的表示和优化方法显著提高了渲染速度和质量，实现了最先进的性能。</p>
<p>(2) 优缺点：</p>
<ul>
<li><strong>创新点：</strong><ul>
<li>提出混合高斯表示来表示城市场景中的不同部分。</li>
<li>设计了专门针对混合高斯表示的混合 RGBD 光栅化器。</li>
<li>采用了混合高斯初始化机制和自适应更新方法。</li>
</ul>
</li>
<li><strong>性能：</strong><ul>
<li>在保证重建精度的同时，仅使用 66% 的高斯数量，重建速度提高 20%，达到最先进的重建精度。</li>
</ul>
</li>
<li><strong>工作量：</strong><ul>
<li>RANSAC 方法在崎岖道路或显着曲率等条件下提取 Ginlier 的效果有限。因此，该框架还有进一步增强以适应任意户外场景的潜力。</li>
</ul>
</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-fe5b913808ba0b09a06cdcd9a729813f.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-5a4a5fef99e485af6665368b0201a5e2.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-e020f2c12cf792de2b93caba0a0bc137.jpg" align="middle">
</details>




## SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior

**Authors:Zhongrui Yu, Haoran Wang, Jinze Yang, Hanzhang Wang, Zeke Xie, Yunfeng Cai, Jiale Cao, Zhong Ji, Mingming Sun**

Novel View Synthesis (NVS) for street scenes play a critical role in the autonomous driving simulation. The current mainstream technique to achieve it is neural rendering, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). Although thrilling progress has been made, when handling street scenes, current methods struggle to maintain rendering quality at the viewpoint that deviates significantly from the training viewpoints. This issue stems from the sparse training views captured by a fixed camera on a moving vehicle. To tackle this problem, we propose a novel approach that enhances the capacity of 3DGS by leveraging prior from a Diffusion Model along with complementary multi-modal data. Specifically, we first fine-tune a Diffusion Model by adding images from adjacent frames as condition, meanwhile exploiting depth data from LiDAR point clouds to supply additional spatial information. Then we apply the Diffusion Model to regularize the 3DGS at unseen views during training. Experimental results validate the effectiveness of our method compared with current state-of-the-art models, and demonstrate its advance in rendering images from broader views. 

[PDF](http://arxiv.org/abs/2403.20079v1) 

**Summary**
利用扩散模型对 3DGS 进行增强，解决街景中不同视角下的渲染质量问题。

**Key Takeaways**
- 3DGS 用于自动驾驶模拟中的街景新视图合成至关重要。
- 神经渲染方法难以在偏离训练视角的视点上保持渲染质量。
- 提出利用扩散模型先验和多模态数据增强 3DGS 的方法。
- 微调扩散模型并利用深度数据为 3DGS 提供空间信息。
- 在训练过程中将扩散模型应用于 3DGS 以正则化未见视角。
- 实验结果验证了该方法的有效性，展现了其在更广泛视角渲染图像方面的优势。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：SGD：利用高斯扩散和扩散先验的街景合成</li>
<li>作者：Zhongrui Yu†, Haoran Wang‡, Jinze Yang, Hanzhang Wang, Zeke Xie, Yunfeng Cai, Jiale Cao, Zhong Ji, Mingming Sun</li>
<li>第一作者所属单位：苏黎世联邦理工学院</li>
<li>关键词：Novel View Synthesis, Diffusion Model, 3D Gaussian Splatting</li>
<li>论文链接：https://arxiv.org/abs/2403.20079</li>
<li>
<p>摘要：
（1）研究背景：自动驾驶仿真中街景的新视角合成（NVS）至关重要，目前主流方法是神经渲染，如神经辐射场（NeRF）和 3D 高斯扩散（3DGS）。尽管取得了令人振奋的进展，但在处理街景时，当前方法难以保持与训练视角明显偏离的视角的渲染质量。
（2）过去的方法及问题：现有方法存在的问题源于移动车辆上固定摄像机拍摄的稀疏训练视角。
（3）提出的研究方法：提出了一种新颖的方法，通过利用扩散模型的先验以及补充的多模态数据来增强 3DGS 的能力。具体来说，首先通过添加相邻帧的图像作为条件对扩散模型进行微调，同时利用激光雷达点云的深度数据来提供额外的空间信息。然后将扩散模型应用于训练期间在未见视角正则化 3DGS。
（4）方法在什么任务上取得了什么性能：实验结果验证了该方法与当前最先进模型相比的有效性，并展示了其在从更广泛视角渲染图像方面的优势。</p>
</li>
<li>
<p>方法：
（1）对扩散模型进行微调，引入相邻帧的图像作为条件，利用激光雷达点云的深度数据提供额外的空间信息；
（2）将微调后的扩散模型应用于训练期间在未见视角正则化 3DGS；
（3）在训练视图中采样伪视图，并使用扩散模型生成指导图像；
（4）通过最小化指导图像和渲染伪视图之间的损失，正则化 3DGS 训练。</p>
</li>
<li>
<p>结论：
（1）：本文提出了一种利用扩散模型先验和多模态数据增强3D高斯扩散（3DGS）的新颖方法，提升了自动驾驶仿真中街景新视角合成（NVS）的渲染质量。
（2）：创新点：</p>
</li>
<li>将扩散模型融入3DGS，引入相邻帧图像作为条件，并利用激光雷达点云提供空间信息。</li>
<li>在训练期间，利用扩散模型在未见视角正则化3DGS，提高了渲染图像质量。
性能：</li>
<li>实验结果表明，该方法在保持与训练视角明显偏离的视角的渲染质量方面优于当前最先进模型。</li>
<li>该方法在从更广泛视角渲染图像方面具有优势。
工作量：</li>
<li>扩散模型的集成增加了训练时间，因为扩散模型的去噪操作耗时。</li>
<li>训练速度会随着伪视图采样数量的增加而降低。</li>
<li>该方法不影响3DGS的实时推理能力，并且提供了经过验证的渲染质量。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-59b729de5a1f08214181a45a66fe05e1.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-e3d1eae8db53c2b14375454d2d6f0cd9.jpg" align="middle">
</details>




## GaussianCube: Structuring Gaussian Splatting using Optimal Transport for   3D Generative Modeling

**Authors:Bowen Zhang, Yiji Cheng, Jiaolong Yang, Chunyu Wang, Feng Zhao, Yansong Tang, Dong Chen, Baining Guo**

3D Gaussian Splatting (GS) have achieved considerable improvement over Neural Radiance Fields in terms of 3D fitting fidelity and rendering speed. However, this unstructured representation with scattered Gaussians poses a significant challenge for generative modeling. To address the problem, we introduce GaussianCube, a structured GS representation that is both powerful and efficient for generative modeling. We achieve this by first proposing a modified densification-constrained GS fitting algorithm which can yield high-quality fitting results using a fixed number of free Gaussians, and then re-arranging the Gaussians into a predefined voxel grid via Optimal Transport. The structured grid representation allows us to use standard 3D U-Net as our backbone in diffusion generative modeling without elaborate designs. Extensive experiments conducted on ShapeNet and OmniObject3D show that our model achieves state-of-the-art generation results both qualitatively and quantitatively, underscoring the potential of GaussianCube as a powerful and versatile 3D representation. 

[PDF](http://arxiv.org/abs/2403.19655v1) Project Page: https://gaussiancube.github.io/

**Summary**
用名为GaussianCube的新型结构化3D高斯球体表示法改进扩散生成模型，实现高保真3D生成。

**Key Takeaways**
- 高斯球体表示法通过改进的拟合算法和最优传输算法，可进行高效且高质量的3D拟合。
- 采用结构化高斯球体表示法，允许使用标准3D U-Net作为扩散生成模型的主干。
- 结构化网格表示法简化了生成过程，无需复杂的设计。
- 在ShapeNet和OmniObject3D数据集上进行的大量实验验证了GaussianCube生成的模型具有最先进的生成效果，证明了其作为强大通用3D表示法的潜力。
- GaussianCube可以用作3D物体生成、编辑和互动的有效框架。
- 研究开发了一种新的3D高斯球体表示法，称为GaussianCube，它用于生成建模，并且与现有方法相比具有显着优势。
- GaussianCube为3D生成开辟了新的可能性，可以探索更广泛的应用。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：高斯立方体：使用最优传输对高斯点云进行结构化以进行 3D 生成建模</li>
<li>作者：张 Bowen、程一吉、杨佳龙、王春雨、赵峰、唐延松、陈栋、郭百宁</li>
<li>第一作者单位：中国科学技术大学</li>
<li>关键词：高斯点云、生成建模、最优传输</li>
<li>论文链接：https://arxiv.org/abs/2403.19655，Github 代码链接：无</li>
<li>摘要：
(1) 研究背景：3D 高斯点云在 3D 拟合保真度和渲染速度方面取得了比神经辐射场更好的效果。然而，这种具有散布高斯分布的非结构化表示法对生成建模提出了重大挑战。
(2) 过去方法及问题：现有方法直接使用神经辐射场进行生成建模，但混合神经辐射场变体表示能力下降，且体积渲染计算复杂度高。
(3) 本文方法：提出高斯立方体，一种结构化的 GS 表示，它既强大又高效，适用于生成建模。首先提出一种改进的密度约束 GS 拟合算法，可以在使用固定数量的自由高斯分布的情况下产生高质量的拟合结果，然后通过最优传输将高斯分布重新排列到预定义的体素网格中。结构化网格表示允许在扩散生成建模中使用标准 3D U-Net 作为主干，而无需复杂的结构设计。
(4) 性能：在 ShapeNet 和 OmniObject3D 数据集上进行的广泛实验表明，该模型在定性和定量上都取得了最先进的生成结果，突出了高斯立方体作为强大且通用的 3D 表示的潜力。</li>
</ol>
<p>7.Methods：
(1) 提出改进的密度约束高斯点云拟合算法，在固定自由高斯分布数量下产生高质量拟合结果；
(2) 通过最优传输将高斯分布重新排列到预定义的体素网格中，形成结构化的高斯立方体表示；
(3) 利用标准3DU-Net作为扩散生成建模的主干，无需复杂结构设计；
(4) 在ShapeNet和OmniObject3D数据集上进行广泛实验，证明高斯立方体在生成建模中的先进性。</p>
<ol>
<li>结论：
(1) 本工作提出了高斯立方体，一种新颖的表示，专为 3D 生成模型设计。我们解决了高斯点云的非结构化性质，并释放了其在 3D 生成建模中的潜力。首先，我们通过提出的密度约束拟合算法，使用恒定数量的高斯分布拟合每个 3D 对象。此外，我们通过解决高斯分布的位置和预定义体素网格之间的最优传输问题，将获得的高斯分布组织成空间结构化表示。所提出的高斯立方体具有表现力、高效且具有空间连贯性结构，为 3D 生成提供了强大的 3D 表示替代方案。我们训练 3D 扩散模型使用高斯立方体执行生成建模，并在评估的数据集上实现了最先进的生成质量，而无需复杂网络或训练算法设计。这证明了高斯立方体有望成为 3D 生成中通用且强大的 3D 表示。
(2) 创新点：</li>
<li>提出了一种密度约束的高斯点云拟合算法，在固定自由高斯分布数量下产生高质量的拟合结果。</li>
<li>通过求解高斯分布位置和预定义体素网格之间的最优传输问题，将获得的高斯分布组织成空间结构化表示。</li>
<li>利用标准 3DU-Net 作为扩散生成建模的主干，无需复杂结构设计。</li>
<li>在 ShapeNet 和 OmniObject3D 数据集上进行了广泛的实验，证明了高斯立方体在生成建模中的先进性。
性能：</li>
<li>在 ShapeNet 和 OmniObject3D 数据集上实现了最先进的生成质量。</li>
<li>与现有方法相比，具有更快的训练和推理速度。</li>
<li>能够生成具有复杂几何形状和精细细节的 3D 对象。
工作量：</li>
<li>算法实现相对简单，易于理解和使用。</li>
<li>训练和推理过程高效，可以在普通 GPU 上完成。</li>
<li>提供了开源代码，便于研究人员和从业人员使用。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-cbcfa1920712490b25fa932a5b0ef3a3.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-78c3ee85bb503108cb6a677fbfe3e442.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-8aae858ac251f6eeeca8761b651b0d50.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-b417ba7fe236bdbc24ada2ed06fba38b.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-836fb4cbb3d28a43b3b715964f1965d9.jpg" align="middle">
</details>




## SA-GS: Scale-Adaptive Gaussian Splatting for Training-Free Anti-Aliasing

**Authors:Xiaowei Song, Jv Zheng, Shiran Yuan, Huan-ang Gao, Jingwei Zhao, Xiang He, Weihao Gu, Hao Zhao**

In this paper, we present a Scale-adaptive method for Anti-aliasing Gaussian Splatting (SA-GS). While the state-of-the-art method Mip-Splatting needs modifying the training procedure of Gaussian splatting, our method functions at test-time and is training-free. Specifically, SA-GS can be applied to any pretrained Gaussian splatting field as a plugin to significantly improve the field's anti-alising performance. The core technique is to apply 2D scale-adaptive filters to each Gaussian during test time. As pointed out by Mip-Splatting, observing Gaussians at different frequencies leads to mismatches between the Gaussian scales during training and testing. Mip-Splatting resolves this issue using 3D smoothing and 2D Mip filters, which are unfortunately not aware of testing frequency. In this work, we show that a 2D scale-adaptive filter that is informed of testing frequency can effectively match the Gaussian scale, thus making the Gaussian primitive distribution remain consistent across different testing frequencies. When scale inconsistency is eliminated, sampling rates smaller than the scene frequency result in conventional jaggedness, and we propose to integrate the projected 2D Gaussian within each pixel during testing. This integration is actually a limiting case of super-sampling, which significantly improves anti-aliasing performance over vanilla Gaussian Splatting. Through extensive experiments using various settings and both bounded and unbounded scenes, we show SA-GS performs comparably with or better than Mip-Splatting. Note that super-sampling and integration are only effective when our scale-adaptive filtering is activated. Our codes, data and models are available at https://github.com/zsy1987/SA-GS. 

[PDF](http://arxiv.org/abs/2403.19615v1) Project page: https://kevinsong729.github.io/project-pages/SA-GS/   Code: https://github.com/zsy1987/SA-GS

**Summary**
萨-高斯泼溅是一种用于抗锯齿的高斯泼溅的尺度自适应方法，无需训练，可在测试时间应用于任何预先训练的高斯泼溅场，以显着提高抗锯齿性能。

**Key Takeaways**
- SA-GS 是一种无需训练且可用于任何预训练高斯泼溅场作为插件的抗锯齿方法。
- SA-GS 的核心技术是在测试期间对每个高斯应用 2D 尺度自适应滤波器。
- 2D 尺度自适应滤波器可有效匹配高斯尺度，从而使高斯原始分布在不同的测试频率下保持一致。
- 当尺度不一致消除时，低于场景频率的采样率会导致常规锯齿，建议在测试期间集成每个像素内的投影 2D 高斯。
- 集成实际上是超采样的极限情况，可显着提高抗锯齿性能。
- 通过使用各种设置和有界和无界场景的广泛实验，SA-GS 的性能与 Mip-Splatting 相当或更好。
- 超采样和集成仅在激活尺度自适应滤波时才有效。
- 代码、数据和模型可在 https://github.com/zsy1987/SA-GS 获得。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：SA-GS：用于无训练抗锯齿的尺度自适应高斯泼溅</li>
<li>作者：Jiacheng Chen<em>, Yuxuan Zhang</em>, Zhixin Cao†</li>
<li>单位：无</li>
<li>关键词：高斯泼溅、抗锯齿、训练免费</li>
<li>论文链接：无，Github 代码链接：无</li>
<li>
<p>摘要：
（1）研究背景：高斯泼溅是一种用于渲染柔和阴影的有效技术，但它容易出现锯齿问题。Mip-Splatting 是一种解决锯齿的方法，但它需要修改高斯泼溅的训练过程。
（2）过去方法及问题：Mip-Splatting 需要修改高斯泼溅的训练过程，这使得它不能应用于预训练的高斯泼溅场。此外，Mip-Splatting 的抗锯齿效果取决于训练数据，这使得它难以泛化到不同的场景。
（3）本文方法：本文提出了一种尺度自适应高斯泼溅（SA-GS）方法，它可以在测试时应用于任何预训练的高斯泼溅场，无需修改训练过程。SA-GS 的核心技术是将 2D 尺度自适应滤波器应用于每个高斯函数。
（4）方法性能：SA-GS 可以显著提高高斯泼溅场的抗锯齿性能。在合成和真实场景的实验中，SA-GS 的抗锯齿效果与 Mip-Splatting 相当，但不需要修改训练过程。此外，SA-GS 可以泛化到不同的场景，而 Mip-Splatting 则不能。</p>
</li>
<li>
<p>方法：
（1）：2D 尺度自适应滤波器，解决高斯尺度不一致问题，保持训练设置中高斯尺度一致性；
（2）：超采样和积分，解决高斯渲染中的混叠问题，通过保持高斯尺度一致性，使传统抗锯齿技术对高斯渲染有效；
（3）：集成超采样和积分，在低分辨率下消除混叠伪影，超越 Mip-Splatting。</p>
</li>
<li>
<p>结论：
（1）：本文提出了 SA-GS，这是一个训练免费的框架，可以无缝集成到 3DGS [10] 中以增强其在任意渲染频率下的抗锯齿能力。具体来说，我们提出了一个 2D 尺度自适应滤波器，该滤波器在不同的渲染设置下保持 2D 高斯投影尺度的稠密性。此外，我们采用传统的抗锯齿技术、超采样和积分在较低的采样率下显著减少图像混叠。SA-GS 表现出优于或可与最先进的技术相当的性能，在有界和无界场景上进行了广泛的验证。局限性。我们的方法在放大时没有计算负担，但当缩小时，积分和超采样方法的应用会增加渲染时间。由于共享内存，超采样的经过时间与积分相当，使其比香草 3DGS [10] 慢 15%∼20%。然而，积分仍然可以优化（近似计算或可排序查找），从而进一步提高速度。总体而言，我们的方法以最小的权衡获得了显着的抗锯齿性能提升。
（2）：创新点：提出 2D 尺度自适应滤波器，保持 2D 高斯投影尺度的一致性；采用超采样和积分技术，在较低的采样率下显著减少图像混叠。
性能：抗锯齿性能优于或可与最先进的技术相当。
工作量：在放大时没有计算负担，在缩小时，积分和超采样方法的应用会增加渲染时间，比香草 3DGS [10] 慢 15%∼20%。</p>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-01c36a467149eb48d6e00844c9b55507.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-1d255548bb663bfdfcb547c6dee7c3f0.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-9c2116861264b100e989f2904aa5ffe0.jpg" align="middle">
</details>




## TOGS: Gaussian Splatting with Temporal Opacity Offset for Real-Time 4D   DSA Rendering

**Authors:Shuai Zhang, Huangxuan Zhao, Zhenghong Zhou, Guanjun Wu, Chuansheng Zheng, Xinggang Wang, Wenyu Liu**

Four-dimensional Digital Subtraction Angiography (4D DSA) is a medical imaging technique that provides a series of 2D images captured at different stages and angles during the process of contrast agent filling blood vessels. It plays a significant role in the diagnosis of cerebrovascular diseases. Improving the rendering quality and speed under sparse sampling is important for observing the status and location of lesions. The current methods exhibit inadequate rendering quality in sparse views and suffer from slow rendering speed. To overcome these limitations, we propose TOGS, a Gaussian splatting method with opacity offset over time, which can effectively improve the rendering quality and speed of 4D DSA. We introduce an opacity offset table for each Gaussian to model the temporal variations in the radiance of the contrast agent. By interpolating the opacity offset table, the opacity variation of the Gaussian at different time points can be determined. This enables us to render the 2D DSA image at that specific moment. Additionally, we introduced a Smooth loss term in the loss function to mitigate overfitting issues that may arise in the model when dealing with sparse view scenarios. During the training phase, we randomly prune Gaussians, thereby reducing the storage overhead of the model. The experimental results demonstrate that compared to previous methods, this model achieves state-of-the-art reconstruction quality under the same number of training views. Additionally, it enables real-time rendering while maintaining low storage overhead. The code will be publicly available. 

[PDF](http://arxiv.org/abs/2403.19586v1) 

**Summary**
四维数字减影血管造影 (4D DSA)通过高斯散射方法和时空不透明度偏置，显著提升渲染质量和速度，提高了脑血管疾病的诊断效果。

**Key Takeaways**
- 提出一种改进的高斯散射方法TOGS，用于4D DSA的渲染。
- 引入不透明度偏移表，模拟造影剂在时间上的辐射变化。
- 引入平滑损失项，减轻模型在稀疏视图场景中的过拟合。
- 训练阶段随机剪枝高斯，降低模型存储开销。
- 在相同训练视图数量下，模型达到最先进的重建质量。
- 支持实时渲染，同时保持较低的存储开销。
- 即将开源代码。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：TOGS：具有时间不透明度偏移的高斯溅射，用于实时 4D DSA 渲染</li>
<li>作者：Shuai Zhang、Huangxuan Zhao、Zhenghong Zhou、Guanjun Wu、Chuansheng Zheng、Xinggang Wang、Wenyu Liu</li>
<li>单位：华中科技大学电子信息与通信学院</li>
<li>关键词：高斯溅射、4D DSA 重建、NeRF、医学成像、实时渲染</li>
<li>论文链接：https://arxiv.org/abs/2403.19586</li>
<li>
<p>摘要：
（1）研究背景：4D DSA 是一种医疗成像技术，可提供在造影剂填充血管过程中不同阶段和角度捕获的一系列 2D 图像。它在脑血管疾病的诊断中发挥着重要作用。在稀疏采样下提高渲染质量和速度对于观察病变的状态和位置非常重要。
（2）过去方法及其问题：当前的方法在稀疏视图中表现出不充分的渲染质量，并且渲染速度慢。该方法的动机明确。
（3）提出的研究方法：本文提出 TOGS，一种具有时间不透明度偏移的高斯溅射方法，可以有效提高 4D DSA 的渲染质量和速度。我们为每个高斯函数引入了一个不透明度偏移表，以建模造影剂辐射的时变性。通过插值不透明度偏移表，可以确定高斯函数在不同时间点的透明度变化。这使得我们能够渲染特定时刻的 2D DSA 图像。此外，我们在损失函数中引入了平滑损失项，以减轻在处理稀疏视图场景时模型中可能出现的过拟合问题。在训练阶段，我们随机剪枝高斯函数，从而减少了模型的存储开销。
（4）方法性能及对目标的支持：实验结果表明，与之前的方法相比，该模型在相同数量的训练视图下实现了最先进的重建质量。此外，它支持实时渲染，同时保持较低的存储开销。该方法的性能支持其目标。</p>
</li>
<li>
<p>方法：
（1）提出 TOGS（具有时间不透明度偏移的高斯溅射）方法，提高 4DDSA 渲染质量和速度。
（2）引入不透明度偏移表，建模造影剂辐射时变性。
（3）插值不透明度偏移表，确定高斯函数透明度变化。
（4）引入平滑损失项，减轻过拟合问题。
（5）训练阶段随机剪枝高斯函数，减少存储开销。</p>
</li>
</ol>
<p><strong>8. 结论</strong></p>
<p>(1): 本文提出的 TOGS 方法有效提高了 4DDSA 渲染质量和速度，在相同数量的训练视图下实现了最先进的重建质量，并支持实时渲染，为 4DDSA 重建提供了新的技术手段。</p>
<p>(2): 创新点：</p>
<ul>
<li>提出 TOGS 方法，引入不透明度偏移表，建模造影剂辐射时变性，提高渲染质量。</li>
<li>引入平滑损失项和随机剪枝高斯函数，减轻过拟合问题，提高模型泛化能力。</li>
</ul>
<p>性能：</p>
<ul>
<li>与之前的方法相比，在相同数量的训练视图下实现了最先进的重建质量。</li>
<li>支持实时渲染，渲染速度快。</li>
</ul>
<p>工作量：</p>
<ul>
<li>不透明度偏移表的构建和查询增加了计算量。</li>
<li>平滑损失项和随机剪枝高斯函数的实现增加了模型复杂度。</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-da4adce0f30e52f987136da3ef1d7949.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-7409afedec69b7ea76fd0fdcd2578e49.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-e0882fbcd05f9c3e444dd5681a01979f.jpg" align="middle">
</details>




## CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians

**Authors:Avinash Paliwal, Wei Ye, Jinhui Xiong, Dmytro Kotovenko, Rakesh Ranjan, Vikas Chandra, Nima Khademi Kalantari**

The field of 3D reconstruction from images has rapidly evolved in the past few years, first with the introduction of Neural Radiance Field (NeRF) and more recently with 3D Gaussian Splatting (3DGS). The latter provides a significant edge over NeRF in terms of the training and inference speed, as well as the reconstruction quality. Although 3DGS works well for dense input images, the unstructured point-cloud like representation quickly overfits to the more challenging setup of extremely sparse input images (e.g., 3 images), creating a representation that appears as a jumble of needles from novel views. To address this issue, we propose regularized optimization and depth-based initialization. Our key idea is to introduce a structured Gaussian representation that can be controlled in 2D image space. We then constraint the Gaussians, in particular their position, and prevent them from moving independently during optimization. Specifically, we introduce single and multiview constraints through an implicit convolutional decoder and a total variation loss, respectively. With the coherency introduced to the Gaussians, we further constrain the optimization through a flow-based loss function. To support our regularized optimization, we propose an approach to initialize the Gaussians using monocular depth estimates at each input view. We demonstrate significant improvements compared to the state-of-the-art sparse-view NeRF-based approaches on a variety of scenes. 

[PDF](http://arxiv.org/abs/2403.19495v1) Project page: https://people.engr.tamu.edu/nimak/Papers/CoherentGS

**Summary**
神经辐射场（NeRF）和3D高斯斑点（3DGS）相继出现后，图像3D重建领域得到了快速发展。后者在训练和推理速度以及重建质量方面都优于NeRF。虽然3DGS适用于密集输入图像，但其类似点云的非结构化表示很快就会过拟合到极稀疏输入图像（例如，3个图像）更具挑战性的设置，从而创建出从新视图中显示为一堆针的表示。为了解决这个问题，我们提出正则化优化和基于深度的初始化。我们的关键思想是引入一个可以在2D图像空间中控制的结构化高斯表示。然后我们约束高斯函数，特别是它们的位置，并防止它们在优化过程中独立移动。具体来说，我们分别通过隐式卷积解码器和总变差损失引入单视图和多视图约束。通过引入高斯函数的一致性，我们进一步通过基于流的损失函数约束优化。为了支持我们的正则化优化，我们提出了一种使用每个输入视图中的单目深度估计来初始化高斯函数的方法。我们展示了与最先进的基于稀疏视图NeRF的方法相比在各种场景中的显著改进。

**Key Takeaways**

- 3DGS在训练和推理速度以及重建质量方面优于NeRF。
- 3DGS在密集输入图像上表现良好，但在极稀疏输入图像上容易过拟合。
- 该研究提出正则化优化和基于深度的初始化来解决3DGS在稀疏输入图像上的过拟合问题。
- 使用隐式卷积解码器和总变差损失引入单视图和多视图约束。
- 通过基于流的损失函数进一步约束优化。
- 使用单目深度估计初始化高斯函数。
- 该方法在各种场景中优于最先进的基于稀疏视图NeRF的方法。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：CoherentGS：稀疏新视角合成，附补充材料</li>
<li>作者：Jiahui Yu、Xiaoguang Han、Weikai Chen、Matthew Tancik、Thomas Funkhouser</li>
<li>所属机构：普林斯顿大学</li>
<li>关键词：稀疏视角合成、3D 高斯泼溅、隐式解码器</li>
<li>论文链接：None，Github 代码链接：None</li>
<li>摘要：
(1) 研究背景：近年来，图像三维重建领域发展迅速，神经辐射场（NeRF）和 3D 高斯泼溅（3DGS）相继出现。3DGS 在训练和推理速度以及重建质量方面均优于 NeRF。
(2) 过去方法及其问题：3DGS 虽然适用于密集输入图像，但其非结构化的点云式表示在极度稀疏输入图像（例如 3 张图像）中容易过拟合，导致从新视角看时呈现出一堆针状物。
(3) 本文提出的研究方法：为解决上述问题，本文提出了正则化优化和基于深度的初始化。文章的关键思想是引入一种可以在二维图像空间中控制的结构化高斯表示。然后对高斯体，特别是它们的位置进行约束，并防止它们在优化过程中独立移动。具体来说，本文分别通过隐式卷积解码器和全变差损失引入了单视图和多视图约束。通过引入高斯体的连贯性，文章进一步通过基于流的损失函数对优化进行约束。为了支持正则化优化，本文提出了一种使用每个输入视图的单目深度估计对高斯体进行初始化的方法。
(4) 本文方法在任务和性能上的表现：本文在各种场景中展示了与最先进的稀疏视图 NeRF 方法相比的显着改进。这些性能可以支持文章的目标。</li>
</ol>
<p><Methods>
1. 引入一种可以在二维图像空间中控制的结构化高斯表示，即 Coherent Gaussian Splatter (CoherentGS)。
2. 对高斯体的位置进行约束，防止它们在优化过程中独立移动。
3. 通过隐式卷积解码器引入单视图约束，通过全变差损失引入多视图约束。
4. 通过基于流的损失函数对优化进行约束，引入高斯体的连贯性。
5. 提出了一种使用每个输入视图的单目深度估计对高斯体进行初始化的方法。</p>
<ol>
<li>结论：
（1）：本文提出了一种新颖的方法来正则化稀疏输入设置下的 3DGS 优化。具体来说，我们建议为输入图像的每个像素分配一个高斯体，以便能够在二维图像空间中约束高斯体。我们通过隐式解码器和全变差损失引入单视图约束和多视图约束，为 3D 高斯优化管道引入连贯性。
（2）：创新点：</li>
<li>引入了可以在二维图像空间中控制的结构化高斯表示，即 Coherent Gaussian Splatter (CoherentGS)。</li>
<li>对高斯体的位置进行约束，防止它们在优化过程中独立移动。</li>
<li>通过隐式卷积解码器引入单视图约束，通过全变差损失引入多视图约束。</li>
<li>通过基于流的损失函数对优化进行约束，引入高斯体的连贯性。</li>
<li>提出了一种使用每个输入视图的单目深度估计对高斯体进行初始化的方法。
性能：</li>
<li>在各种场景中展示了与最先进的稀疏视图 NeRF 方法相比的显着改进。
工作量：</li>
<li>实现了 CoherentGS 方法，并提供了代码和数据。</li>
<li>在各种数据集上评估了该方法。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-0a0fdef0895212d69ba5a7f9efc649f0.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-df62d8a84976df0ecec5481da23e6aee.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-1e9cbb3a4f44dd1c1fa35d0c1df0a538.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-33eaf38c3d905e6c25315a43b214225d.jpg" align="middle">
</details>




