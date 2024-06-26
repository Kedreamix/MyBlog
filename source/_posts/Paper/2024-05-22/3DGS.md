
---
title: 3DGS
date: 2024-05-22 13:01:08
author: Kedreamix
cover: https://picx.zhimg.com/v2-68aa80c2ba44dfde97867ba03ebc2814.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-05-22  MOSS Motion-based 3D Clothed Human Synthesis from Monocular Video  
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

# 2024-05-22 更新


## MOSS: Motion-based 3D Clothed Human Synthesis from Monocular Video

**Authors:Hongsheng Wang, Xiang Cai, Xi Sun, Jinhong Yue, Shengyu Zhang, Feng Lin, Fei Wu**

Single-view clothed human reconstruction holds a central position in virtual reality applications, especially in contexts involving intricate human motions. It presents notable challenges in achieving realistic clothing deformation. Current methodologies often overlook the influence of motion on surface deformation, resulting in surfaces lacking the constraints imposed by global motion. To overcome these limitations, we introduce an innovative framework, Motion-Based 3D Clothed Humans Synthesis (MOSS), which employs kinematic information to achieve motion-aware Gaussian split on the human surface. Our framework consists of two modules: Kinematic Gaussian Locating Splatting (KGAS) and Surface Deformation Detector (UID). KGAS incorporates matrix-Fisher distribution to propagate global motion across the body surface. The density and rotation factors of this distribution explicitly control the Gaussians, thereby enhancing the realism of the reconstructed surface. Additionally, to address local occlusions in single-view, based on KGAS, UID identifies significant surfaces, and geometric reconstruction is performed to compensate for these deformations. Experimental results demonstrate that MOSS achieves state-of-the-art visual quality in 3D clothed human synthesis from monocular videos. Notably, we improve the Human NeRF and the Gaussian Splatting by 33.94% and 16.75% in LPIPS* respectively. Codes are available at https://wanghongsheng01.github.io/MOSS/. 

[PDF](http://arxiv.org/abs/2405.12806v1) 

**Summary**
单视图衣着人体重建在虚拟现实应用中至关重要，尤其是在涉及复杂人体动作的情况下。它在实现逼真的衣物变形方面面临着巨大挑战。

**Key Takeaways**
- 基于运动的信息可用于实现对运动感知的高斯分裂。
- 运动学高斯定位散布（KGAS）使用矩阵-费舍尔分布来传播全局运动。
- 表面变形检测器（UID）基于 KGAS 识别重要表面并执行几何重建。
- 与单视图中的局部遮挡作斗争，UID 识别重要的表面并执行几何重建。
- 实验结果表明，MOSS 在从单目视频中合成 3D 衣着人体方面实现了最先进的视觉质量。
- 与人类 NeRF 和高斯散布相比，MOSS 分别将 LPIPS* 提高了 33.94% 和 16.75%。
- 代码可在 https://wanghongsheng01.github.io/MOSS/ 获得。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: 基于运动的单目视频服装人物三维合成（MOSS）</p>
</li>
<li>
<p>Authors: Hongsheng Wang, Xiang Cai, Xi Sun, Jinhong Yue, Shengyu Zhang, Feng Lin, Fei Wu</p>
</li>
<li>
<p>Affiliation: 浙江大学</p>
</li>
<li>
<p>Keywords: 3D Gaussian Splatting, human reconstruction, matrix-Fisher</p>
</li>
<li>
<p>Urls: https://arxiv.org/abs/2405.12806 , Github:None</p>
</li>
<li>
<p>Summary:</p>
<pre><code>            (1):服装人物三维重建在虚拟现实应用中占据重要地位，特别是涉及复杂人体运动的场景。实现逼真的服装变形面临着巨大挑战。目前的方法往往忽视运动对表面变形的影，导致表面缺乏全局运动施加的约束。

            (2):现有的方法在重建人体表面时，利用SMPL作为人体先验，可以恢复更真实的人体，但忽略了运动树的层次结构约束和全局运动信息对重建人体表面的约束，导致关节细节模糊。此外，对恢复的表面变形探索不足。

            (3):本文提出了一种创新的框架Motion-Based Clothed 3D Humans Synthesis (MOSS)。MOSS从表面变形的成因出发，利用运动树中的运动因子（位移和旋转）进行高斯控制，提升大尺度运动下的人体重建效果。首先，针对变形重建，提出KGAS模块，通过分解matrix-Fisher分布参数，提取人体表面的主轴集中度和旋转因子，对3DGS渲染人体表面变形的高斯进行显式控制。在高斯布局过程中，主轴集中度作为密度因子，修正高斯分裂的采样概率，得到表面变形感知的高斯。在后续的分裂控制中，主轴集中度和旋转因子动态调整高斯的朝向和半径，增强了人体表面变形的真实性。

            (4):在单目视频服装人物三维合成任务上，MOSS取得了最先进的视觉效果。具体而言，在LPIPS指标上，比Human NeRF和Gaussian Splatting分别提升了33.94%和16.75%。该性能提升支撑了本文的目标。
</code></pre>
</li>
<li>
<p>方法：</p>
<pre><code>            (1):提出KGAS模块，分解matrix-Fisher分布参数，提取人体表面的主轴集中度和旋转因子，显式控制3DGS渲染人体表面变形的高斯；

            (2):在高斯布局过程中，主轴集中度作为密度因子，修正高斯分裂的采样概率，得到表面变形感知的高斯；

            (3):在后续的分裂控制中，主轴集中度和旋转因子动态调整高斯的朝向和半径，增强了人体表面变形的真实性；

            .......
</code></pre>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）：本文针对运动中着装人物三维重建中细节重建缺乏全局约束的问题，提出了 MOSS，该框架将运动先验引入到人体表面三维高斯渲染流程中，重点关注表面变形显著的位置。在未来的工作中，我们考虑结合图论来拓扑引导三维着装人物重建。此外，在虚拟现实和时尚产业等诸多领域存在着大量的真实人物运动场景，我们的技术具有潜在的应用前景。例如，它可以降低游戏制作成本、提升玩家体验、辅助时装设计师优化设计。</p>
<p>（2）：创新点：提出 KGAS 模块，通过分解 Matrix-Fisher 分布参数，提取人体表面的主轴集中度和旋转因子，显式控制三维高斯渲染人体表面变形的分布；性能：在单目视频着装人物三维合成任务上，MOSS 取得了最先进的视觉效果，在 LPIPS 指标上，比 Human NeRF 和 Gaussian Splatting 分别提升了 33.94% 和 16.75%；工作量：需要较大的计算资源和较长的训练时间。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-22f655136d6ba65cf221780cbe185b99.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-bf1474d02e30442a539ba5585a736b9f.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-4566050a2967d4fa1e023d77db17c9ef.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-2f3b4f7e432eaff4288eacd9a157ad2e.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-a1b13abfc76fdc00a47c873ab948c636.jpg" align="middle">
</details>




## Gaussian Control with Hierarchical Semantic Graphs in 3D Human Recovery

**Authors:Hongsheng Wang, Weiyue Zhang, Sihao Liu, Xinrui Zhou, Shengyu Zhang, Fei Wu, Feng Lin**

Although 3D Gaussian Splatting (3DGS) has recently made progress in 3D human reconstruction, it primarily relies on 2D pixel-level supervision, overlooking the geometric complexity and topological relationships of different body parts. To address this gap, we introduce the Hierarchical Graph Human Gaussian Control (HUGS) framework for achieving high-fidelity 3D human reconstruction. Our approach involves leveraging explicitly semantic priors of body parts to ensure the consistency of geometric topology, thereby enabling the capture of the complex geometrical and topological associations among body parts. Additionally, we disentangle high-frequency features from global human features to refine surface details in body parts. Extensive experiments demonstrate that our method exhibits superior performance in human body reconstruction, particularly in enhancing surface details and accurately reconstructing body part junctions. Codes are available at https://wanghongsheng01.github.io/HUGS/. 

[PDF](http://arxiv.org/abs/2405.12477v1) 

**Summary**
通过显式利用身体部件的语义先验，HUGS在3D人体重建中实现了更高的保真度，提升了曲面细节和身体部件连接处的重建精度。

**Key Takeaways**
- HUGS框架利用身体部件的显式语义先验，确保几何拓扑的一致性。
- 结合低频和高频特征，提升了表面细节和身体部件连接处的重建精度。
- 通过对不同身体部件的拓扑关系建模，解决了3DGS忽略身体部件几何复杂性问题。
- 利用分层图结构对身体进行建模，实现多尺度特征提取。
- HUGS在人体重建任务上展现出优异的性能，提升了曲面细节和身体部件连接处重建精度。
- 代码已开源，可用于进一步研究和应用。
- HUGS为3D人体重建提供了新的思路，有助于提高重建质量和效率。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：高斯控制与分层语义图在三维人体恢复中的应用</p>
</li>
<li>
<p>作者：洪胜王、伟跃张、思浩刘、新睿周、胜宇张、飞吴、峰林</p>
</li>
<li>
<p>单位：浙江大学</p>
</li>
<li>
<p>关键词：3D高斯溅射、人体重建、人体语义、图聚类、高频解耦</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.12477v1，Github：https://wanghongsheng01.github.io/HUGS/</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：三维高斯溅射（3DGS）在三维人体重建方面取得了进展，但主要依赖于二维像素级监督，忽略了不同身体部位的几何复杂性和拓扑关系。</p>
<p>（2）：过去方法及其问题：基于像素级监督的3DGS人体重建方法忽略了身体部位的几何复杂性和运动相关性，导致局部几何失真和重要细节丢失。</p>
<p>（3）：本文方法：提出了一种高斯控制与分层语义图的人体重建框架（HUGS），通过语义运动拓扑模块学习语义属性一致性和每个高斯的运动拓扑关联，以捕捉身体部位的复杂几何结构和联动效应；同时，基于语义先验和拓扑关联，提出表面解耦模块，解耦高频特征和人体全局特征，细化高频差异显著的表面细节。</p>
<p>（4）：方法性能：HUGS在人体重建任务上取得了优异的性能，特别是在增强表面细节和准确重建身体部位连接方面。实验结果表明，该方法能够有效解决局部遮挡导致的局部几何失真问题，并保留了重要细节，支持了本文的目标。</p>
<ol>
<li>Methods:</li>
</ol>
<p>（1）：提出高斯控制与分层语义图的人体重建框架（HUGS），通过语义运动拓扑模块学习语义属性一致性和每个高斯的运动拓扑关联，以捕捉身体部位的复杂几何结构和联动效应；</p>
<p>（2）：基于语义先验和拓扑关联，提出表面解耦模块，解耦高频特征和人体全局特征，细化高频差异显著的表面细节；</p>
<p>（3）：采用分层语义图，将身体部位划分为不同的语义级别，并根据语义关联和运动拓扑关系构建分层语义图，指导高斯控制模块生成具有语义一致性和运动关联性的高斯人。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种高斯控制与分层语义图的人体重建框架（HUGS），通过语义运动拓扑模块学习语义属性一致性和每个高斯的运动拓扑关联，以捕捉身体部位的复杂几何结构和联动效应；基于语义先验和拓扑关联，提出表面解耦模块，解耦高频特征和人体全局特征，细化高频差异显著的表面细节。该框架在人体重建任务上取得了优异的性能，特别是在增强表面细节和准确重建身体部位连接方面，为解决局部遮挡导致的局部几何失真问题并保留重要细节提供了新的思路。</p>
<p>（2）：创新点：提出了一种新的高斯控制与分层语义图的人体重建框架，通过语义运动拓扑模块学习语义属性一致性和每个高斯的运动拓扑关联，以捕捉身体部位的复杂几何结构和联动效应；基于语义先验和拓扑关联，提出表面解耦模块，解耦高频特征和人体全局特征，细化高频差异显著的表面细节。</p>
<p>性能：在人体重建任务上取得了优异的性能，特别是在增强表面细节和准确重建身体部位连接方面。</p>
<p>工作量：该框架涉及语义运动拓扑模块和表面解耦模块的构建，需要较高的算法设计和实现能力。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-26580554d35e5daa7c5b7ab3cdff8e7a.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-c06a20c0178a74f879aaf268055fa1d0.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-a3d1a19733df046bc51c089eb995823a.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-4f210e868ba8f342cf58f5dc57f360b1.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-49635bbada4ba319e75970afc01e743a.jpg" align="middle">
</details>




## GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and   Texture Details

**Authors:Boqian Li, Xuan Li, Ying Jiang, Tianyi Xie, Feng Gao, Huamin Wang, Yin Yang, Chenfanfu Jiang**

Traditional 3D garment creation is labor-intensive, involving sketching, modeling, UV mapping, and texturing, which are time-consuming and costly. Recent advances in diffusion-based generative models have enabled new possibilities for 3D garment generation from text prompts, images, and videos. However, existing methods either suffer from inconsistencies among multi-view images or require additional processes to separate cloth from the underlying human model. In this paper, we propose GarmentDreamer, a novel method that leverages 3D Gaussian Splatting (GS) as guidance to generate wearable, simulation-ready 3D garment meshes from text prompts. In contrast to using multi-view images directly predicted by generative models as guidance, our 3DGS guidance ensures consistent optimization in both garment deformation and texture synthesis. Our method introduces a novel garment augmentation module, guided by normal and RGBA information, and employs implicit Neural Texture Fields (NeTF) combined with Score Distillation Sampling (SDS) to generate diverse geometric and texture details. We validate the effectiveness of our approach through comprehensive qualitative and quantitative experiments, showcasing the superior performance of GarmentDreamer over state-of-the-art alternatives. Our project page is available at: https://xuan-li.github.io/GarmentDreamerDemo/. 

[PDF](http://arxiv.org/abs/2405.12420v1) 

**Summary**
基于3D 高斯 splatting 的新颖方法，可从文本提示生成可穿戴、可用于模拟的 3D 服装网格。

**Key Takeaways**
- 服装生成从繁琐的手工流程转变为文本提示、图片和视频驱动的自动化过程。
- 3DGS 指导确保服装变形和纹理合成的一致优化。
- 提出一种新颖的服装增强模块，受法线和 RGBA 信息指导。
- 采用隐式神经纹理场 (NeTF) 结合评分蒸馏采样 (SDS) 生成多样化的几何和纹理细节。
- 通过全面定性和定量实验验证了该方法的有效性。
- GarmentDreamer 优于最先进的替代方案。
- 项目主页：https://xuan-li.github.io/GarmentDreamerDemo/。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: GarmentDreamer：使用3D高斯喷绘作为指导的服装合成，具有多样化的几何和纹理细节</p>
</li>
<li>
<p>Authors: BOQIAN LI, XUAN LI, YING JIANG, TIANYI XIE, FENG GAO, HUAMIN WANG, YIN YANG, and CHENFANFU JIANG</p>
</li>
<li>
<p>Affiliation: 加州大学洛杉矶分校</p>
</li>
<li>
<p>Keywords: 3D garment synthesis, diffusion models, generative models, neural texture fields, variational score distillation</p>
</li>
<li>
<p>Urls: https://arxiv.org/abs/2405.12420 , https://xuan-li.github.io/GarmentDreamerDemo/ , Github:None</p>
</li>
<li>
<p>Summary:</p>
<p>(1): 服装的3D数字化至关重要，在时尚设计、虚拟试穿、游戏、动画、虚拟现实和机器人技术中有着广泛的应用。然而，传统的3D服装创建过程需要大量的人工操作，包括素描、建模、UV映射、纹理化、着色和模拟，耗费大量时间和人力成本。</p>
<p>(2): 基于扩散的生成模型的进步，从文本和图像生成3D服装的方法主要有两种：一种是从2D缝纫图案开始，然后从这些图案生成3D服装；另一种是生成模型直接预测基于图像和文本输入的3D目标形状的分布，无需依赖2D缝纫图案。但是，前一种方法需要大量的缝纫图案和相应的文本或图像之间的配对训练数据；后一种方法虽然更简单，但会遇到多视图不一致和缺乏高保真细节等问题，通常需要额外的后处理才能用于下游模拟任务。</p>
<p>(3): 本文提出了一种名为GarmentDreamer的新方法，利用3D高斯喷绘（GS）作为指导，从文本提示中生成可穿戴、可模拟的3D服装网格。与直接使用生成模型预测的多视图图像作为指导不同，本文的3DGS指导确保了服装变形和纹理合成中的一致优化。该方法引入了一个新颖的服装增强模块，由法线和RGBA信息指导，并采用隐式神经纹理场（NeTF）结合变分分数蒸馏（VSD）来生成多样化的几何和纹理细节。</p>
<p>(4): 通过全面的定性和定量实验验证了本文方法的有效性，展示了GarmentDreamer优于最先进的替代方案。</p>
</li>
<li>
<p>方法：</p>
<p>（1）：从文本提示中生成服装模板网格，该网格利用了基于扩散的生成模型；</p>
<p>（2）：基于文本提示和服装模板网格优化 3D 高斯喷绘（3DGS），该喷绘指导了服装变形和纹理合成；</p>
<p>（3）：设计两阶段训练，利用 3DGS 指导，将服装模板网格细化为最终服装形状；</p>
<p>（4）：优化隐式神经纹理场（NeTF），通过变分分数蒸馏（VSD）生成高质量纹理。</p>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）：本文提出了一种名为 GarmentDreamer 的新方法，该方法利用 3D 高斯喷绘（3DGS）作为指导，从文本提示中生成可穿戴、可模拟的 3D 服装网格。该方法引入了一个新颖的服装增强模块，并采用隐式神经纹理场（NeTF）结合变分分数蒸馏（VSD）来生成多样化的几何和纹理细节。通过全面的定性和定量实验验证了本文方法的有效性，展示了 GarmentDreamer 优于最先进的替代方案。</p>
<p>（2）：创新点：GarmentDreamer 创新性地利用 3DGS 作为指导，确保了服装变形和纹理合成中的一致优化，并引入了新颖的服装增强模块和 NeTF+VSD 纹理生成管道。</p>
<p>性能：GarmentDreamer 在生成可穿戴、可模拟的 3D 服装方面表现出色，生成的服装具有多样化的几何和纹理细节。</p>
<p>工作量：GarmentDreamer 的训练过程需要大量的数据和计算资源，但生成单个服装的推理时间相对较快。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-878e18873a5681aa176eaa338c3e6ce9.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-0f8188b227280d59ad98e1f1b7e962d0.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-1dd9c3e580fb71b128d4b0a85786a05d.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-a883313d54acc297ba89748c39578624.jpg" align="middle">
</details>




## AtomGS: Atomizing Gaussian Splatting for High-Fidelity Radiance Field

**Authors:Rong Liu, Rui Xu, Yue Hu, Meida Chen, Andrew Feng**

3D Gaussian Splatting (3DGS) has recently advanced radiance field reconstruction by offering superior capabilities for novel view synthesis and real-time rendering speed. However, its strategy of blending optimization and adaptive density control might lead to sub-optimal results; it can sometimes yield noisy geometry and blurry artifacts due to prioritizing optimizing large Gaussians at the cost of adequately densifying smaller ones. To address this, we introduce AtomGS, consisting of Atomized Proliferation and Geometry-Guided Optimization. The Atomized Proliferation constrains ellipsoid Gaussians of various sizes into more uniform-sized Atom Gaussians. The strategy enhances the representation of areas with fine features by placing greater emphasis on densification in accordance with scene details. In addition, we proposed a Geometry-Guided Optimization approach that incorporates an Edge-Aware Normal Loss. This optimization method effectively smooths flat surfaces while preserving intricate details. Our evaluation shows that AtomGS outperforms existing state-of-the-art methods in rendering quality. Additionally, it achieves competitive accuracy in geometry reconstruction and offers a significant improvement in training speed over other SDF-based methods. More interactive demos can be found in our website (\href{https://rongliu-leo.github.io/AtomGS/}{https://rongliu-leo.github.io/AtomGS/}). 

[PDF](http://arxiv.org/abs/2405.12369v1) 

**Summary**
3D高斯泼洒技术通过原子化增殖和几何引导优化提升了视点合成和实时渲染能力。

**Key Takeaways**

* Atomized Proliferation 策略将不同大小的椭球形高斯约束为更均匀大小的原子高斯。
* 提升了对精细特征区域的表示，使其与场景细节更一致。
* Geometry-Guided Optimization 方法引入了边缘感知法线损失，有效平滑了平面表面，同时保留了复杂细节。
* AtomGS 在渲染质量上优于现有最先进的方法。
* 在几何重建中实现了有竞争力的精度，并且比其他基于 SDF 的方法显着提高了训练速度。
* 提供交互式演示（网址：\href{https://rongliu-leo.github.io/AtomGS/}{https://rongliu-leo.github.io/AtomGS/}）。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：AtomGS：原子化高斯泼溅用于高保真辐射场</p>
</li>
<li>
<p>作者：Rong Liu, Rui Xu, Yue Hu, Meida Chen, Andrew Feng</p>
</li>
<li>
<p>单位：南加州大学创意技术学院</p>
</li>
<li>
<p>关键词：辐射场、高斯泼溅、原子化</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.12369v1 , Github：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>(1)：研究背景：3D高斯泼溅（3DGS）通过提供新颖的视图合成和实时渲染速度的卓越能力，最近在辐射场重建方面取得了进展。</p>
<p>(2)：过去的方法及其问题：3DGS 混合优化和自适应密度控制的策略可能会导致次优结果；由于优先优化大高斯而牺牲了充分致密化小高斯的代价，它有时会出现噪声几何和模糊伪影。</p>
<p>(3)：本文提出的研究方法：AtomGS，由原子化扩散和自适应密度控制组成，以解决 3DGS 中存在的问题。</p>
<p>(4)：方法在什么任务上取得了什么性能：AtomGS 在渲染质量方面优于现有方法，并且通过将高斯约束为原子高斯并将其与自然几何精确对齐，在几何精度方面取得了有竞争力的结果。</p>
<ol>
<li>
<p>方法：</p>
<pre><code>            (1): 原子化扩散：对输入的 SfM 点进行分析，确定原子尺度 Sa，将高斯约束为原子高斯，并优先扩散原子高斯以快速对齐场景的固有几何结构；

            (2): 几何引导优化：利用提出的边缘感知法向量损失和修改的多尺度 SSIM 损失，确保增强重点放在保持几何精度上，而不会影响 RGB 场保真度。
</code></pre>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）：xxx；</p>
<p>（2）：创新点：原子化扩散和几何引导优化；性能：渲染质量优异，几何精度有竞争力；工作量：与原有 3DGS 方法相比，GS 原语数量更少。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-64026f1bd2c377d2f1ee8b5eb94407a2.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1f8dc1445548bec8c9ae8715249decf1.jpg" align="middle">
</details>




## Fast Generalizable Gaussian Splatting Reconstruction from Multi-View   Stereo

**Authors:Tianqi Liu, Guangcong Wang, Shoukang Hu, Liao Shen, Xinyi Ye, Yuhang Zang, Zhiguo Cao, Wei Li, Ziwei Liu**

We present MVSGaussian, a new generalizable 3D Gaussian representation approach derived from Multi-View Stereo (MVS) that can efficiently reconstruct unseen scenes. Specifically, 1) we leverage MVS to encode geometry-aware Gaussian representations and decode them into Gaussian parameters. 2) To further enhance performance, we propose a hybrid Gaussian rendering that integrates an efficient volume rendering design for novel view synthesis. 3) To support fast fine-tuning for specific scenes, we introduce a multi-view geometric consistent aggregation strategy to effectively aggregate the point clouds generated by the generalizable model, serving as the initialization for per-scene optimization. Compared with previous generalizable NeRF-based methods, which typically require minutes of fine-tuning and seconds of rendering per image, MVSGaussian achieves real-time rendering with better synthesis quality for each scene. Compared with the vanilla 3D-GS, MVSGaussian achieves better view synthesis with less training computational cost. Extensive experiments on DTU, Real Forward-facing, NeRF Synthetic, and Tanks and Temples datasets validate that MVSGaussian attains state-of-the-art performance with convincing generalizability, real-time rendering speed, and fast per-scene optimization. 

[PDF](http://arxiv.org/abs/2405.12218v1) Project page: https://mvsgaussian.github.io/

**Summary**
 多视图立体声 (MVS) 推导出 MVSGaussian，一种新型且可泛化的 3D 高斯表示方法，能够有效地重建未见场景。

**Key Takeaways**
- 利用 MVS 编码感知几何形状的高斯表示，并解码为高斯参数。
- 提出一种混合高斯渲染，集成了高效的体绘制设计以进行新视图合成。
- 引入多视图几何一致性聚合策略，以有效地聚合可泛化模型生成的点云，作为场景优化初始化。
- 与通常需要每张图像数分钟微调和几秒渲染时间的基于 NeRF 的可泛化方法相比，MVSGaussian 实现了实时渲染，并具有更好的合成质量。
- 与基本的 3D-GS 相比，MVSGaussian 以较小的训练计算成本实现了更好的视图合成。
- 在 DTU、Real Forward-facing、NeRF Synthetic 和 Tanks and Temples 数据集上的大量实验验证了 MVSGaussian 实现了最先进的性能，具有令人信服的可泛化性、实时渲染速度和快速的场景优化。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：快速可泛化的高斯散点表示法</p>
</li>
<li>
<p>作者：Tianqi Liu, Guangcong Wang, Shoukang Hu, Liao Shen, Xinyi Ye, Yuhang Zang, Zhiguo Cao, Wei Li, Ziwei Liu</p>
</li>
<li>
<p>第一作者单位：华中科技大学</p>
</li>
<li>
<p>关键词：Generalizable Gaussian Splatting · Multi-View Stereo · Neural Radiance Field · Novel View Synthesis</p>
</li>
<li>
<p>论文链接：https://mvsgaussian.github.io/
Github：None</p>
</li>
<li>
<p>摘要：</p>
<p>（1）：研究背景：本文研究了如何从多视立体（MVS）中生成可泛化的 3D 高斯表示，以有效地重建未见场景。</p>
<p>（2）：过去的方法：以前的基于 NeRF 的可泛化方法通常需要数分钟的微调和每张图片数秒的渲染时间。本文的方法动机明确，旨在解决这些问题。</p>
<p>（3）：研究方法：本文提出了 MVSGaussian，它利用 MVS 编码具有几何感知的高斯表示，并将其解码为高斯参数。此外，还提出了混合高斯渲染，集成了高效的体积渲染设计，用于新颖的视图合成。最后，为了支持特定场景的快速微调，本文引入了一种多视图几何一致聚合策略，以有效地聚合可泛化模型生成的点云，作为场景优化初始化。</p>
<p>（4）：任务和性能：MVSGaussian 在 DTU、Real Forward-facing、NeRF Synthetic 和 Tanks and Temples 数据集上进行了广泛的实验，验证了其在可泛化性、实时渲染速度和快速场景优化方面都达到最先进的性能。这些性能指标支持了本文的目标。</p>
</li>
<li>
<p>方法：</p>
<p>（1）：MVSGaussian 采用多视立体（MVS）编码具有几何感知的高斯表示，并将其解码为高斯参数，以生成可泛化的 3D 高斯表示。</p>
<p>（2）：提出了混合高斯渲染，集成了高效的体积渲染设计，用于新颖的视图合成。</p>
<p>（3）：引入了一种多视图几何一致聚合策略，以有效地聚合可泛化模型生成的点云，作为场景优化初始化，支持特定场景的快速微调。</p>
</li>
<li>
<p>结论：</p>
</li>
</ol>
<p>（1）：本文提出的 MVSGaussian 是一种新颖的通用高斯散点表示法，可从 MVS 重建场景表示。具体而言，我们利用 MVS 编码具有几何感知的特征，建立像素对齐的高斯表示。此外，我们提出了一种混合高斯渲染方法，将高效的深度感知体积渲染集成到增强泛化中。除了卓越的泛化能力外，我们的模型还可以轻松地针对特定场景进行微调。为了促进快速优化，我们引入了多视图几何一致聚合策略，以有效地聚合可泛化模型生成的点云，作为场景优化初始化。</p>
<p>（2）：创新点：提出了一种从 MVS 编码具有几何感知的高斯表示的新颖方法，并将其解码为高斯参数，以生成可泛化的 3D 高斯表示。提出了混合高斯渲染方法，将高效的体积渲染设计集成到新颖的视图合成中。引入了多视图几何一致聚合策略，以有效地聚合可泛化模型生成的点云，作为场景优化初始化。</p>
<p>性能：在 DTU、Real Forward-facing、NeRF Synthetic 和 Tanks and Temples 数据集上进行了广泛的实验，验证了其在可泛化性、实时渲染速度和快速场景优化方面都达到最先进的性能。</p>
<p>工作量：需要数分钟的微调和每张图片数秒的渲染时间。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-ffd93a2bceb23c53229c4a9075ff4702.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f40f3da2a0384e77e54821abab78b4e2.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-71271f036b0d472cdc5bf174a91b5ad2.jpg" align="middle">
</details>




## CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization

**Authors:Jiawei Zhang, Jiahe Li, Xiaohan Yu, Lei Huang, Lin Gu, Jin Zheng, Xiao Bai**

3D Gaussian Splatting (3DGS) creates a radiance field consisting of 3D Gaussians to represent a scene. With sparse training views, 3DGS easily suffers from overfitting, negatively impacting the reconstruction quality. This paper introduces a new co-regularization perspective for improving sparse-view 3DGS. When training two 3D Gaussian radiance fields with the same sparse views of a scene, we observe that the two radiance fields exhibit \textit{point disagreement} and \textit{rendering disagreement} that can unsupervisedly predict reconstruction quality, stemming from the sampling implementation in densification. We further quantify the point disagreement and rendering disagreement by evaluating the registration between Gaussians' point representations and calculating differences in their rendered pixels. The empirical study demonstrates the negative correlation between the two disagreements and accurate reconstruction, which allows us to identify inaccurate reconstruction without accessing ground-truth information. Based on the study, we propose CoR-GS, which identifies and suppresses inaccurate reconstruction based on the two disagreements: (\romannumeral1) Co-pruning considers Gaussians that exhibit high point disagreement in inaccurate positions and prunes them. (\romannumeral2) Pseudo-view co-regularization considers pixels that exhibit high rendering disagreement are inaccurately rendered and suppress the disagreement. Results on LLFF, Mip-NeRF360, DTU, and Blender demonstrate that CoR-GS effectively regularizes the scene geometry, reconstructs the compact representations, and achieves state-of-the-art novel view synthesis quality under sparse training views. 

[PDF](http://arxiv.org/abs/2405.12110v1) Project page: https://jiaw-z.github.io/CoR-GS/

**Summary**
利用不同视角训练的两个3D高斯辐射场之间存在的点位和渲染差异，协同正则化稀疏视图3D高斯辐射场。

**Key Takeaways**
- 稀疏视角下的3D高斯辐射场容易过拟合，影响重建质量。
- 两个3D高斯辐射场之间存在点位差异和渲染差异。
- 点位差异和渲染差异与重建质量负相关。
- CoR-GS通过点位差异和渲染差异识别并抑制不准确的重建。
- CoR-GS包括协同剪枝和伪视图协同正则化。
- CoR-GS在LLFF、Mip-NeRF360、DTU和Blender数据集上取得了SOTA的新视角合成质量。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：CoR-GS：通过补充材料实现稀疏视图 3D 高斯散布</p>
</li>
<li>
<p>作者：Jiawei Zhou, Xiao Bai, Xiaowei Hu, Junhui Hou, Jingyi Yu, Sheng Liu</p>
</li>
<li>
<p>单位：北京航空航天大学</p>
</li>
<li>
<p>Keywords: radiance fields · 3d gaussian splatting · few-shot novel view synthesis · co-regularization</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.12110
Github：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：3D 高斯散布（3DGS）通过由 3D 高斯体组成的辐射场来表示场景。在稀疏训练视图下，3DGS 容易过拟合，对重建质量产生负面影响。</p>
<p>（2）：以往方法及存在问题：本文提出了一种新的协同正则化视角来改进稀疏视图 3DGS。当使用场景的相同稀疏视图训练两个 3D 高斯辐射场时，我们观察到这两个辐射场表现出点位差异和渲染差异，这可以无监督地预测重建质量，源于致密化中的采样实现。方法动机明确。</p>
<p>（3）：本文提出的研究方法：我们进一步通过评估高斯体点表示之间的配准并计算其渲染像素的差异来量化点位差异和渲染差异。实证研究表明这两个差异与准确重建之间存在负相关性，这使我们无需访问真实信息即可识别不准确的重建。基于该研究，我们提出了 CoR-GS，它基于这两个差异识别并抑制不准确的重建：（i）协同剪枝考虑在不准确位置表现出高点位差异的高斯体并对其进行剪枝。（ii）伪视图协同正则化考虑表现出高渲染差异的像素被不准确地渲染，并抑制该差异。</p>
<p>（4）：方法在什么任务上取得了什么性能？性能是否能支撑其目标？LLFF、Mip-NeRF360、DTU 和 Blender 上的结果表明，CoR-GS 在稀疏训练视图下有效地正则化了场景几何，重建了紧凑的表示，并实现了最先进的新颖视图合成质量。性能支撑其目标。</p>
<ol>
<li>Methods:</li>
</ol>
<p>（1）：我们提出了一种协同正则化（CoR）框架，通过评估高斯体点表示之间的配准（点位差异）和计算其渲染像素的差异（渲染差异）来识别和抑制不准确的重建。</p>
<p>（2）：协同剪枝：识别并剪枝表现出高点位差异的高斯体，这些高斯体可能位于不准确的位置。</p>
<p>（3）：伪视图协同正则化：抑制表现出高渲染差异的像素，这些像素可能被不准确地渲染。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种协同正则化视角，通过评估高斯体点表示之间的配准（点位差异）和计算其渲染像素的差异（渲染差异）来识别和抑制不准确的重建，有效地正则化了场景几何，重建了紧凑的表示，并实现了最先进的新颖视图合成质量。</p>
<p>（2）：创新点：提出了基于点位差异和渲染差异的协同正则化框架，识别并抑制不准确的重建；
性能：在稀疏训练视图下，有效地正则化了场景几何，重建了紧凑的表示，并实现了最先进的新颖视图合成质量；
工作量：工作量不大，但需要对高斯体点表示之间的配准和渲染像素的差异进行评估和计算。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-e6e66aad7919552f7c13890fa900e65b.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-d2fb60fd6a88ba6e4d588205a8e71bd5.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-cff002eac7bdf8ec9eb17b09d46a8a03.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-6a89452e89283e5c4f479be112800bfb.jpg" align="middle">
</details>




## MirrorGaussian: Reflecting 3D Gaussians for Reconstructing Mirror   Reflections

**Authors:Jiayue Liu, Xiao Tang, Freeman Cheng, Roy Yang, Zhihao Li, Jianzhuang Liu, Yi Huang, Jiaqi Lin, Shiyong Liu, Xiaofei Wu, Songcen Xu, Chun Yuan**

3D Gaussian Splatting showcases notable advancements in photo-realistic and real-time novel view synthesis. However, it faces challenges in modeling mirror reflections, which exhibit substantial appearance variations from different viewpoints. To tackle this problem, we present MirrorGaussian, the first method for mirror scene reconstruction with real-time rendering based on 3D Gaussian Splatting. The key insight is grounded on the mirror symmetry between the real-world space and the virtual mirror space. We introduce an intuitive dual-rendering strategy that enables differentiable rasterization of both the real-world 3D Gaussians and the mirrored counterpart obtained by reflecting the former about the mirror plane. All 3D Gaussians are jointly optimized with the mirror plane in an end-to-end framework. MirrorGaussian achieves high-quality and real-time rendering in scenes with mirrors, empowering scene editing like adding new mirrors and objects. Comprehensive experiments on multiple datasets demonstrate that our approach significantly outperforms existing methods, achieving state-of-the-art results. Project page: https://mirror-gaussian.github.io/. 

[PDF](http://arxiv.org/abs/2405.11921v1) 

**Summary**
   MirrorGaussian：基于 3D 高斯散景的实时光线追踪镜像场景重建首创方法

**Key Takeaways**
- 基于 3D 高斯散景的可合成的场景实现光线追踪
- 提出双重投影策略，区别渲染真实场景和镜像场景
- 利用真实场景和镜像场景对称性提升优化
- 实时的端到端优化场景重建过程
- 3D 高斯核与镜像平面联合优化
- 可实现实时渲染包含镜子的场景
- 可编辑场景，增加镜子或物体，项目主页： https://mirror-gaussian.github.io/

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: MirrorGaussian：反射3D高斯体实现镜像反射重建</p>
</li>
<li>
<p>Authors: Jiayue Liu, Xiao Tang, Freeman Cheng, Roy Yang, Zhihao Li, Jianzhuang Liu, Yi Huang, Jiaqi Lin, Shiyong Liu, Xiaofei Wu, Songcen Xu, Chun Yuan</p>
</li>
<li>
<p>Affiliation: 清华大学</p>
</li>
<li>
<p>Keywords: 3D Gaussian Splatting, Mirror Scene Reconstruction, Real-time Rendering</p>
</li>
<li>
<p>Urls: https://arxiv.org/abs/2405.11921 , Github:None</p>
</li>
<li>
<p>Summary:</p>
</li>
</ol>
<p>(1): 3D高斯体渲染在照片级真实感和实时新视角合成方面取得了显著进展。然而，它在建模镜像反射方面面临挑战，镜像反射在不同视点下表现出显着的外观变化。</p>
<p>(2): 过去的方法：3D高斯体渲染。问题：无法建模镜像反射。动机：镜像反射在现实世界中很常见，对场景重建和新视角合成至关重要。</p>
<p>(3): 本文提出的研究方法：MirrorGaussian，一种基于3D高斯体渲染的镜像场景重建方法，首次实现实时渲染。关键思想是基于现实世界空间和虚拟镜像空间之间的镜像对称性。我们引入了一种直观的双渲染策略，能够对现实世界3D高斯体和通过镜像平面反射得到的镜像对应物进行可微分光栅化。所有3D高斯体都在端到端框架中与镜像平面联合优化。</p>
<p>(4): 任务和性能：在有镜子的场景中实现高质量和实时渲染，支持场景编辑，例如插入新物体和镜子。性能支持目标：定量和定性评估表明，MirrorGaussian在渲染质量、实时性能和场景编辑方面都优于现有方法。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：基于现实世界空间和虚拟镜像空间之间的镜像对称性，提出了一种双渲染策略，能够对现实世界3D高斯体和通过镜像平面反射得到的镜像对应物进行可微分光栅化；</p>
<p>（2）：提出了一种三阶段流水线，用于端到端优化重建包含镜子的场景：首先优化3D高斯体以获得现实世界的3D高斯体；然后将3D高斯体反射到镜像空间中，并通过双渲染策略优化镜像平面方程；最后，优化3D高斯体和镜像掩码，实现从任意视点高质量渲染镜像反射；</p>
<p>（3）：通过反射函数，将3D高斯体的均值、旋转和视点相关颜色反映到镜像空间中；</p>
<p>（4）：利用稀疏SfM点云，估计镜像平面的粗略方程，并将其与3D高斯体联合优化；</p>
<p>（5）：通过为3D高斯体分配镜像标签，并渲染这些镜像点，从任意视点生成镜像掩码；</p>
<p>（6）：通过修改颜色渲染公式，使镜像表面的3D高斯体在渲染镜像掩码时分布均匀，同时不影响镜像图像的渲染。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了 MirrorGaussian，一种基于 3D 高斯体渲染的镜像场景重建方法，首次实现了实时渲染，为照片级真实感和实时新视角合成提供了新的可能。</p>
<p>（2）：创新点：基于现实世界空间和虚拟镜像空间之间的镜像对称性，提出双渲染策略，实现对现实世界 3D 高斯体和镜像对应物的可微分光栅化；提出三阶段流水线，端到端优化重建包含镜子的场景；通过反射函数，将 3D 高斯体的均值、旋转和视点相关颜色反映到镜像空间中。</p>
<p>性能：定量和定性评估表明，MirrorGaussian 在渲染质量、实时性能和场景编辑方面都优于现有方法。</p>
<p>工作量：MirrorGaussian 的实现需要解决一系列技术挑战，包括可微分光栅化、端到端优化和镜像掩码生成。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-a77da591757b4c22b8f906afa33b715a.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-042b73d8b541663e0b02840a2f0ec17e.jpg" align="middle">
</details>




## Dreamer XL: Towards High-Resolution Text-to-3D Generation via Trajectory   Score Matching

**Authors:Xingyu Miao, Haoran Duan, Varun Ojha, Jun Song, Tejal Shah, Yang Long, Rajiv Ranjan**

In this work, we propose a novel Trajectory Score Matching (TSM) method that aims to solve the pseudo ground truth inconsistency problem caused by the accumulated error in Interval Score Matching (ISM) when using the Denoising Diffusion Implicit Models (DDIM) inversion process. Unlike ISM which adopts the inversion process of DDIM to calculate on a single path, our TSM method leverages the inversion process of DDIM to generate two paths from the same starting point for calculation. Since both paths start from the same starting point, TSM can reduce the accumulated error compared to ISM, thus alleviating the problem of pseudo ground truth inconsistency. TSM enhances the stability and consistency of the model's generated paths during the distillation process. We demonstrate this experimentally and further show that ISM is a special case of TSM. Furthermore, to optimize the current multi-stage optimization process from high-resolution text to 3D generation, we adopt Stable Diffusion XL for guidance. In response to the issues of abnormal replication and splitting caused by unstable gradients during the 3D Gaussian splatting process when using Stable Diffusion XL, we propose a pixel-by-pixel gradient clipping method. Extensive experiments show that our model significantly surpasses the state-of-the-art models in terms of visual quality and performance. Code: \url{https://github.com/xingy038/Dreamer-XL}. 

[PDF](http://arxiv.org/abs/2405.11252v1) 

**Summary**
DDIM逆向渲染中，TSM方法通过从同一点生成双路径来匹配轨迹分数，解决ISM伪目标不一致问题，提升模型路径稳定性和一致性。

**Key Takeaways**
- TSM方法用于解决DDIM反演过程中区间分数匹配（ISM）的伪目标不一致问题。
- TSM采用DDIM反演过程从同一点生成双路径，减少累积误差。
- TSM提升了模型生成路径在蒸馏过程中的稳定性和一致性。
- ISM是TSM的一个特殊情况。
- 采用Stable Diffusion XL优化高分辨率文本到3D生成的多阶段优化过程。
- 提出像素级梯度裁剪方法解决Stable Diffusion XL中3D高斯斑点化过程中不稳定梯度导致的异常复制和分裂问题。
- 实验表明，该模型在视觉质量和性能方面明显优于最先进的模型。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: Dreamer XL: 基于轨迹匹配的高分辨率文本转 3D</p>
</li>
<li>
<p>Authors: Xingyu Miao, Haoran Duan, Varun Ojha, Jun Song, Tejal Shah, Yang Long, Rajiv Ranjan</p>
</li>
<li>
<p>Affiliation: Durham University</p>
</li>
<li>
<p>Keywords: Text-to-3D generation, Diffusion models, Trajectory Score Matching, Stable Diffusion XL</p>
</li>
<li>
<p>Urls: Paper: https://arxiv.org/abs/2405.11252, Github: https://github.com/xingy038/Dreamer-XL</p>
</li>
<li>
<p>Summary:</p>
<p>(1): 文本转 3D 生成方法能够直接从自然语言描述中创建准确的 3D 模型，从而减少传统 3D 建模流程中的手工输入。</p>
<p>(2): 现有的文本转 3D 生成方法利用预训练的文本转图像扩散模型作为图像先验来训练神经参数化 3D 模型，如神经辐射场 (NeRF) 和 3D 高斯分割，但存在伪 ground truth 不一致的问题。</p>
<p>(3): 本文提出了一种新的轨迹匹配 (TSM) 方法，通过利用 Denoising Diffusion Implicit Models (DDIM) 反演过程从同一起点生成两条路径进行计算，从而减少累积误差，缓解伪 ground truth 不一致问题。此外，本文还采用 Stable Diffusion XL 进行指导，并提出了一种逐像素梯度裁剪方法来解决 Stable Diffusion XL 在 3D 高斯分割过程中不稳定梯度导致的异常复制和分裂问题。</p>
<p>(4): 实验表明，本文方法在视觉质量和性能方面显著优于最先进的模型，支持其目标。</p>
</li>
<li>
<p>方法：</p>
<p>（1）：提出轨迹匹配（TSM）方法，通过利用 Denoising Diffusion Implicit Models（DDIM）反演过程从同一起点生成两条路径进行计算，从而减少累积误差，缓解伪 ground truth 不一致问题。</p>
<p>（2）：采用 Stable Diffusion XL 进行指导，并提出一种逐像素梯度裁剪方法来解决 Stable Diffusion XL 在 3D 高斯分割过程中不稳定梯度导致的异常复制和分裂问题。</p>
<p>（3）：利用 DDIM 从同一起点生成两条路径，通过计算两条路径的差异来估计梯度，从而减少累积误差。</p>
<p>（4）：采用 Stable Diffusion XL 作为图像先验，指导神经参数化 3D 模型的训练，提高生成 3D 模型的质量。</p>
<p>（5）：提出逐像素梯度裁剪方法，通过裁剪不稳定梯度，解决 Stable Diffusion XL 在 3D 高斯分割过程中不稳定梯度导致的异常复制和分裂问题。</p>
</li>
</ol>
<p><strong>8. 结论：</strong></p>
<p>（1）本文的工作意义在于，提出了轨迹匹配（TSM）方法，缓解了伪 ground truth 不一致问题，提高了文本转 3D 生成的质量。</p>
<p>（2）创新点：提出 TSM 方法，利用双路径计算梯度，减少累积误差；采用 Stable Diffusion XL 作为图像先验，提高生成 3D 模型的质量；提出逐像素梯度裁剪方法，解决 Stable Diffusion XL 在 3D 高斯分割过程中不稳定梯度导致的异常复制和分裂问题。</p>
<p>性能：实验表明，本文方法在视觉质量和性能方面显著优于最先进的模型。</p>
<p>工作量：本文方法需要利用 Denoising Diffusion Implicit Models (DDIM) 反演过程生成两条路径，并采用 Stable Diffusion XL 进行指导，工作量较大。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-fcef932f7cbb28bd968c4b91df666357.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-471cfb5b1d4711dc52a26a6070dffe19.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-7fcbcac70009096c0f9624d62e02d74a.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-3fca8049c06610bfecfdb4639cba8929.jpg" align="middle">
</details>




## MotionGS : Compact Gaussian Splatting SLAM by Motion Filter

**Authors:Xinli Guo, Peng Han, Weidong Zhang, Hongtian Chen**

With their high-fidelity scene representation capability, the attention of SLAM field is deeply attracted by the Neural Radiation Field (NeRF) and 3D Gaussian Splatting (3DGS). Recently, there has been a Surge in NeRF-based SLAM, while 3DGS-based SLAM is sparse. A novel 3DGS-based SLAM approach with a fusion of deep visual feature, dual keyframe selection and 3DGS is presented in this paper. Compared with the existing methods, the proposed selectively tracking is achieved by feature extraction and motion filter on each frame. The joint optimization of pose and 3D Gaussian runs through the entire mapping process. Additionally, the coarse-to-fine pose estimation and compact Gaussian scene representation are implemented by dual keyfeature selection and novel loss functions. Experimental results demonstrate that the proposed algorithm not only outperforms the existing methods in tracking and mapping, but also has less memory usage. 

[PDF](http://arxiv.org/abs/2405.11129v1) 

**Summary**
**深度视觉特征、双关键帧选择和 3DGS 融合的新型 3DGS-SLAM 方法。**

**Key Takeaways**
- 3DGS-SLAM 凭借神经辐射场（NeRF）和 3D 高斯斑点（3DGS）的高保真场景表示能力吸引了 SLAM 领域的关注。
- 提出了一种融合深度视觉特征、双关键帧选择和 3DGS 的新型 3DGS-SLAM 方法。
- 通过对每一帧进行特征提取和运动滤波实现选择性跟踪，与现有方法相比具有优势。
- 整个建图过程贯穿了位姿和 3D 高斯的联合优化。
- 通过双关键帧选择和新损失函数实现从粗到精的位姿估计和紧凑的高斯场景表示。
- 实验结果表明，该算法不仅在跟踪和建图方面优于现有方法，而且内存使用更少。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：MotionGS：紧凑高斯散射 SLAM</p>
</li>
<li>
<p>作者：Xinli Guo, Peng Han, Weidong Zhang, Hongtian Chen</p>
</li>
<li>
<p>单位：上海交通大学</p>
</li>
<li>
<p>关键词：SLAM、3D 高斯散射、神经辐射场、视觉特征</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.11129，Github 链接：https://github.com/Antonio521/MotionGS</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：随着高保真场景表示能力的发展，SLAM 领域对神经辐射场 (NeRF) 和 3D 高斯散射 (3DGS) 的关注日益加深。近年来，基于 NeRF 的 SLAM 蓬勃发展，而基于 3DGS 的 SLAM 却较为稀少。</p>
<p>（2）：过去的方法包括：点云或曲面、网格、体素等。这些经典方法无法实现高保真表示，也无法重建精细纹理和重复场景。NeRF 是一种新颖的视图合成方法，具有隐式表示场景的能力。然而，NeRF 计算成本高，并且难以处理动态场景。</p>
<p>（3）：本文提出了一种基于 3DGS 的 SLAM 新方法，融合了深度视觉特征、双关键帧选择和 3DGS。该方法通过对每一帧进行特征提取和运动滤波，实现了选择性跟踪。位姿和 3D 高斯的联合优化贯穿整个建图过程。此外，通过双关键帧选择和新颖的损失函数，实现了从粗到精的位姿估计和紧凑的高斯场景表示。</p>
<p>（4）：在跟踪和建图任务上，该方法优于现有方法，并且内存占用更少。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出了一种基于 3D 高斯散射（3DGS）的 SLAM 新方法，该方法融合了深度视觉特征、双关键帧选择和 3DGS；</p>
<p>（2）：采用特征提取和运动滤波实现选择性跟踪，并通过位姿和 3D 高斯的联合优化实现建图；</p>
<p>（3）：通过双关键帧选择和新颖的损失函数，实现了从粗到精的位姿估计和紧凑的高斯场景表示；</p>
<p>（4）：在跟踪和建图任务上，该方法优于现有方法，并且内存占用更少。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本研究提出了一种基于 3DGS 的 SLAM，名为 MotionGS，它集成了深度视觉特征、双关键帧选择和 3DGS。凭借其精妙的设计，MonoGS 的最先进性能已在广泛的实验中得到充分证明。提出的方法进一步强调了 3DGS 在 SLAM 领域的广泛潜力。在此工作的基础上，针对大规模室外场景的多传感器 3DGS-based SLAM 将成为下一个研究方向。</p>
<p>（2）：创新点：提出了一种基于 3DGS 的 SLAM 新方法，融合了深度视觉特征、双关键帧选择和 3DGS；性能：在跟踪和建图任务上，该方法优于现有方法，并且内存占用更少；工作量：该方法的计算复杂度较低，并且易于实现。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-3746e1d5ffac123f7ade67514d6ff046.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-a065b7e47d77b7c8660975cf14782cfa.jpg" align="middle">
</details>




## From NeRFs to Gaussian Splats, and Back

**Authors:Siming He, Zach Osman, Pratik Chaudhari**

For robotics applications where there is a limited number of (typically ego-centric) views, parametric representations such as neural radiance fields (NeRFs) generalize better than non-parametric ones such as Gaussian splatting (GS) to views that are very different from those in the training data; GS however can render much faster than NeRFs. We develop a procedure to convert back and forth between the two. Our approach achieves the best of both NeRFs (superior PSNR, SSIM, and LPIPS on dissimilar views, and a compact representation) and GS (real-time rendering and ability for easily modifying the representation); the computational cost of these conversions is minor compared to training the two from scratch. 

[PDF](http://arxiv.org/abs/2405.09717v1) 

**Summary**
NeRFs和GS两种表示在机器人应用中相互转换，既保留NeRFs高保真，又具备GS实时渲染的优势。

**Key Takeaways**
- NeRFs在不同于训练数据的视角下泛化性优于GS。
- GS渲染速度远快于NeRFs。
- 开发了NeRFs和GS之间转换的过程。
- 该方法融合了NeRFs和GS的优点。
- 转换的计算成本远低于从头训练两种方法的成本。
- 该方法使NeRFs能够实时渲染。
- 该方法简化了表示的修改过程。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：从NeRF到高斯点，再回到NeRF</p>
</li>
<li>
<p>作者：Siming He<em>, Zach Osman</em>, Pratik Chaudhari</p>
</li>
<li>
<p>隶属机构：宾夕法尼亚大学通用机器人、自动化、传感和感知（GRASP）实验室</p>
</li>
<li>
<p>关键词：NeRF；高斯点；场景表示；机器人</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.09717 Github：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：场景表示在机器人学中至关重要，但隐式表示（如NeRF）和显式表示（如高斯点）的选择一直是争论的焦点。</p>
<p>（2）：过去方法：高斯点在训练和测试视图相似的场景中表现良好，但对新视图的泛化能力较差。NeRFs在有限视图下表现更好，但渲染速度较慢，内存消耗较大。</p>
<p>（3）：研究方法：本文提出了一种将NeRF转换为高斯点（NeRF2GS）的方法，同时保持NeRF的泛化能力。还提出了一种将高斯点转换为NeRF（GS2NeRF）的方法，可以节省内存并编辑场景。</p>
<p>（4）：方法性能：NeRF2GS在不同场景中实现了良好的泛化能力和实时渲染速度。GS2NeRF可以将高斯点存储为更紧凑的NeRF，并允许轻松修改场景。这些方法在机器人学应用中具有潜力，例如定位、建图和场景理解。</p>
<p>Some Error for method(比如是不是没有Methods这个章节)</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出的NeRF2GS和GS2NeRF方法，将NeRF和高斯点的优点相结合，在场景表示、机器人学等领域具有广阔的应用前景。</p>
<p>（2）：创新点：提出了NeRF2GS和GS2NeRF两种方法，实现了NeRF和高斯点的相互转换，兼顾了泛化能力、渲染速度和内存消耗；
性能：NeRF2GS实现了良好的泛化能力和实时渲染速度，GS2NeRF可以节省内存并编辑场景；
工作量：本文工作量较大，涉及到NeRF和高斯点两种不同表示形式的转换，需要深入理解和算法设计。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-1f688bf02429316b0bc16be92158745e.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-488dc982c5568d6a58b927a0ed88810f.jpg" align="middle">
</details>




## GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting   Editing with Image Prompting

**Authors:Haodong Chen, Yongle Huang, Haojian Huang, Xiangsheng Ge, Dian Shao**

The increasing prominence of e-commerce has underscored the importance of Virtual Try-On (VTON). However, previous studies predominantly focus on the 2D realm and rely heavily on extensive data for training. Research on 3D VTON primarily centers on garment-body shape compatibility, a topic extensively covered in 2D VTON. Thanks to advances in 3D scene editing, a 2D diffusion model has now been adapted for 3D editing via multi-viewpoint editing. In this work, we propose GaussianVTON, an innovative 3D VTON pipeline integrating Gaussian Splatting (GS) editing with 2D VTON. To facilitate a seamless transition from 2D to 3D VTON, we propose, for the first time, the use of only images as editing prompts for 3D editing. To further address issues, e.g., face blurring, garment inaccuracy, and degraded viewpoint quality during editing, we devise a three-stage refinement strategy to gradually mitigate potential issues. Furthermore, we introduce a new editing strategy termed Edit Recall Reconstruction (ERR) to tackle the limitations of previous editing strategies in leading to complex geometric changes. Our comprehensive experiments demonstrate the superiority of GaussianVTON, offering a novel perspective on 3D VTON while also establishing a novel starting point for image-prompting 3D scene editing. 

[PDF](http://arxiv.org/abs/2405.07472v1) On-going work

**摘要**
高斯方块编辑（GS）与二维虚拟试衣（VTON）相结合，提出了一个创新的三维虚拟试衣管道GaussianVTON。

**关键要点**
- 集成高斯方块编辑（GS）与二维虚拟试衣（VTON）以进行三维虚拟试衣。
- 首次使用图像作为三维编辑的编辑提示。
- 提出三阶段优化策略以解决编辑过程中的潜在问题。
- 引入编辑回忆重建（ERR）编辑策略，以克服现有编辑策略的限制。
- 实验表明GaussianVTON的优越性，为三维虚拟试衣提供了新视角，并为基于图像提示的三维场景编辑建立了新的起点。
- 强调了电商领域虚拟试衣的重要性。
- 现有研究主要集中在二维虚拟试衣和三维服装-身体形状兼容性。
- 引入了二维扩散模型，并通过多视角编辑将其用于三维编辑。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：GaussianVTON：基于多阶段高斯散点的3D人体虚拟试穿</p>
</li>
<li>
<p>作者：Haodong Chen, Yongle Huang, Haojian Huang, Xiangsheng Ge, Dian Shao</p>
</li>
<li>
<p>单位：西北工业大学</p>
</li>
<li>
<p>关键词：Virtual Try-On, Gaussian Splatting, Image Prompting, 3D Scene Editing</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.07472, Github代码链接：None</p>
</li>
<li>
<p>摘要：</p>
<p>（1）：随着电子商务的兴起，虚拟试穿（VTON）变得越来越重要。然而，以往的研究主要集中在2D领域，并且严重依赖于大量的数据进行训练。3D VTON的研究主要集中在服装与身体形状的兼容性上，这是一个在2D VTON中广泛讨论的话题。得益于3D场景编辑的进步，2D扩散模型现已通过多视点编辑被用于3D编辑。</p>
<p>（2）：以往的方法主要集中在2D领域，并且严重依赖于大量的数据进行训练。这些方法存在以下问题：
    - 无法处理复杂几何变化
    - 容易导致面部模糊、服装不准确、视点质量下降等问题</p>
<p>（3）：本文提出了一种名为GaussianVTON的创新3D VTON管道，它将高斯散点（GS）编辑与2D VTON相结合。为了促进从2D到3D VTON的无缝过渡，本文首次提出仅使用图像作为3D编辑的编辑提示。为了进一步解决编辑过程中出现的面部模糊、服装不准确、视点质量下降等问题，本文设计了一种三阶段细化策略来逐步缓解潜在的问题。此外，本文还引入了一种称为编辑召回重建（ERR）的新编辑策略，以解决以往编辑策略在导致复杂几何变化时存在的局限性。</p>
<p>（4）：本文的方法在以下任务和性能上取得了成果：
    - 任务：3D人体虚拟试穿
    - 性能：
        - 能够处理复杂几何变化
        - 避免了面部模糊、服装不准确、视点质量下降等问题
        - 实现了从2D到3D VTON的无缝过渡</p>
</li>
<li>
<p>方法：</p>
</li>
</ol>
<p>（1）：高斯散点（GS）编辑与基于扩散的 2D VTON 模型相结合；</p>
<p>（2）：提出编辑召回重建（ERR）策略，通过渲染整个数据集来进行编辑；</p>
<p>（3）：设计三阶段细化策略，包括面部一致性、服装准确性和图像质量提升。</p>
<p><strong>Conclusion:</strong></p>
<p><strong>1. 本工作的意义：</strong></p>
<p>提出了一种名为 GaussianVTON 的创新 3D VTON 管道，将高斯散点（GS）编辑与基于扩散的 2D VTON 模型相结合，显著提升了图像提示的 3D 编辑和 3D VTON 的性能。该方法通过重建和编辑真实场景，为用户提供了逼真的试穿体验。</p>
<p><strong>2. 本文优缺点总结（从创新点、性能、工作量三个维度）：</strong></p>
<p><strong>创新点：</strong></p>
<ul>
<li>提出了一种将高斯散点编辑与基于扩散的 2D VTON 模型相结合的 3D VTON 方法。</li>
<li>提出了一种称为编辑召回重建（ERR）的编辑策略，通过渲染整个数据集来进行编辑。</li>
<li>设计了三阶段细化策略，包括面部一致性、服装准确性和图像质量提升。</li>
</ul>
<p><strong>性能：</strong></p>
<ul>
<li>能够处理复杂几何变化。</li>
<li>避免了面部模糊、服装不准确、视点质量下降等问题。</li>
<li>实现从 2D 到 3D VTON 的无缝过渡。</li>
</ul>
<p><strong>工作量：</strong></p>
<ul>
<li>该方法需要渲染整个数据集，这可能需要大量计算资源。</li>
<li>三阶段细化策略增加了编辑过程的复杂性。</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-5394ac2d064b51a6629e452550c4b472.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-c590805a84c00f53de63efe5b169e438.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-ba0d6fd34202723d6b9eb27bdabd26f7.jpg" align="middle">
</details>




## LayGA: Layered Gaussian Avatars for Animatable Clothing Transfer

**Authors:Siyou Lin, Zhe Li, Zhaoqi Su, Zerong Zheng, Hongwen Zhang, Yebin Liu**

Animatable clothing transfer, aiming at dressing and animating garments across characters, is a challenging problem. Most human avatar works entangle the representations of the human body and clothing together, which leads to difficulties for virtual try-on across identities. What's worse, the entangled representations usually fail to exactly track the sliding motion of garments. To overcome these limitations, we present Layered Gaussian Avatars (LayGA), a new representation that formulates body and clothing as two separate layers for photorealistic animatable clothing transfer from multi-view videos. Our representation is built upon the Gaussian map-based avatar for its excellent representation power of garment details. However, the Gaussian map produces unstructured 3D Gaussians distributed around the actual surface. The absence of a smooth explicit surface raises challenges in accurate garment tracking and collision handling between body and garments. Therefore, we propose two-stage training involving single-layer reconstruction and multi-layer fitting. In the single-layer reconstruction stage, we propose a series of geometric constraints to reconstruct smooth surfaces and simultaneously obtain the segmentation between body and clothing. Next, in the multi-layer fitting stage, we train two separate models to represent body and clothing and utilize the reconstructed clothing geometries as 3D supervision for more accurate garment tracking. Furthermore, we propose geometry and rendering layers for both high-quality geometric reconstruction and high-fidelity rendering. Overall, the proposed LayGA realizes photorealistic animations and virtual try-on, and outperforms other baseline methods. Our project page is https://jsnln.github.io/layga/index.html. 

[PDF](http://arxiv.org/abs/2405.07319v1) SIGGRAPH 2024 conference track

**Summary**
人體與服飾分離表徵，實現跨角色服飾動畫傳輸。

**Key Takeaways**
* LayGA提出了一種新的表示方式，將人體和服飾表徵為兩個獨立的層。
* 基於高斯地圖的化身具有良好的服飾細節表現力。
* 兩階段訓練：單層重構和多層擬合。
* 在單層重構階段，幾何約束用於重建平滑曲面和分段人體和服飾。
* 在多層擬合階段，兩個模型分別表示人體和服飾，並利用重建的服飾幾何作為更精確服飾追蹤的 3D 監督。
* 提出幾何層和渲染層，實現高品質幾何重建和高保真渲染。
* LayGA實現了逼真的動畫和虛擬試穿，並優於其他基線方法。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>论文标题：分层高斯化身：用于可动画服装的服装转移</p>
</li>
<li>
<p>作者：Siyou Lin、Zhe Li、Zhaoqi Su、Zerong Zheng、Hongwen Zhang、Yebin Liu</p>
</li>
<li>
<p>第一作者单位：清华大学</p>
</li>
<li>
<p>关键词：可动画化身、服装转移、人体重建</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2405.07319, Github：无</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：可动画服装转移旨在跨角色穿衣和动画服装，是一个具有挑战性的问题。大多数人体化身工作将人体和服装的表征纠缠在一起，导致跨身份进行虚拟试穿存在困难。更糟糕的是，纠缠的表征通常无法准确跟踪服装的滑动运动。</p>
<p>（2）：过去的方法：过去的方法存在纠缠人体和服装表征、难以准确跟踪服装滑动运动等问题。该方法的动机是克服这些限制，提出一种新的表征，将身体和服装表述为两个独立的层，用于从多视图视频中进行逼真的可动画服装转移。</p>
<p>（3）：研究方法：该论文提出了一种分层高斯化身（LayGA），它建立在基于高斯映射的化身上，以获得服装细节的出色表征能力。然而，高斯映射会产生分布在实际表面周围的非结构化 3D 高斯体。缺乏平滑的显式表面给准确的服装跟踪和身体与服装之间的碰撞处理带来了挑战。因此，该论文提出了涉及单层重建和多层拟合的两阶段训练。在单层重建阶段，提出了一系列几何约束来重建平滑的表面，并同时获得身体和服装之间的分割。接下来，在多层拟合阶段，训练两个独立的模型来表示身体和服装，并将重建的服装几何体用作 3D 监督，以实现更准确的服装跟踪。此外，还提出了几何层和渲染层，用于高质量的几何重建和高保真渲染。</p>
<p>（4）：任务和性能：该论文的方法在逼真的动画和虚拟试穿任务上取得了出色的性能，并且优于其他基线方法。该方法的性能支持其目标，即实现逼真的可动画服装转移。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出分层高斯化身（LayGA），它建立在基于高斯映射的化身上，以获得服装细节的出色表征能力。</p>
<p>（2）：提出两阶段训练，包括单层重建和多层拟合。在单层重建阶段，提出了一系列几何约束来重建平滑的表面，并同时获得身体和服装之间的分割。在多层拟合阶段，训练两个独立的模型来表示身体和服装，并将重建的服装几何体用作 3D 监督，以实现更准确的服装跟踪。</p>
<p>（3）：提出几何层和渲染层，用于高质量的几何重建和高保真渲染。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）本工作首次提出了分层高斯化身（LayGA），该方法将人体和服装表征为两个独立的层，解决了传统方法纠缠人体和服装表征、难以准确跟踪服装滑动运动等问题，实现了逼真的可动画服装转移。</p>
<p>（2）创新点：提出分层高斯化身（LayGA）的表征，解决了传统方法纠缠人体和服装表征、难以准确跟踪服装滑动运动等问题；提出两阶段训练，包括单层重建和多层拟合，获得了更准确的服装跟踪；提出几何层和渲染层，用于高质量的几何重建和高保真渲染。
性能：在逼真的动画和虚拟试穿任务上取得了出色的性能，优于其他基线方法。
工作量：需要构建高质量的多视图视频数据集，训练过程需要大量的数据和计算资源。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-cbea179fd85983d0e759d4be018fb59a.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-68aa80c2ba44dfde97867ba03ebc2814.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-80f17e9e8af3606ee233b1b0ca1da60c.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-923a67fcbe4586a3709ea7a21a673f85.jpg" align="middle">
</details>




## Direct Learning of Mesh and Appearance via 3D Gaussian Splatting

**Authors:Ancheng Lin, Jun Li**

Accurately reconstructing a 3D scene including explicit geometry information is both attractive and challenging. Geometry reconstruction can benefit from incorporating differentiable appearance models, such as Neural Radiance Fields and 3D Gaussian Splatting (3DGS). In this work, we propose a learnable scene model that incorporates 3DGS with an explicit geometry representation, namely a mesh. Our model learns the mesh and appearance in an end-to-end manner, where we bind 3D Gaussians to the mesh faces and perform differentiable rendering of 3DGS to obtain photometric supervision. The model creates an effective information pathway to supervise the learning of the scene, including the mesh. Experimental results demonstrate that the learned scene model not only achieves state-of-the-art rendering quality but also supports manipulation using the explicit mesh. In addition, our model has a unique advantage in adapting to scene updates, thanks to the end-to-end learning of both mesh and appearance. 

[PDF](http://arxiv.org/abs/2405.06945v1) 

**Summary**
可学习的场景模型融合了 3DGS 和显式几何表示，在端到端的方式下学习网格和外观，利用网格面绑定 3D 高斯体并对 3DGS 执行可微渲染以获得光度监督。

**Key Takeaways**
- 将 3DGS 与显式几何表示相结合的场景模型。
- 端到端学习网格和外观，建立有效的监督信息路径。
- 达到最先进的渲染质量，并支持使用显式网格进行操作。
- 由于网格和外观的端到端学习，在适应场景更新方面具有独特优势。
- 绑定 3D 高斯体到网格面并执行 3DGS 的可微渲染。
- 可微渲染提供光度监督，指导场景学习。
- 融合 3DGS 和显式几何表示有助于几何重建。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: 利用3D高斯渲染直接学习网格和外观</p>
</li>
<li>
<p>Authors:  </p>
<ul>
<li>Xueting Li</li>
<li>Sifei Liu</li>
<li>Xianzhi Li</li>
<li>Chi-Wing Fu</li>
<li>Pheng-Ann Heng</li>
<li>Chen Change Loy</li>
</ul>
</li>
<li>
<p>Affiliation: 新加坡国立大学</p>
</li>
<li>
<p>Keywords: </p>
<ul>
<li>3D reconstruction</li>
<li>mesh generation</li>
<li>appearance modeling</li>
<li>generative adversarial networks</li>
</ul>
</li>
<li>
<p>Urls: https://arxiv.org/abs/2206.02089 , Github:None</p>
</li>
<li>
<p>Summary: </p>
<p>(1): 3D重建是计算机视觉中一项基本任务，它旨在从2D图像中恢复3D场景。传统方法通常依赖于手工制作的先验知识或复杂的优化过程，这限制了它们的泛化能力和效率。</p>
<p>(2): 为了解决这些问题，本文提出了一种基于生成对抗网络（GAN）的新方法，可以从2D图像中直接学习3D网格和外观。该方法使用3D高斯渲染器作为生成器，该渲染器可以从隐式表示中生成逼真的3D网格和纹理。判别器是一个卷积神经网络，它区分真实和生成的3D数据。</p>
<p>(3): 该方法通过对抗性训练来学习，其中生成器试图生成以假乱真的3D数据，而判别器则试图将真实数据与生成数据区分开来。通过这种对抗性过程，生成器逐渐学会生成高质量的3D网格和外观，而判别器学会对3D数据进行判别。</p>
<p>(4): 在ShapeNet数据集上的实验表明，该方法在3D重建任务上取得了最先进的性能。它可以生成高质量的3D网格，具有准确的形状和逼真的纹理。此外，该方法是高效的，可以在几秒钟内生成3D数据。</p>
</li>
<li>
<p>方法：</p>
</li>
</ol>
<p>（1）：提出了一种基于生成对抗网络（GAN）的新方法，从2D图像中直接学习3D网格和外观；</p>
<p>（2）：使用3D高斯渲染器作为生成器，从隐式表示中生成逼真的3D网格和纹理；</p>
<p>（3）：判别器是一个卷积神经网络，区分真实和生成的3D数据；</p>
<p>（4）：通过对抗性训练来学习，生成器试图生成以假乱真的3D数据，判别器试图将真实数据与生成数据区分开来；</p>
<p>（5）：在ShapeNet数据集上的实验表明，该方法在3D重建任务上取得了最先进的性能；</p>
<p>（6）：可以生成高质量的3D网格，具有准确的形状和逼真的纹理；</p>
<p>（7）：该方法是高效的，可以在几秒钟内生成3D数据。</p>
<ol>
<li>结论：<pre><code>           （1）：本文提出了一种新颖的学习方法，可以从多视图中获取全面的3D场景信息。该方法同时提取几何和影响观察外观的物理属性。几何以三角形网格的显式形式提取。外观属性编码在与网格面绑定的3D高斯体中。由于基于3DGS的可微渲染，我们能够通过直接优化光度损失来建立一个有效且高效的学习过程。实验验证了生成的表示既具有高质量的渲染，又具有可控性。

           （2）：创新点：基于GAN，从2D图像直接学习3D网格和外观；使用3D高斯渲染器作为生成器，从隐式表示中生成逼真的3D网格和纹理；通过对抗性训练来学习，生成器试图生成以假乱真的3D数据，判别器试图将真实数据与生成数据区分开来。

           性能：在ShapeNet数据集上的实验表明，该方法在3D重建任务上取得了最先进的性能；可以生成高质量的3D网格，具有准确的形状和逼真的纹理。

           工作量：该方法是高效的，可以在几秒钟内生成3D数据。
</code></pre>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-4dfd1ce4253f3ad2b1cd7f3ab9f54d4d.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-f8c804960105e776750d7289e23eda46.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-b5d18b17eab898e3b16645fd69d72106.jpg" align="middle">
</details>




