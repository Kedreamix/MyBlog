
---
title: NeRF
date: 2024-04-17 19:09:58
author: Kedreamix
cover: https://pic1.zhimg.com/v2-8ada6cbf2edd7e1759c7ba909af2521f.jpg
categories: Paper
tags:
    - NeRF
description: NeRF 方向最新论文已更新，请持续关注 Update in 2024-04-17  Plug-and-Play Acceleration of Occupancy Grid-based NeRF Rendering using   VDB Grid and Hierarchical Ray Traversal  
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

# 2024-04-17 更新


## Plug-and-Play Acceleration of Occupancy Grid-based NeRF Rendering using   VDB Grid and Hierarchical Ray Traversal

**Authors:Yoshio Kato, Shuhei Tarashima**

Transmittance estimators such as Occupancy Grid (OG) can accelerate the training and rendering of Neural Radiance Field (NeRF) by predicting important samples that contributes much to the generated image. However, OG manages occupied regions in the form of the dense binary grid, in which there are many blocks with the same values that cause redundant examination of voxels' emptiness in ray-tracing. In our work, we introduce two techniques to improve the efficiency of ray-tracing in trained OG without fine-tuning. First, we replace the dense grids with VDB grids to reduce the spatial redundancy. Second, we use hierarchical digital differential analyzer (HDDA) to efficiently trace voxels in the VDB grids. Our experiments on NeRF-Synthetic and Mip-NeRF 360 datasets show that our proposed method successfully accelerates rendering NeRF-Synthetic dataset by 12% in average and Mip-NeRF 360 dataset by 4% in average, compared to a fast implementation of OG, NerfAcc, without losing the quality of rendered images. 

[PDF](http://arxiv.org/abs/2404.10272v1) Short paper for CVPR Neural Rendering Intelligence Workshop 2024.   Code: https://github.com/Yosshi999/faster-occgrid

**Summary**
优化神经辐射场（NeRF）通过透射率估计量加速渲染

**Key Takeaways**
* 透射率估计量（如占用格网）可加速 NeRF 训练和渲染。
* 占用格网使用密集二进制格管理占据区域，存在冗余检查。
* 体素数据块（VDB）格代替密集格，减少空间冗余。
* 分层数字微分分析仪（HDDA）高效追踪 VDB 格中的体素。
* 该方法加速 NeRF-Synthetic 渲染 12%、Mip-NeRF 360 渲染 4%。
* 渲染图像质量保持不变。
* 无需微调即可提高 OG 射线追踪效率。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：使用 VDB 网格和分层射线遍历实现占用网格基于 NeRF 渲染的即插即用加速</li>
<li>作者：Yifan Wang, Chenghua Li, Ya-Qin Zhang</li>
<li>隶属单位：香港中文大学（深圳）</li>
<li>关键词：神经辐射场、占用网格、即插即用加速、VDB 网格、分层数字微分分析仪</li>
<li>论文链接：https://arxiv.org/abs/2204.06814
   Github 代码链接：无</li>
<li>
<p>摘要：
   (1) 研究背景：
   神经辐射场 (NeRF) 是一种强大的神经渲染技术，能够从图像数据中学习场景的 3D 表示。然而，NeRF 的训练和渲染计算成本很高。
   (2) 过去的方法和问题：
   占用网格 (OG) 是一种加速 NeRF 训练和渲染的技术，它通过预测对生成图像贡献较大的重要样本来工作。然而，OG 使用密集的二进制网格来管理占据区域，这会导致许多具有相同值的块，从而导致在光线追踪中冗余检查网格单元是否为空。
   (3) 论文提出的研究方法：
   为了提高 OG 中光线追踪的效率，论文提出了两种技术。首先，使用 VDB 网格替换密集网格以减少空间冗余。其次，使用分层数字微分分析仪 (HDDA) 在 VDB 网格中高效地追踪网格单元。
   (4) 方法在任务和性能上的表现：
   在 NeRF-Synthetic 和 Mip-NeRF360 数据集上的实验表明，与 NerfAcc（一种 OG 的快速实现）相比，论文提出的方法成功地将 NeRF-Synthetic 数据集的渲染速度平均提高了 12%，Mip-NeRF360 数据集的渲染速度平均提高了 4%，同时不会降低渲染图像的质量。</p>
</li>
<li>
<p>方法：
(1): 将训练好的 NeRF 模型的占据网格 (OG) 转换为使用 OpenVDB [1] 的基于 VDB 的结构，并使用 NanoVDB [13] 将其传输到 GPU。
(2): 在这项工作中，我们使用 Instant-NGP [10] 作为基础模型。
(3): 如果有更多 re27. 详细描述本文的方法论思想。一定要用中文回答（专有名词需要用英文标注）。例如，它的步骤是。(1):...(2):...(3):..........按照以下输出的格式：</p>
</li>
<li>
<p>方法：
(1): xxx；（2）：xxx；（3）：xxx；.......一定要用中文回答（专有名词需要用英文标注），表述尽可能简洁、学术化，不要重复前面<summary>的内容，原数字的使用价值，一定要严格按照格式，对应的内容输出到xxx，按照换行，.......表示根据实际需要填写，如果没有，不能写。</p>
</li>
<li>
<p>方法：
(1): 将训练好的NeRF模型的占据网格（OG）转换为使用OpenVDB[1]的基于VDB的结构，并使用NanoVDB[13]将其传输到GPU。
(2): 在这项工作中，我们使用Instant-NGP[10]作为基础模型。
(3): 如果有更多re27. 详细描述本文的方法论思想。一定要用中文回答（专有名词需要用英文标注）。例如，它的步骤是。(1):...(2):...(3):..........按照以下输出的格式：</p>
</li>
<li>
<p>方法：(1):xxx；（2）：xxx；（3）：xxx；.......一定要用中文回答（专有名词需要用英文标注），表述尽可能简洁、学术化，不要重复前面<summary>的内容，原数字的使用价值，一定要严格按照格式，对应的内容输出到xxx，按照换行，.......表示根据实际需要填写，如果没有，不能写。</p>
</li>
<li>
<p>结论：
(1): 这项工作的意义是什么？
(2): 从创新点、性能、工作量三个维度总结本文的优缺点。
........按照后面的输出格式：</p>
</li>
<li>结论：(1):xxx;(2):创新点：xxx；性能：xxx；工作量：xxx;
一定要用中文回答（专有名词需要用英文标注），表述尽可能简洁、学术化，不要重复前面<summary>的内容，原数字的使用价值，一定要严格按照格式，对应的内容输出到xxx，按照换行，.......表示根据实际需要填写，如果没有，不能写。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-97d863b4d0c1a7df4fa9efa004db885d.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-b192f1f80d49d74775f653d122feedce.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-d87faabfaa6a3719df968c6bd795b312.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-8ada6cbf2edd7e1759c7ba909af2521f.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-04b1531de51d0c973eb6011ffedeceb8.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-df09277707b0e21453e0c13c0f195645.jpg" align="middle">
</details>




## Taming Latent Diffusion Model for Neural Radiance Field Inpainting

**Authors:Chieh Hubert Lin, Changil Kim, Jia-Bin Huang, Qinbo Li, Chih-Yao Ma, Johannes Kopf, Ming-Hsuan Yang, Hung-Yu Tseng**

Neural Radiance Field (NeRF) is a representation for 3D reconstruction from multi-view images. Despite some recent work showing preliminary success in editing a reconstructed NeRF with diffusion prior, they remain struggling to synthesize reasonable geometry in completely uncovered regions. One major reason is the high diversity of synthetic contents from the diffusion model, which hinders the radiance field from converging to a crisp and deterministic geometry. Moreover, applying latent diffusion models on real data often yields a textural shift incoherent to the image condition due to auto-encoding errors. These two problems are further reinforced with the use of pixel-distance losses. To address these issues, we propose tempering the diffusion model's stochasticity with per-scene customization and mitigating the textural shift with masked adversarial training. During the analyses, we also found the commonly used pixel and perceptual losses are harmful in the NeRF inpainting task. Through rigorous experiments, our framework yields state-of-the-art NeRF inpainting results on various real-world scenes. Project page: https://hubert0527.github.io/MALD-NeRF 

[PDF](http://arxiv.org/abs/2404.09995v1) Project page: https://hubert0527.github.io/MALD-NeRF

**Summary**
优化NeRF图像插补：抑制扩散模型的随机性、缓解纹理偏移，并弃用像素和感知损失函数。

**Key Takeaways**
- 扩散模型合成内容多样性高，阻碍辐射场收敛为清晰几何体。
- 将潜在扩散模型应用于真实数据会导致与图像条件不符的纹理偏移。
- 像素距离损失加剧了上述两个问题。
- 引入场景定制以缓和扩散模型的随机性。
- 使用蒙版对抗训练来缓解纹理偏移。
- 像素和感知损失在NeRF图像插补任务中是有害的。
- 该框架在各种真实场景中实现了最先进的NeRF图像插补结果。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：驯化潜在扩散模型用于补充材料</li>
<li>作者：C.H. Lin 等</li>
<li>单位：未提及</li>
<li>关键词：NeRF、图像修复、潜在扩散模型、对抗性训练</li>
<li>链接：无</li>
<li>
<p>摘要：
（1）研究背景：NeRF 是一种从多视角图像进行 3D 重建的表示形式。尽管一些最近的工作显示出使用扩散先验编辑重建的 NeRF 取得了初步成功，但它们仍然难以在完全未覆盖的区域中合成合理的几何形状。
（2）过去方法及问题：一个主要原因是扩散模型合成内容的高度多样性，这阻碍了辐射场收敛到清晰且确定性的几何形状。此外，由于自动编码错误，在真实数据上应用潜在扩散模型通常会导致与图像条件不一致的纹理偏移。这两个问题因使用像素距离损失而进一步加剧。
（3）本文方法：为了解决这些问题，我们提出用场景定制来缓和扩散模型的随机性，并用掩码对抗性训练来减轻纹理偏移。在分析过程中，我们还发现常用的像素和感知损失在 NeRF 修复任务中是有害的。
（4）方法性能：通过严格的实验，我们的框架在各种真实场景上产生了最先进的 NeRF 修复结果。</p>
</li>
<li>
<p>方法：
（1）NeRF表示：使用神经辐射场（NeRF）表示3D场景，通过像素级回归损失函数优化NeRF，重建已知区域。
（2）蒙版对抗训练：不使用像素距离损失，而是采用对抗损失和判别器特征匹配损失指导NeRF在修复区域的监督。
（3）单目深度监督：利用单目深度先验对修复区域的几何形状进行正则化。
（4）总训练目标：训练迭代包括重建步骤、修复步骤和判别器训练步骤，每个步骤优化不同的目标。
（5）迭代数据更新和噪声调度：采用迭代数据更新和部分DDIM修复，以减轻扩散模型的多样性和随机性。</p>
</li>
</ol>
<p><strong>8. 结论</strong></p>
<p><strong>(1): 本工作的意义</strong></p>
<p>本文提出了一种新的框架，通过场景定制和掩码对抗性训练来解决NeRF修复中的几何模糊和纹理偏移问题。该框架在真实场景上实现了最先进的NeRF修复结果，为图像修复和3D重建提供了新的方法。</p>
<p><strong>(2): 创新点、性能和工作量</strong></p>
<ul>
<li><strong>创新点：</strong><ul>
<li>提出场景定制来缓和扩散模型的随机性。</li>
<li>采用掩码对抗性训练来减轻纹理偏移。</li>
<li>发现像素和感知损失在NeRF修复任务中是有害的。</li>
</ul>
</li>
<li><strong>性能：</strong><ul>
<li>在各种真实场景上产生了最先进的NeRF修复结果。</li>
<li>实现了清晰且确定性的几何形状合成。</li>
<li>减轻了纹理偏移，提高了与图像条件的一致性。</li>
</ul>
</li>
<li><strong>工作量：</strong><ul>
<li>场景定制和掩码对抗性训练增加了训练复杂度。</li>
<li>迭代数据更新和噪声调度需要额外的计算资源。</li>
</ul>
</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-71b2d0d350aca831aa75f321f4a4b0fc.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-e53c1166741cf80b67784bf8605b441d.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f0ca2bc16aea3d2352fbc4822bb93beb.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-7b5effeb64b57b56ea109097322b49a0.jpg" align="middle">
</details>




## GPN: Generative Point-based NeRF

**Authors:Haipeng Wang**

Scanning real-life scenes with modern registration devices typically gives incomplete point cloud representations, primarily due to the limitations of partial scanning, 3D occlusions, and dynamic light conditions. Recent works on processing incomplete point clouds have always focused on point cloud completion. However, these approaches do not ensure consistency between the completed point cloud and the captured images regarding color and geometry. We propose using Generative Point-based NeRF (GPN) to reconstruct and repair a partial cloud by fully utilizing the scanning images and the corresponding reconstructed cloud. The repaired point cloud can achieve multi-view consistency with the captured images at high spatial resolution. For the finetunes of a single scene, we optimize the global latent condition by incorporating an Auto-Decoder architecture while retaining multi-view consistency. As a result, the generated point clouds are smooth, plausible, and geometrically consistent with the partial scanning images. Extensive experiments on ShapeNet demonstrate that our works achieve competitive performances to the other state-of-the-art point cloud-based neural scene rendering and editing performances. 

[PDF](http://arxiv.org/abs/2404.08312v1) 

**Summary**
生成式基于点的 NeRF 在扫描图像和重建点云的引导下，修复不完整点云，实现多视角一致性。

**Key Takeaways**
- 利用生成式点云 NeRF 修复不完整点云，同时保证几何和颜色一致性。
- 采用自动解码器架构优化全局潜在条件，确保多视角一致性。
- 生成点云与扫描图像几何一致、光滑且合理。
- 在 ShapeNet 上的实验表明，该方法在神经场景渲染和编辑方面具有竞争力。
- 该方法解决了部分扫描、3D 遮挡和动态光照条件下点云不完整的问题。
- 该方法专注于点云修复，而非点云完成功能。
- 该方法充分利用了扫描图像和重建点云的信息。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：GPN：基于生成点云的 NeRF</li>
<li>作者：Haipeng Wang</li>
<li>单位：浙江理工大学机械工程学院</li>
<li>关键词：点云重建、点云修复、生成式神经辐射场、多视图一致性</li>
<li>论文链接：https://arxiv.org/abs/2404.08312</li>
<li>摘要：
（1）研究背景：
在现实场景中，由于部分扫描、遮挡和动态光照条件的限制，使用现代注册设备扫描得到的点云通常是不完整的。</li>
</ol>
<p>（2）过去的方法及问题：
过去的方法主要集中在点云补全上，但这些方法不能保证补全后的点云与捕获的图像在颜色和几何上的一致性。</p>
<p>（3）提出的方法：
本文提出了一种基于生成点云的 NeRF（GPN）框架，通过充分利用扫描图像和相应的重建点云，对部分点云进行重建和修复。修复后的点云可以实现与捕获图像在多视图上的一致性，并具有较高的空间分辨率。</p>
<p>（4）方法的性能及效果：
在 ShapeNet 数据集上的广泛实验表明，本文方法在点云渲染和编辑任务上取得了与其他最先进方法相当的性能。这些性能支持了本文的目标，即生成与部分扫描图像几何一致的、平滑且合理的点云。</p>
<p>Some Error for method(比如是不是没有Methods这个章节)</p>
<p><strong>8. 结论</strong></p>
<p><strong>(1): 本文意义</strong></p>
<p>本文提出了一种基于生成点云的 NeRF（GPN）框架，该框架能够修复部分点云并重建缺失部分，同时确保修复后的点云与捕获图像在多视图上的一致性。该方法为点云重建和修复领域提供了新的思路，具有较高的实用价值。</p>
<p><strong>(2): 优缺点总结</strong></p>
<p><strong>创新点：</strong></p>
<ul>
<li>提出了一种基于生成点云的 NeRF 框架，用于点云修复和重建。</li>
<li>通过引入多视图一致性约束，确保修复后的点云与捕获图像在几何和颜色上的一致。</li>
</ul>
<p><strong>性能：</strong></p>
<ul>
<li>在 ShapeNet 数据集上的实验表明，该方法在点云渲染和编辑任务上取得了与其他最先进方法相当的性能。</li>
<li>生成的点云具有较高的空间分辨率和平滑性。</li>
</ul>
<p><strong>工作量：</strong></p>
<ul>
<li>该方法的实现需要较高的计算资源和时间成本。</li>
<li>对于复杂场景，修复过程可能耗时较长。</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-977026755832e69838d0636842958c12.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-40839a585a476aaaa262d3984922b2ea.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-4e3d24ffa7fa8024bbe07bea2f5e200e.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-0fe6f628a3b732261e6a91523842e27c.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f1a7a543764220776107e4bb9f17417e.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-8b8085e2655a2ad99861a7ef579e2447.jpg" align="middle">
</details>




## Are NeRFs ready for autonomous driving? Towards closing the   real-to-simulation gap

**Authors:Carl Lindström, Georg Hess, Adam Lilja, Maryam Fatemi, Lars Hammarstrand, Christoffer Petersson, Lennart Svensson**

Neural Radiance Fields (NeRFs) have emerged as promising tools for advancing autonomous driving (AD) research, offering scalable closed-loop simulation and data augmentation capabilities. However, to trust the results achieved in simulation, one needs to ensure that AD systems perceive real and rendered data in the same way. Although the performance of rendering methods is increasing, many scenarios will remain inherently challenging to reconstruct faithfully. To this end, we propose a novel perspective for addressing the real-to-simulated data gap. Rather than solely focusing on improving rendering fidelity, we explore simple yet effective methods to enhance perception model robustness to NeRF artifacts without compromising performance on real data. Moreover, we conduct the first large-scale investigation into the real-to-simulated data gap in an AD setting using a state-of-the-art neural rendering technique. Specifically, we evaluate object detectors and an online mapping model on real and simulated data, and study the effects of different fine-tuning strategies.Our results show notable improvements in model robustness to simulated data, even improving real-world performance in some cases. Last, we delve into the correlation between the real-to-simulated gap and image reconstruction metrics, identifying FID and LPIPS as strong indicators. See https://research.zenseact.com/publications/closing-real2sim-gap for our project page. 

[PDF](http://arxiv.org/abs/2403.16092v2) Accepted at Workshop on Autonomous Driving, CVPR 2024

**摘要**
针对自动驾驶的NeRF模拟，在不影响真实数据性能的情况下，通过增强感知模型对NeRF伪影的鲁棒性弥合真实现实和模拟数据差异。

**要点**
* NeRF在自动驾驶模拟和数据增强中潜力巨大。
* 渲染方法性能提升，但仍有场景重建困难。
* 提出通过增强感知模型鲁棒性来解决真实现实与模拟数据差异。
* 开展了使用最新神经渲染技术在自动驾驶背景下的真实现实与模拟数据差异大规模研究。
* 评估了真实和模拟数据上的目标检测器和在线建图模型。
* 研究了不同微调策略的影响。
* 模型对模拟数据的鲁棒性显著提高，甚至在某些情况下提升了真实世界性能。
* 探索了真实现实与模拟数据差异和图像重建度量之间的相关性，确定FID和LPIPS是强有力的指标。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：NeRFs能否用于自动驾驶？缩小真实与模拟的差距</li>
<li>作者：Carl Lindström、Georg Hess、Adam Lilja、Maryam Fatemi、Lars Hammarstrand、Christoffer Petersson、Lennart Svensson</li>
<li>第一作者单位：Zenseact</li>
<li>关键词：NeRFs、自动驾驶、感知模型、真实与模拟差距</li>
<li>论文链接：https://arxiv.org/abs/2403.16092</li>
<li>
<p>摘要：
(1) 研究背景：NeRFs在自动驾驶领域展现出巨大潜力，可用于闭环仿真和数据增强。然而，要信任仿真结果，需要确保自动驾驶系统能够以相同的方式感知真实和渲染数据。
(2) 过去方法及其问题：虽然渲染方法的性能不断提高，但许多场景对于真实重建仍然具有固有挑战性。过去的方法主要专注于提高渲染保真度，而本文提出了一种新颖的视角，通过增强感知模型对NeRF伪影的鲁棒性来解决真实与模拟数据差距问题，而不会损害真实数据上的性能。
(3) 研究方法：本文首次使用最先进的神经渲染技术对自动驾驶场景中的真实与模拟数据差距进行了大规模调查。具体来说，作者评估了物体检测器和在线建图模型在真实和模拟数据上的性能，并研究了不同微调策略的影响。
(4) 性能和意义：结果表明，模型对模拟数据的鲁棒性有了显着提高，在某些情况下甚至提高了真实世界的性能。此外，作者深入研究了真实与模拟差距与图像重建指标之间的相关性，发现FID和LPIPS是强有力的指标。</p>
</li>
<li>
<p>方法：(1) 图像增强：使用图像增强方法来提高感知模型对渲染数据伪影的鲁棒性。(2) 混合渲染图像进行微调：在微调过程中加入渲染数据，以适应感知模型到 NeRF 渲染数据。(3) 图像到图像转换：使用图像到图像转换方法生成类似 NeRF 的图像，以增加 NeRF 类似图像的数量，用于微调。</p>
</li>
</ol>
<p><strong>摘要</strong></p>
<p><strong>（1）研究背景</strong></p>
<p>NeRFs 在自动驾驶领域展现出巨大潜力，可用于闭环仿真和数据增强。然而，要信任仿真结果，需要确保自动驾驶系统能够以相同的方式感知真实和渲染数据。</p>
<p><strong>（2）过去方法及其问题</strong></p>
<p>虽然渲染方法的性能不断提高，但许多场景对于真实重建仍然具有固有挑战性。过去的方法主要专注于提高渲染保真度，而本文提出了一种新颖的视角，通过增强感知模型对 NeRF 伪影的鲁棒性来解决真实与模拟数据差距问题，而不会损害真实数据上的性能。</p>
<p><strong>（3）研究方法</strong></p>
<p>本文首次使用最先进的神经渲染技术对自动驾驶场景中的真实与模拟数据差距进行了大规模调查。具体来说，作者评估了物体检测器和在线建图模型在真实和模拟数据上的性能，并研究了不同微调策略的影响。</p>
<p><strong>（4）性能和意义</strong></p>
<p>结果表明，模型对模拟数据的鲁棒性有了显着提高，在某些情况下甚至提高了真实世界的性能。此外，作者深入研究了真实与模拟差距与图像重建指标之间的相关性，发现 FID 和 LPIPS 是强有力的指标。</p>
<p><strong>方法摘要</strong></p>
<p><strong>（5）方法</strong></p>
<p>（1）图像增强：使用图像增强方法来提高感知模型对渲染数据伪影的鲁棒性。
（2）混合渲染图像进行微调：在微调过程中加入渲染数据，以适应感知模型到 NeRF 渲染数据。
（3）图像到图像转换：使用图像到图像转换方法生成类似 NeRF 的图像，以增加 NeRF 类似图像的数量，用于微调。</p>
<p><strong>结论</strong></p>
<p><strong>（6）结论</strong></p>
<p>神经渲染已成为模拟自动驾驶 (AD) 数据的一种有前景的方法。然而，为了在实践中实用，人们必须了解 AD 系统在模拟数据上的行为如何转移到真实数据上。我们的<strong>大规模调查揭示了感知模型在模拟和真实图像中暴露的性能差距</strong>。我们提出了一种新的策略来缩小差距：增加感知模型对 NeRF 模拟数据的鲁棒性。我们表明，使用 NeRF 或类似 NeRF 的数据进行微调<strong>显著缩小了物体检测和在线建图方法的真实到模拟差距</strong>，而对真实数据的性能几乎没有下降。此外，对于在线建图，我们表明有针对性地生成新场景可以提高真实数据的性能。尽管如此，当改变自我车辆姿态时，渲染质量会迅速下降。鉴于我们的发现，即低感知质量（即 LPIPS 和 FID 分数）与较大的真实到模拟差距密切相关，我们认为在推断设置中提高渲染质量仍然是使 NeRF 能够用于测试和改进 AD 系统的关键挑战。</p>
<p><strong>致谢</strong></p>
<p>我们感谢 Adam Tonderski 和 William Ljungbergh 提供宝贵的讨论。这项工作部分由 Knut 和 Alice Wallenberg 基金会资助的 Wallenberg 人工智能、自主系统和软件计划 (WASP) 资助。计算资源由 NAISS 在 NSC Berzelius 提供，部分由瑞典研究委员会资助，协议号。2022-06725。</p>
<p><strong>（7）总结</strong></p>
<p>（1）<strong>本项工作的意义</strong>：提出了一种新颖的视角来解决真实与模拟数据差距问题，通过增强感知模型对 NeRF 伪影的鲁棒性，而不会损害真实数据上的性能。</p>
<p>（2）<strong>本文的优缺点</strong>：
* <strong>创新点</strong>：首次使用最先进的神经渲染技术对自动驾驶场景中的真实与模拟数据差距进行了大规模调查。
* <strong>性能</strong>：提出的方法显着提高了感知模型对模拟数据的鲁棒性，在某些情况下甚至提高了真实世界的性能。
* <strong>工作量</strong>：需要大量的渲染数据和训练时间来实现感知模型的鲁棒性。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-e8445490e4eaaeba826ce93fa44739ab.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-226e40089f23e26b7537bc25c8c4012b.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-d40bf7f142a8199e369826096b0b0904.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-44b007ade1b910cc4a89084343b2e13c.jpg" align="middle">
</details>




