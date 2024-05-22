
---
title: 3DGS
date: 2024-04-09 16:23:53
author: Kedreamix
cover: https://pic1.zhimg.com/v2-547f5a57e280ecd60e9f1e905a13c71d.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-04-09  Robust Gaussian Splatting  
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

# 2024-04-09 更新


## Robust Gaussian Splatting

**Authors:François Darmon, Lorenzo Porzi, Samuel Rota-Bulò, Peter Kontschieder**

In this paper, we address common error sources for 3D Gaussian Splatting (3DGS) including blur, imperfect camera poses, and color inconsistencies, with the goal of improving its robustness for practical applications like reconstructions from handheld phone captures. Our main contribution involves modeling motion blur as a Gaussian distribution over camera poses, allowing us to address both camera pose refinement and motion blur correction in a unified way. Additionally, we propose mechanisms for defocus blur compensation and for addressing color in-consistencies caused by ambient light, shadows, or due to camera-related factors like varying white balancing settings. Our proposed solutions integrate in a seamless way with the 3DGS formulation while maintaining its benefits in terms of training efficiency and rendering speed. We experimentally validate our contributions on relevant benchmark datasets including Scannet++ and Deblur-NeRF, obtaining state-of-the-art results and thus consistent improvements over relevant baselines. 

[PDF](http://arxiv.org/abs/2404.04211v1) 

**Summary**
3D高斯体素渲染（3DGS）的通用错误源建模及其在实际应用中的鲁棒性提升。

**Key Takeaways**
- 将运动模糊建模为相机位姿上的高斯分布，统一处理相机位姿优化和运动模糊校正。
- 提出散焦模糊补偿和解决由于环境光、阴影或与相机相关的因素（如白平衡设置变化）导致的颜色不一致的机制。
- 提出的解决方案与 3DGS 公式无缝集成，同时保持其在训练效率和渲染速度方面的优势。
- 在 Scannet++ 和 Deblur-NeRF 等相关基准数据集上通过实验证明了我们的贡献，获得了最先进的结果，并始终如一地改进了相关基准。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：鲁棒高斯溅射</li>
<li>作者：François Darmon, Lorenzo Porzi, Samuel Rota-Bulò, Peter Kontschieder</li>
<li>隶属：Meta Reality Labs 苏黎世</li>
<li>关键词：3D 高斯溅射、位姿优化、运动模糊</li>
<li>链接：arxiv.org/abs/2404.04…</li>
<li>摘要：
(1) 研究背景：3D 高斯溅射 (3DGS) 是一种用于从图像重建 3D 场景的有效技术。然而，它容易受到模糊、不完美的相机位姿和颜色不一致等常见错误源的影响。
(2) 过去的方法：现有的方法通常分别处理这些错误源，这可能会导致次优结果。
(3) 本文提出的研究方法：本文提出了一种统一的框架，将运动模糊建模为相机位姿上的高斯分布，从而同时解决相机位姿优化和运动模糊校正问题。此外，还提出了针对散焦模糊补偿和解决由环境光、阴影或相机相关因素（如白平衡设置不同）引起的颜色不一致的机制。
(4) 任务和性能：在 Scannet++ 和 Deblur-NeRF 等基准数据集上进行的实验验证了本文方法的有效性，获得了最先进的结果，并对相关基准线进行了持续的改进。这些结果支持了本文的目标，即提高 3DGS 在实际应用中的鲁棒性，例如从手持手机拍摄的图像进行重建。</li>
</ol>
<p>7.方法：
（1）：提出了一种统一框架，将运动模糊建模为相机位姿上的高斯分布，同时解决相机位姿优化和运动模糊校正问题。
（2）：针对散焦模糊补偿，提出了一种机制来补偿由环境光、阴影或相机相关因素（如白平衡设置不同）引起的颜色不一致。
（3）：提出了一个具有逐图像参数的RGB解码器函数，以解决由环境光、阴影或相机相关因素（如白平衡设置不同）引起的颜色不一致。</p>
<p>8.结论：
（1）：本文提出了一种统一框架，将运动模糊建模为相机位姿上的高斯分布，同时解决相机位姿优化和运动模糊校正问题，并针对散焦模糊补偿和颜色不一致提出了机制，提高了3D高斯溅射的鲁棒性。
（2）：创新点：本文提出了一个统一的框架，同时解决相机位姿优化、运动模糊校正、散焦模糊补偿和颜色不一致等问题，提高了3D高斯溅射的鲁棒性。
性能：本文方法在Scannet++和Deblur-NeRF等基准数据集上获得了最先进的结果，并对相关基准线进行了持续的改进。
工作量：本文方法的实现相对复杂，需要对相机位姿优化、运动模糊校正、散焦模糊补偿和颜色不一致等多个方面进行建模和求解。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-1fe522891f8ae397344ebb9db256a018.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-09d15a60f6aa00f7632f702431cf9775.jpg" align="middle">
</details>




## OmniGS: Omnidirectional Gaussian Splatting for Fast Radiance Field   Reconstruction using Omnidirectional Images

**Authors:Longwei Li, Huajian Huang, Sai-Kit Yeung, Hui Cheng**

Photorealistic reconstruction relying on 3D Gaussian Splatting has shown promising potential in robotics. However, the current 3D Gaussian Splatting system only supports radiance field reconstruction using undistorted perspective images. In this paper, we present OmniGS, a novel omnidirectional Gaussian splatting system, to take advantage of omnidirectional images for fast radiance field reconstruction. Specifically, we conduct a theoretical analysis of spherical camera model derivatives in 3D Gaussian Splatting. According to the derivatives, we then implement a new GPU-accelerated omnidirectional rasterizer that directly splats 3D Gaussians onto the equirectangular screen space for omnidirectional image rendering. As a result, we realize differentiable optimization of the radiance field without the requirement of cube-map rectification or tangent-plane approximation. Extensive experiments conducted in egocentric and roaming scenarios demonstrate that our method achieves state-of-the-art reconstruction quality and high rendering speed using omnidirectional images. To benefit the research community, the code will be made publicly available once the paper is published. 

[PDF](http://arxiv.org/abs/2404.03202v2) 7 pages, 4 figures

**Summary**
全景高斯点云系统利用全向图像进行快速的视场重建，无需立方体贴图校正或切平面逼近，实现可微分优化。

**Key Takeaways**
- 全景高斯点云系统利用全向图像进行视场重建。
- 该系统通过理论分析球面相机模型导数，实现对全向图像的快速光栅化。
- 系统通过 GPU 加速，直接将三维高斯点云渲染到等距矩形屏幕空间。
- 无需立方体贴图校正或切平面逼近，可实现视场的光差分优化。
- 该方法在自中心和漫游场景中均达到最先进的重建质量和高渲染速度。
- 该系统代码将于论文发表后公开。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：OmniGS：全向高斯 splatting，用于使用全向图像快速重建光场</li>
<li>作者：李龙威，黄华健，杨世杰，程辉</li>
<li>隶属：中山大学计算机科学与工程学院</li>
<li>关键词：全向视觉，光场重建，3D 重建，新视角合成，高斯 splatting</li>
<li>链接：https://arxiv.org/abs/2404.03202</li>
<li>摘要：
（1）研究背景：
近年来，使用神经辐射场 (NeRF) 技术进行光场重建取得了显著进展。然而，NeRF 方法的训练和推理时间较长，限制了其在实时应用中的使用。</li>
</ol>
<p>（2）过去方法及问题：
3D 高斯 splatting 是一种有效解决 NeRF 限制的方法，它使用 3D 高斯明确表示光场。然而，现有的 splatting 算法仅支持使用未失真的透视图像进行光场重建。</p>
<p>（3）本文方法：
本文提出了一种新的系统 OmniGS，它利用全向高斯 splatting 进行快速光场重建。OmniGS 对球面相机模型导数进行了理论分析，并实现了新的 GPU 加速全向光栅化器，可直接将 3D 高斯 splatting 到等距矩形屏幕空间，用于全向图像渲染。</p>
<p>（4）方法性能：
在以自我为中心和漫游场景中进行的广泛实验表明，OmniGS 使用全向图像实现了最先进的重建质量和高渲染速度。这些性能支持了 OmniGS 在实时应用中的使用。</p>
<ol>
<li>
<p>方法：
(1): 提出 OmniGS 系统，利用全向高斯 splatting 进行快速光场重建；
(2): 对球面相机模型导数进行理论分析，实现 GPU 加速全向光栅化器；
(3): 将 3D 高斯 splatting 直接光栅化到等距矩形屏幕空间，用于全向图像渲染；
(4): 在自我为中心和漫游场景中进行广泛实验，验证 OmniGS 在使用全向图像进行重建时，具有最先进的重建质量和高渲染速度。</p>
</li>
<li>
<p>结论：
(1): 本工作提出了一种使用全向高斯 splatting 进行快速光场重建的新系统 OmniGS，该系统在使用全向图像进行重建时，具有最先进的重建质量和高渲染速度，支持了 OmniGS 在实时应用中的使用。
(2): 创新点：</p>
</li>
<li>提出 OmniGS 系统，利用全向高斯 splatting 进行快速光场重建。</li>
<li>对球面相机模型导数进行理论分析，实现 GPU 加速全向光栅化器。</li>
<li>将 3D 高斯 splatting 直接光栅化到等距矩形屏幕空间，用于全向图像渲染。</li>
<li>在自我为中心和漫游场景中进行广泛实验，验证 OmniGS 在使用全向图像进行重建时，具有最先进的重建质量和高渲染速度。
性能：</li>
<li>使用全向图像实现了最先进的重建质量和高渲染速度。</li>
<li>支持 OmniGS 在实时应用中的使用。
工作量：</li>
<li>对球面相机模型导数进行理论分析。</li>
<li>实现 GPU 加速全向光栅化器。</li>
<li>在自我为中心和漫游场景中进行广泛实验。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-5c5391fc4277ce922cdddc0af1ec26d4.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-d443789e6c3193b616d8dc21049af0b5.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1ca44202ac53707a8da1ef4807f9c933.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-c42315ac9ad685573dcfa99dc36d6e4e.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-03c97710b7522487bbb73acfc93336fd.jpg" align="middle">
</details>




## CityGaussian: Real-time High-quality Large-Scale Scene Rendering with   Gaussians

**Authors:Yang Liu, He Guan, Chuanchen Luo, Lue Fan, Junran Peng, Zhaoxiang Zhang**

The advancement of real-time 3D scene reconstruction and novel view synthesis has been significantly propelled by 3D Gaussian Splatting (3DGS). However, effectively training large-scale 3DGS and rendering it in real-time across various scales remains challenging. This paper introduces CityGaussian (CityGS), which employs a novel divide-and-conquer training approach and Level-of-Detail (LoD) strategy for efficient large-scale 3DGS training and rendering. Specifically, the global scene prior and adaptive training data selection enables efficient training and seamless fusion. Based on fused Gaussian primitives, we generate different detail levels through compression, and realize fast rendering across various scales through the proposed block-wise detail levels selection and aggregation strategy. Extensive experimental results on large-scale scenes demonstrate that our approach attains state-of-theart rendering quality, enabling consistent real-time rendering of largescale scenes across vastly different scales. Our project page is available at https://dekuliutesla.github.io/citygs/. 

[PDF](http://arxiv.org/abs/2404.01133v2) Project Page: https://dekuliutesla.github.io/citygs/

**Summary**
通过采用分而治之的训练方法和分级细节策略，CityGaussian 有助于有效地训练大规模 3DGS 并实时渲染不同比例的场景。

**Key Takeaways**
* CityGaussian 提出了一种新颖的分而治之训练方法，用于高效的大规模 3DGS 训练。
* 全局场景先验和自适应训练数据选择可实现高效的训练和无缝融合。
* 基于融合的高斯基元，通过压缩生成不同细节等级。
* 通过提出的分块细节级别选择和聚合策略，实现跨不同比例的快速渲染。
* 大规模场景上的广泛实验结果表明，CityGaussian 的渲染质量达到最先进的水平。
* CityGaussian 能够以一致的方式实时渲染跨不同比例的大规模场景。
* CityGaussian 项目主页：https://dekuliutesla.github.io/citygs/。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>论文标题：CityGaussian：实时高质量大场景渲染中的高斯体素</li>
<li>作者：Yang Liu, He Guan, Chuanchen Luo, Lue Fan, Junran Peng, Zhaoxiang Zhang</li>
<li>第一作者单位：中国科学院自动化研究所</li>
<li>关键词：大场景重建、新视角合成、3D高斯体素</li>
<li>论文链接：https://arxiv.org/abs/2404.01133
Github 代码链接：无</li>
<li>
<p>摘要：
(1) 研究背景：实时 3D 场景重建和新视角合成在 AR/VR、航空测量和自动驾驶等领域至关重要。该任务追求大范围（通常超过 1.5 公里²）的高保真重建和实时渲染，跨越不同的尺度。近年来，神经辐射场 (NeRF) 主导了该领域，但它们在细节保真度方面仍存在不足或性能低下的问题。
(2) 过去方法及其问题：3D 高斯体素 (3DGS) 作为一种有前途的替代解决方案出现。它使用显式 3D 高斯体素作为基元，在渲染速度和质量方面表现出优势。然而，有效训练大规模 3DGS 并在各种尺度上实时渲染它仍然具有挑战性。
(3) 本文提出的研究方法：本文提出了 CityGaussian (CityGS)，它采用了一种新颖的分割和征服训练方法和细节级别 (LoD) 策略，以实现高效的大规模 3DGS 训练和渲染。具体来说，全局场景先验和自适应训练数据选择实现了高效的训练和无缝融合。基于融合的高斯基元，我们通过压缩生成了不同的细节级别，并通过提出的块级细节级别选择和聚合策略实现了跨不同尺度的快速渲染。
(4) 方法在任务和性能上的表现：在大规模场景上的广泛实验结果表明，我们的方法达到了最先进的渲染质量，实现了跨不同尺度的大规模场景的实时渲染。这些性能支持了本文的目标。</p>
</li>
<li>
<p>方法：
（1）生成粗略的全局高斯体素，作为训练的先验；
（2）基于全局先验，根据数据分布自适应地划分高斯体素和数据；
（3）利用融合的高斯基元，生成不同细节层次，并通过块级细节层次选择和聚合策略实现跨尺度的快速渲染。</p>
</li>
<li>
<p>结论：
(1): 本工作提出了 CityGaussian (CityGS)，一种用于大规模场景的高斯体素表示方法，通过分割和征服训练方法和细节级别策略实现了高效的训练和渲染。该方法在大规模场景上实现了最先进的渲染质量，支持跨不同尺度的实时渲染。
(2): 创新点：</p>
</li>
<li>提出了一种新颖的分割和征服训练方法，有效训练大规模 3DGS。</li>
<li>设计了一种细节级别策略，通过压缩生成不同细节级别，并通过块级细节级别选择和聚合策略实现跨尺度的快速渲染。
性能：</li>
<li>在大规模场景上实现了最先进的渲染质量。</li>
<li>支持跨不同尺度的实时渲染。
工作量：</li>
<li>训练和渲染大规模 3DGS 具有挑战性。</li>
<li>需要进一步的研究来提高训练和渲染效率。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-cdc289cc94afaf05e9abae37e6d49ef8.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-547f5a57e280ecd60e9f1e905a13c71d.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-8faf5cbf97c2d3cac383a23cf4a18d31.jpg" align="middle">
</details>




