
---
title: 3DGS
date: 2024-02-02 22:24:12
author: Kedreamix
cover: https://pica.zhimg.com/v2-e4e5570dfa99dfac9b297f7650c717c3.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-02-02  360-GS Layout-guided Panoramic Gaussian Splatting For Indoor Roaming  
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

# 2024-02-02 更新


## 360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming

**Authors:Jiayang Bai, Letian Huang, Jie Guo, Wen Gong, Yuanqi Li, Yanwen Guo**

3D Gaussian Splatting (3D-GS) has recently attracted great attention with real-time and photo-realistic renderings. This technique typically takes perspective images as input and optimizes a set of 3D elliptical Gaussians by splatting them onto the image planes, resulting in 2D Gaussians. However, applying 3D-GS to panoramic inputs presents challenges in effectively modeling the projection onto the spherical surface of ${360^\circ}$ images using 2D Gaussians. In practical applications, input panoramas are often sparse, leading to unreliable initialization of 3D Gaussians and subsequent degradation of 3D-GS quality. In addition, due to the under-constrained geometry of texture-less planes (e.g., walls and floors), 3D-GS struggles to model these flat regions with elliptical Gaussians, resulting in significant floaters in novel views. To address these issues, we propose 360-GS, a novel $360^{\circ}$ Gaussian splatting for a limited set of panoramic inputs. Instead of splatting 3D Gaussians directly onto the spherical surface, 360-GS projects them onto the tangent plane of the unit sphere and then maps them to the spherical projections. This adaptation enables the representation of the projection using Gaussians. We guide the optimization of 360-GS by exploiting layout priors within panoramas, which are simple to obtain and contain strong structural information about the indoor scene. Our experimental results demonstrate that 360-GS allows panoramic rendering and outperforms state-of-the-art methods with fewer artifacts in novel view synthesis, thus providing immersive roaming in indoor scenarios. 

[PDF](http://arxiv.org/abs/2402.00763v1) 11 pages, 10 figures

**Summary**
360-GS 以平面投影为基础，利用布局先验来指导优化过程，从而产生可用于渲染全景和生成新视角图像的 3D 椭圆高斯分布。

**Key Takeaways**

- 3D 高斯斑点 (3D-GS) 是一种流行的技术，它通常将透视图像作为输入，并优化一组 3D 椭圆高斯分布，将它们喷射到图像平面上，从而产生 2D 高斯分布。
- 然而，将 3D-GS 应用于全景输入时，使用 2D 高斯分布对 ${360^\circ}$ 图像的球形表面上的投影进行建模存在挑战。
- 在实际应用中，输入全景通常很稀疏，导致 3D 高斯分布的初始化不可靠，随后 3D-GS 质量下降。
- 此外，由于纹理平面（例如墙壁和地板）的几何形状受限，3D-GS 难以使用椭圆高斯分布对这些平坦区域进行建模，从而导致新视图中出现明显的漂浮物。
- 为了解决这些问题，我们提出了 360-GS，这是一种针对有限数量的全景输入的新型 $360^{\circ}$ 高斯斑点。
- 360-GS 不将 3D 高斯分布直接喷射到球形表面上，而是将其投影到单位球的切平面，然后将它们映射到球形投影。这种改编能够使用高斯分布表示投影。
- 我们通过利用全景中的布局先验来指导 360-GS 的优化，这些先验很容易获得，并且包含有关室内场景的强大结构信息。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：360-GS：布局引导的室内全景高斯渲染</li>
<li>作者：Jiayang Bai, Letian Huang, Jie Guo, Wen Gong, Yuanqi Li, Yanwen Guo</li>
<li>隶属：南京大学</li>
<li>关键词：3D高斯渲染、全景图像、室内场景、布局引导</li>
<li>论文链接：https://arxiv.org/abs/2402.00763
   Github 链接：无</li>
<li>
<p>摘要：
   (1)：研究背景：3D高斯渲染（3D-GS）因其实时性和照片级渲染效果而备受关注。该技术通常以透视图像作为输入，通过将一组 3D 椭圆高斯体渲染到图像平面上，从而生成 2D 高斯体。然而，将 3D-GS 应用于全景输入时，使用 2D 高斯体有效建模 360° 图像的球面投影存在挑战。在实际应用中，输入全景图像通常是稀疏的，导致 3D 高斯体的初始化不可靠，进而降低 3D-GS 的质量。此外，由于缺乏纹理的平面（例如墙壁和地板）的几何约束不足，3D-GS 难以使用椭圆高斯体对这些平面区域进行建模，从而导致在新的视角中出现明显的浮动物体。
   (2)：过去的方法及其问题：为了解决这些问题，本文提出了一种针对有限全景输入的新型 360° 高斯渲染方法 360-GS。与直接将 3D 高斯体渲染到球面上不同，360-GS 将其投影到单位球体的切平面，然后将其映射到球面投影。这种改进使得使用高斯体表示投影成为可能。我们通过利用全景图像中的布局先验来指导 360-GS 的优化，这些先验易于获取，并且包含有关室内场景的强结构信息。
   (3)：本文的研究方法：我们的实验结果表明，360-GS 能够从有限数量的全景输入中生成高质量的全景渲染。与 3D-GS 相比，360-GS 在准确性、细节和鲁棒性方面均表现出优势。
   (4)：方法的性能及其对目标的支持：360-GS 在室内场景渲染任务上取得了优异的性能。与 3D-GS 相比，360-GS 在准确性、细节和鲁棒性方面均表现出优势。这些结果表明，360-GS 能够有效地利用布局先验来指导 3D 高斯体的优化，从而生成高质量的全景渲染。</p>
</li>
<li>
<p>方法：
(1)：360◦高斯体镶嵌：提出了一种新颖的 splatting 技术，将 splatting 分解为两个步骤：在单位球体的切平面上 splatting 和映射到球面。
(2)：布局引导初始化和正则化：利用全景图像中的布局先验来指导 3D 高斯体的优化，这些先验易于获取，并且包含有关室内场景的强结构信息。
(3)：全景渲染：通过将 splattered 的高斯体从前到后进行 alpha 混合，可以生成全景渲染。</p>
</li>
<li>
<p>结论：
（1）：本文提出了一种新颖的布局引导全景高斯渲染流水线，名为360-GS，它支持直接全景渲染，并且对稀疏输入具有鲁棒性。360-GS的基石是我们的360◦高斯 splatting 算法以及房间布局先验的结合。360◦高斯 splatting 算法通过利用透视投影和映射来解决在球面表面建模投影的挑战，从而实现对具有等距矩形图像的 3D 高斯的直接优化。我们在 3D 高斯的初始化过程中利用全景图中的房间布局先验，提供了一种更易于访问且鲁棒的替代方案来替代 SfM 点云。我们还引入了布局引导正则化来减轻浮动问题并保留房间布局的几何结构。360-GS 支持实时漫游，并在真实世界场景中为新颖视角合成提供了最先进的性能。
（2）：创新点：</p>
</li>
<li>提出了一种新颖的 360◦高斯 splatting 算法，该算法将 splatting 分解为两个步骤：在单位球体的切平面上 splatting 和映射到球面。</li>
<li>利用全景图像中的布局先验来指导 3D 高斯的优化，这些先验易于获取，并且包含有关室内场景的强结构信息。</li>
<li>引入了布局引导正则化来减轻浮动问题并保留房间布局的几何结构。
性能：</li>
<li>与 3D-GS 相比，360-GS 在准确性、细节和鲁棒性方面均表现出优势。</li>
<li>360-GS 在室内场景渲染任务上取得了优异的性能。
工作量：</li>
<li>需要收集和预处理全景图像。</li>
<li>需要优化 3D 高斯的参数。</li>
<li>需要将 splattered 的高斯体从前到后进行 alpha 混合以生成全景渲染。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-38c0a2fd61f19043e9f57d34dec4a1c6.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-9fe5198d06678b334414f192b0c83aa8.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-e4e5570dfa99dfac9b297f7650c717c3.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-f5349fc8a22abb33ba9a2c7388b0a826.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1d8e3eade9a3d6331e76dbab98e15a68.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-ffe9d7162c03cd614dfd0b6e7509adbd.jpg" align="middle">
</details>




## CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians with   Dual Feature Fusion

**Authors:Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan**

We propose Compact and Swift Segmenting 3D Gaussians(CoSSegGaussians), a method for compact 3D-consistent scene segmentation at fast rendering speed with only RGB images input. Previous NeRF-based segmentation methods have relied on time-consuming neural scene optimization. While recent 3D Gaussian Splatting has notably improved speed, existing Gaussian-based segmentation methods struggle to produce compact masks, especially in zero-shot segmentation. This issue probably stems from their straightforward assignment of learnable parameters to each Gaussian, resulting in a lack of robustness against cross-view inconsistent 2D machine-generated labels. Our method aims to address this problem by employing Dual Feature Fusion Network as Gaussians' segmentation field. Specifically, we first optimize 3D Gaussians under RGB supervision. After Gaussian Locating, DINO features extracted from images are applied through explicit unprojection, which are further incorporated with spatial features from the efficient point cloud processing network. Feature aggregation is utilized to fuse them in a global-to-local strategy for compact segmentation features. Experimental results show that our model outperforms baselines on both semantic and panoptic zero-shot segmentation task, meanwhile consumes less than 10% inference time compared to NeRF-based methods. Code and more results will be available at https://David-Dou.github.io/CoSSegGaussians 

[PDF](http://arxiv.org/abs/2401.05925v3) 9 pages, 8 figures, correct writing details

**摘要**
结合点云与显式反投射的特征融合网络，实现紧凑而快速的 3D 高斯混合分割。

**关键要点**

- 提出一种用于紧凑、快速且仅以RGB图像作为输入的3D场景一致性分割方法：紧凑快速分割3D高斯（CoSSegGaussians）。
- 现有的基于高斯体素的分割方法在进行零镜头分割时难以生成紧凑的掩模，这可能是因为它们将可学习的参数直接分配给每个高斯体素，从而导致缺乏对跨视图不一致的2D机器生成的标签的鲁棒性。
- 利用双特征融合网络作为高斯体素的分割字段来解决上述问题。
- 首先在RGB监督下优化3D高斯体素。
- 然后通过显式反投影应用从图像中提取的DINO特征，并结合来自有效点云处理网络的空间特征。
- 利用特征聚合在全局到局部的策略中融合这些特征以实现紧凑的分割特征。
- 实验结果表明，与NeRF为基础的方法相比，该模型在语义分割和全景零镜头分割任务上都优于基线，同时推理时间少于10%。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：紧凑而快速的场景分割 3D 高斯体与双重特征融合</li>
<li>作者：Dou Bin, Zhang Tianyu, Ma Yongjia, Wang Zhaohui, Yuan Zejian</li>
<li>单位：西安交通大学人工智能与机器人学院</li>
<li>关键词：3D 场景分割、神经辐射场、高斯体、双重特征融合</li>
<li>论文链接：https://arxiv.org/abs/2401.05925，Github 代码链接：None</li>
<li>
<p>摘要：
（1）研究背景：近年来，计算机视觉和计算机图形学取得了显着进展，特别是在神经渲染领域。神经辐射场 (NeRF) 及其后续方法推动了神经场景表示的发展，在新型视图合成方面显示出显着的性能。
（2）过去的方法及其问题：基于 NeRF 的分割方法依赖于耗时的神经场景优化。虽然最近的 3D 高斯体 splatting 显着提高了速度，但现有的基于高斯体的分割方法难以产生紧凑的掩模，尤其是在零样本分割中。这个问题可能源于其直接将可学习参数分配给每个高斯体，导致对跨视图不一致的 2D 机器生成的标签缺乏鲁棒性。
（3）本文方法：本文提出了一种紧凑而快速的场景分割方法，称为 CoSSegGaussians，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度快。具体来说，我们首先在 RGB 监督下优化 3D 高斯体。在高斯体定位之后，通过显式反投影应用从图像中提取的 DINO 特征，然后将其与来自高效点云处理网络的空间特征结合。利用特征聚合在全局到局部策略中融合它们以获得紧凑的分割特征。
（4）方法性能：实验结果表明，我们的模型在语义和全景零样本分割任务上都优于基线方法，同时推理时间不到基于 NeRF 的方法的 10%。</p>
</li>
<li>
<p>方法：
（1）高斯体定位阶段：使用 L1 和 L_D-SSIM 光度损失来监督高斯体的几何信息，包括质心、协方差、不透明度和颜色。
（2）分割阶段：将多尺度的 DINO 特征反投影到高斯体上，并与从高斯体中提取的空间特征融合。
（3）特征聚合：使用全局到局部策略聚合融合后的特征，以生成紧凑的分割特征。
（4）监督：使用零样本分割掩模和关联掩模来监督分割参数，并使用 NCE 损失进行优化。</p>
</li>
<li>
<p>结论：
（1）：本文提出了一种紧凑而快速的场景分割方法 CoSSegGaussians，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度快。实验结果表明，我们的模型在语义和全景零样本分割任务上都优于基线方法，同时推理时间不到基于 NeRF 的方法的 10%。
（2）：创新点：</p>
</li>
<li>提出了一种紧凑而快速的场景分割方法 CoSSegGaussians，该方法仅使用 RGB 图像输入即可实现紧凑的 3D 一致场景分割，且渲染速度快。</li>
<li>提出了一种双重特征融合网络作为分割场，该网络聚合了 DINO 和空间特征用于分割。</li>
<li>将多尺度的 DINO 特征从图像反投影到定位的 3D 高斯体上，并进一步与高斯体的空间信息相结合。</li>
<li>应用全局到局部聚合模块生成紧凑的分割逻辑。
性能：</li>
<li>在语义和全景零样本分割任务上都优于基线方法。</li>
<li>推理时间不到基于 NeRF 的方法的 10%。
工作量：</li>
<li>使用了大量的数据集进行训练和测试。</li>
<li>算法的实现和训练过程较为复杂。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-ecce62ef2d2a0a0c5d6577de6d7cb33f.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-222c4f05c24f306aefd909de021e726c.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-6dff94133ac5b0802b5de3fb9550eff1.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-e96a03193e246ab9e77a3dd6aa18e239.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-3f381d5614322d380f003e54e659eb10.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-fb6b0eeec85fc1d0f2cd12928b40918f.jpg" align="middle">
</details>




