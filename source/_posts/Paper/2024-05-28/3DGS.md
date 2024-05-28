
---
title: 3DGS
date: 2024-05-28 01:55:43
author: Kedreamix
cover: https://pic1.zhimg.com/v2-8db132ec3c58c945a06898a8758b7480.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-05-28  Feature Splatting for Better Novel View Synthesis with Low Overlap  
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

# 2024-05-28 更新


## Feature Splatting for Better Novel View Synthesis with Low Overlap

**Authors:T. Berriel Martins, Javier Civera**

3D Gaussian Splatting has emerged as a very promising scene representation, achieving state-of-the-art quality in novel view synthesis significantly faster than competing alternatives. However, its use of spherical harmonics to represent scene colors limits the expressivity of 3D Gaussians and, as a consequence, the capability of the representation to generalize as we move away from the training views. In this paper, we propose to encode the color information of 3D Gaussians into per-Gaussian feature vectors, which we denote as Feature Splatting (FeatSplat). To synthesize a novel view, Gaussians are first "splatted" into the image plane, then the corresponding feature vectors are alpha-blended, and finally the blended vector is decoded by a small MLP to render the RGB pixel values. To further inform the model, we concatenate a camera embedding to the blended feature vector, to condition the decoding also on the viewpoint information. Our experiments show that these novel model for encoding the radiance considerably improves novel view synthesis for low overlap views that are distant from the training views. Finally, we also show the capacity and convenience of our feature vector representation, demonstrating its capability not only to generate RGB values for novel views, but also their per-pixel semantic labels. We will release the code upon acceptance.   Keywords: Gaussian Splatting, Novel View Synthesis, Feature Splatting 

[PDF](http://arxiv.org/abs/2405.15518v1) 

**Summary**
使用特征splattering（FeatSplat）将3D高斯体的颜色信息编码到每个高斯体的特征向量中，提高了新视图合成的质量和泛化能力。

**Key Takeaways**
• 3D高斯splattering在新视图合成中取得了state-of-the-art的质量，但其使用球谐函数表达场景颜色限制了3D高斯体的表达能力。
• 本文提出将颜色信息编码到每个高斯体的特征向量中，以提高表达能力和泛化能力。
• 特征splattering（FeatSplat）模型包括高斯体的splattering、alpha-blending和解码三个步骤。
• 模型中还加入了相机embedding，以条件解码也基于视点信息。
• 实验结果表明，FeatSplat模型显著提高了低重叠视图的新视图合成质量。
• FeatSplat模型不仅可以生成RGB值，还可以生成每像素的语义标签。
• 将发布代码。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**


1. Title: 特征Splattering用于低重叠视图的新视图合成 (Feature Splatting for Better Novel View Synthesis with Low Overlap)

2. Authors: Tomas Berriel Martins, Javier Civera

3. Affiliation: 扎拉戈萨大学(I3A)

4. Keywords: Gaussian Splatting, Novel View Synthesis, Feature Splatting

5. Urls: arXiv:2405.15518v1, Github:None

6. Summary:


    - (1):该论文的研究背景是寻找适合三维场景表示，以便在机器人、虚拟现实和增强现实应用中使用。


    - (2):过去的方法包括Neural Radiance Fields（NeRFs）和三维高斯Splattering（3DGS），但它们存在一些缺陷，例如NeRFs计算开销高、3DGS使用球谐函数表示场景颜色限制了其表达能力。


    - (3):本文提出了一种新的方法，称为特征Splattering（FeatSplat），它将三维高斯的颜色信息编为每个高斯的特征向量，然后将这些征向量混合并解码以生成RGB像素值。


    - (4):实验结果表明，FeatSplat方法可以显著改善低重叠视图的新视图合成性能，并且可以生成每像素的语义标签，以支持机器人等应用。





8. Conclusion: 

- (1):本文的工作对于三维场景表示和新视图合成具有重要意义，可以应用于机器人、虚拟现实和增强现实等领域。

- (2):Innovation point: 本文提出了一种新的特征Splattering（FeatSplat）方法，弥补了Neural Radiance Fields（NeRFs）和三维高斯Splattering（3DGS）的不足之处； Performance: FeatSplat方法可以生成高质量的新视图，并且可以生成每像素的语义标签； Workload: 本文的方法计算开销相对较低，适合实时应用。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-af9ac9b1d0d353f31971a8ace9ae132b.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-eaee1c783ee42cdf998fdd81f98539e2.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-922abaae68f73855cac3e6cd2f6fb3d0.jpg" align="middle">
</details>




## HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed   via Gaussian Splatting

**Authors:Yuanhao Cai, Zihao Xiao, Yixun Liang, Yulun Zhang, Xiaokang Yang, Yaoyao Liu, Alan Yuille**

High dynamic range (HDR) novel view synthesis (NVS) aims to create photorealistic images from novel viewpoints using HDR imaging techniques. The rendered HDR images capture a wider range of brightness levels containing more details of the scene than normal low dynamic range (LDR) images. Existing HDR NVS methods are mainly based on NeRF. They suffer from long training time and slow inference speed. In this paper, we propose a new framework, High Dynamic Range Gaussian Splatting (HDR-GS), which can efficiently render novel HDR views and reconstruct LDR images with a user input exposure time. Specifically, we design a Dual Dynamic Range (DDR) Gaussian point cloud model that uses spherical harmonics to fit HDR color and employs an MLP-based tone-mapper to render LDR color. The HDR and LDR colors are then fed into two Parallel Differentiable Rasterization (PDR) processes to reconstruct HDR and LDR views. To establish the data foundation for the research of 3D Gaussian splatting-based methods in HDR NVS, we recalibrate the camera parameters and compute the initial positions for Gaussian point clouds. Experiments demonstrate that our HDR-GS surpasses the state-of-the-art NeRF-based method by 3.84 and 1.91 dB on LDR and HDR NVS while enjoying 1000x inference speed and only requiring 6.3% training time. 

[PDF](http://arxiv.org/abs/2405.15125v1) The first 3D Gaussian Splatting-based method for HDR imaging

**Summary**
提出高动态范围Gaussian Splatting（HDR-GS）框架，实现高效 novel view synthesis 和曝光时间可控的低动态范围图像重建。

**Key Takeaways**
• 高动态范围 novel view synthesis（HDR NVS）旨在使用HDR成像技术从新视点生成逼真的图像。
• 现有的HDR NVS方法主要基于NeRF，存在长训练时间和慢推理速度的问题。
• 本文提出高动态范围Gaussian Splatting（HDR-GS）框架，实现高效 novel view synthesis 和曝光时间可控的低动态范围图像重建。
• HDR-GS使用双动态范围（DDR）高斯点云模型和基于MLP的tone-mapper来渲染HDR和LDR颜色。
• 该方法在LDR和HDR NVS任务上超过基于NeRF的方法，且具有1000倍的推理速度和仅需6.3%的训练时间
• 实验结果表明HDR-GS在HDR NVS任务上具有明显的优势。
• 本文为基于3D高斯splattting的HDR NVS方法奠定了数据基础。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**






1. Title: 高动态范围新视图合成（HDR-GS）：基于高斯抹除的高效HDR新视图合成（High Dynamic Range Gaussian Splatting: Efficient HDR Novel View Synthesis via Gaussian Splatting）

2. Authors: Yuanhao Cai, Zihao Xiao, Yixun Liang, Minghan Qin, Yulun Zhang, Xiaokang Yang, Yaoyao Liu, Alan Yuille

3. Affiliation: 约翰斯·霍普金斯大学

4. Keywords: 高动态范围, 新视图合成, 高斯抹除, Novel View Synthesis, HDR, Gaussian Splatting

5. Urls: https://arxiv.org/abs/2405.15125v1, Github: https://github.com/caiyuanhao1998/HDR-GS

6. Summary:


- (1):本文研究背景是高动态范围（HDR）新视图合成（NVS），旨在使用HDR成像技术从新视点生成逼真的图像。


- (2):过去的方法主要基于NeRF，但这些方法存在长训练时间和慢推理速度的问题。


- (3):本文提出的研究方法是High Dynamic Range Gaussian Splatting（HDR-GS），它使用双动态范围（DDR）高斯点云模型和平行可微分光栅化（PDR）过程来高效地渲染HDR和LDR视图。


- (4):本文方法在HDR和LDR新视图合成任务上优于基于NeRF的方法，达到了3.84和1.91 dB的PSNR性能，并且具有1000倍的推理速度和仅需6.3%的训练时间
7. 方法：

- (1):提出双动态范围（DDR）高斯点云模型，用于表示高动态范围（HDR）图像的颜色和深度信息，该模型由高斯分布函数和点云数据组成。

- (2):使用平行可微分光栅化（PDR）过程将DDR高斯点云模型转换为高效的渲染表示，以便快速生成HDR和LDR视图。

- (3):设计高斯抹除（Gaussian Splatting）算法，用于将DDR高斯点云模型投影到目标视图平面上，生成高质量的HDR和LDR图像。

- (4):提出基于高斯抹除的新视图合成（Novel View Synthesis）方法，用于从给定的HDR图像中生成意视点的HDR和LDR图像。

- (5):使用基于NeRF的方法作为基线，比较HDR-GS方法在HDR和LDR新视图合成任务上的性能，结果表明HDR-GS方法具有更高的PSNR性能和更快的推理速度。

- (6):通过实验验证HDR-GS方法的有效性和高效性，结果表明HDR-GS方法能够生成高质量的HDR和LDR图像，并且具有实时渲染的能力。





8. Conclusion:


- (1):该研究工作的重要性在于解决了高动态范围（HDR）新视图合成中的效率问题，实现了高质量的HDR图像渲染和快速推理速度，具有广泛的应用前景在计算机视觉、图形学和机器学习等领域。


- (2):创新点：提出了一种基于高斯抹除的高效HDR新视图合成方法HDR-GS，解决了基于NeRF方法的长训练时间和慢推理速度问题；性能：在HDR和LDR新视图合成任务上，HDR-GS方法具有更高的PSNR性能和更快的推理速度；工作量：HDR-GS方法仅需6.3%的训练时间和1000倍的推理速度，具有实时渲染的能力。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-62274faaed9878e5e0161dea6f18dbbe.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1eb56bf3e6d513a6248b50e7a8d0c539.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-a6cf6e245e96bb903d2b486b7727c24e.jpg" align="middle">
</details>




## GS-Hider: Hiding Messages into 3D Gaussian Splatting

**Authors:Xuanyu Zhang, Jiarui Meng, Runyi Li, Zhipei Xu, Yongbing Zhang, Jian Zhang**

3D Gaussian Splatting (3DGS) has already become the emerging research focus in the fields of 3D scene reconstruction and novel view synthesis. Given that training a 3DGS requires a significant amount of time and computational cost, it is crucial to protect the copyright, integrity, and privacy of such 3D assets. Steganography, as a crucial technique for encrypted transmission and copyright protection, has been extensively studied. However, it still lacks profound exploration targeted at 3DGS. Unlike its predecessor NeRF, 3DGS possesses two distinct features: 1) explicit 3D representation; and 2) real-time rendering speeds. These characteristics result in the 3DGS point cloud files being public and transparent, with each Gaussian point having a clear physical significance. Therefore, ensuring the security and fidelity of the original 3D scene while embedding information into the 3DGS point cloud files is an extremely challenging task. To solve the above-mentioned issue, we first propose a steganography framework for 3DGS, dubbed GS-Hider, which can embed 3D scenes and images into original GS point clouds in an invisible manner and accurately extract the hidden messages. Specifically, we design a coupled secured feature attribute to replace the original 3DGS's spherical harmonics coefficients and then use a scene decoder and a message decoder to disentangle the original RGB scene and the hidden message. Extensive experiments demonstrated that the proposed GS-Hider can effectively conceal multimodal messages without compromising rendering quality and possesses exceptional security, robustness, capacity, and flexibility. Our project is available at: https://xuanyuzhang21.github.io/project/gshider. 

[PDF](http://arxiv.org/abs/2405.15118v1) 3DGS steganography

**Summary**
三维高斯分裂（3DGS）隐写术框架GS-Hider，实现了对原始3DGS点云文件的隐写和提取。

**Key Takeaways**
• 3DGS需要保护版权、完整性和隐私，因为训练需要大量时间和计算成本。
• 3DGS具有显式3D表示和实时渲染速度，导致点云文件公开透明，具有明确的物理意义。
• GS-Hider框架可以将3D场景和图像嵌入到原始GS点云中，以不可见的方式提取隐藏的消息。
• GS-Hider使用耦合安全特征属性替换原始3DGS的球谐系数，并使用场景解码器和消解码器来分离原始RGB场景和隐藏消息。
• 实验表明，GS-Hider可以有效地隐藏多模式消息，而不影响渲染质量，具有异常的安全性、鲁棒性、容量和灵活性。
• GS-Hider项目可在https://xuanyuzhang21.github.io/project/gshider上访问。
• GS-Hider框架可以保护3DGS的版权、完整性和隐私。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**






1. Title: GS-Hider：隐藏消息到3D高斯点云（GS-Hider: Hiding Messages into 3D Gaussian Splatting）

2. Authors: Xuanyu Zhang, Jiarui Meng, Runyi Li, Zhipei Xu, Yongbing Zhang, Jian Zhang

3. Affiliation: 电子与计算机工程学院，北京大学（School of Electronic and Computer Engineering, Peking University）

4. Keywords: 3D高斯点云、隐写术、数字水印、copyright protection

5. Urls: https://arxiv.org/abs/2405.15118, Github: https://xuanyuzhang21.github.io/project/gshider/

6. Summary:


- (1):本文的研究背景是保护3D场景重建和新视图合成中的数字资产的版权和隐私，特别是基于3D高斯点云（3DGS）的方法。

- (2):过去的隐写术方法主要使用傅里叶和小波变换来嵌入消息，但是这些方法不能很好地适应3DGS的特点，例如明确的3D表示和实时渲染速度。

- (3):本文提出了一个名为GS-Hider的隐写术框架，使用耦合的安全特征属性来替换原始3DGS的球谐系数，然后使用场景解码器和消息解码器来分离原始RGB场景和隐藏的消息。

- (4):实验结果表明，GS-Hider可以在不影响渲染质量的情况下隐藏多模态消息，并且具有非常高的安全性、鲁棒性、容量和灵活性。
7. 方法：

- (1)：首先，作者们提出了基于耦合安全特征属性的隐写术框架GS-Hider，该框架可以将消息隐藏在3D高斯点云（3DGS）中。

- (2)：在GS-Hider框架中，作者们使用耦合的安全特征属性来替换原始3DGS的球谐系数，具体来说，就是将消息嵌入到球谐系数中。

- (3)：然后，作者们使用场景解码器和消息解码器来分离原始RGB场景和隐藏的消息，这两个解码器都是基于深度学习的神经网络。

- (4)：在消息嵌入过程中，作者们使用了anisotropic Gaussians表示场景，通过splattin技术将3D高斯点云投影到图像平面上，并使用经点基于渲染来生成图像。

- (5)：为了提高消息的安全性和鲁棒性，作者们使用了多种技术，包括DIFFusion-based方法和Frequency-based方法来保护消息抵抗攻击。

- (6)：在实验中，作者们使用了多种数据集和评估指标来评估GS-Hider的性能，结果表明GS-Hider可以在不影响渲染质量的情况下隐藏多模态消息，并且具有非常高的安全性、鲁棒性、容量和灵活性。





8. Conclusion:

- (1): 本文的工作意义在于提出了一种高保真、安全、大容量和多功能的3D高斯点云隐写术框架，即GS-Hider，为保护3D场景重建和新视图合成中的数字资产版权和隐私提供了有效的技术支持。

- (2): 创新点：GS-Hider框架利用耦合的安全特征表示和双解码器解码技术，实现了在3D高斯点云中隐藏消息，具有很高的安全性、鲁棒性和灵活性；性能：实验结果表明GS-Hider在不影响渲染质量的情况下可以隐藏多模态消息，且具有高容量；工作量：文章未详细说明具体的工作量评估，需要进一步补充和完善。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-44535b4dc9ae919b2dce80a4be050e9a.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-bbb3c977263acb314ebe7c8c3a9043c9.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-9e7d4ae3f321d6e860ec2da2743463f2.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-8db132ec3c58c945a06898a8758b7480.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-51183cc617b206934e4fdaaba05fdc46.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-c5422ed30935cd238fd580f363ae7ec2.jpg" align="middle">
</details>




## DoGaussian: Distributed-Oriented Gaussian Splatting for Large-Scale 3D   Reconstruction Via Gaussian Consensus

**Authors:Yu Chen, Gim Hee Lee**

The recent advances in 3D Gaussian Splatting (3DGS) show promising results on the novel view synthesis (NVS) task. With its superior rendering performance and high-fidelity rendering quality, 3DGS is excelling at its previous NeRF counterparts. The most recent 3DGS method focuses either on improving the instability of rendering efficiency or reducing the model size. On the other hand, the training efficiency of 3DGS on large-scale scenes has not gained much attention. In this work, we propose DoGaussian, a method that trains 3DGS distributedly. Our method first decomposes a scene into K blocks and then introduces the Alternating Direction Method of Multipliers (ADMM) into the training procedure of 3DGS. During training, our DoGaussian maintains one global 3DGS model on the master node and K local 3DGS models on the slave nodes. The K local 3DGS models are dropped after training and we only query the global 3DGS model during inference. The training time is reduced by scene decomposition, and the training convergence and stability are guaranteed through the consensus on the shared 3D Gaussians. Our method accelerates the training of 3DGS by 6+ times when evaluated on large-scale scenes while concurrently achieving state-of-the-art rendering quality. Our project page is available at https://aibluefisher.github.io/DoGaussian. 

[PDF](http://arxiv.org/abs/2405.13943v1) 

**Summary**
最近对3D高斯点云（3DGS）的研究显示了在新视图合成（NVS）任务上取得了令人期待的成果。 

**Key Takeaways**
- 3DGS在渲染性能和保真度方面表现优越，优于以往的NeRF方法。
- 最近的3DGS方法要么专注于改善渲染效率的不稳定性，要么减小模型尺寸。
- 本文提出了DoGaussian方法，该方法通过将场景分解为K个块，并引入交替方向乘子法（ADMM）来分布式训练3DGS。
- DoGaussian方法通过场景分解缩短了训练时间，同时确保了训练的收敛性和稳定性。
- 训练时间缩短了6倍以上，同时在大规模场景上实现了最先进的渲染质量。
- 项目页面链接：https://aibluefisher.github.io/DoGaussian。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**






1. Title: DoGaussian：分布式面向高斯斯普拉特（Distributed-Oriented Gaussian Splatting）


2. Authors: Yu Chen, Gim Hee Lee


3. Affiliation: 新加坡国立大学


4. Keywords: 3D Gaussian Splatting, Novel View Synthesis, Distributed Training


5. Urls: https://arxiv.org/abs/2405.13943v1, Github: None


6. Summary:


    - (1):近年来，三维高斯斯普拉特（3DGS）在新视图合成（NVS）任务中取得了良好的结果，然而，当前3DGS方法的训练效率在大规模场景下尚未受到足够的关注。


    - (2):之前的方法主要集中在提高渲染效率的不稳定性或减少模型大小，但这些方法忽视了大规模场景下的训练效率问题。


    - (3):本文提出了DoGaussian方法，该方法将场景分解成K个块，然后引入交替方向乘子法（ADMM）到3DGS的训练过程中。在训练过程中，DoGaussian在主节点上维护一个全局的3DGS模型，在从节点上维护K个局部的3DGS模型


    - (4):DoGaussian方在大规模场景下加速了3DGS的训练速度，达到了6倍以上的加速，同时也获得了最先进的渲染质量。
7. 方法：

- (1)：将场景分解成 K 个块，以便分布式训练。在每个块中，分配训练视图和点云数据。

- (2)：引入 Alternating Direction Method of Multipliers（ADMM）算法，在分布式训练中实现全局一致的 3D Gaussian Splatting 模型。在每个块中，维护一个局部的 3D Gaussian Splatting 模型，并与主节点上的全局模型进行交互。

- (3)：在每个块中，使用 ADMM 算法更新局部模型，并将更新后的模型与主节点上的全局模型进行平均，以实现模型的一致性。

- (4)：在训练过程中，使用 Penalty Parameter 和 Over-relaxation 技术来提高 ADMM 算法的收敛速度。

- (5)：使用场景分割算法，以确保每个块的大小相似，并且相邻块之间有足够的重叠区域，以促进训练的收敛。

- (6)：在训练完成后，使用全局模型来合成新视图，以实现高质量的渲染结果。

- (7)：实验结果表明，提出的 DoGaussian 方法可以在大规模场景下加速 3D Gaussian Splatting 的训练速度，达到了 6 倍以上的加速，同时也获得了最先进的渲染质量。





8. Conclusion: 

- (1):本文的贡献在于解决了三维高斯斯普拉特（3DGS）在大规模场景下的训效率问题，提高了新视图合成（NVS）的实时性和质量。

- (2):创新点：提出了一种分布式训练方法DoGaussian，使用Alternating Direction Method of Multipliers（ADMM）算法实现全局一致的3DGS模型；性能：加速了3DGS的训练速度，达到了6倍以上的加速，同时也获得了最先进的渲染质量；工作量：需要大量的计算资源和场景分割算法来实现分布式训练。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-22c8c9dbbe8897a84779859d7460a6eb.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-261a3638b92396cc85c1385cc6c53581.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-4e3e352a0325ce88ecaee52f7e182708.jpg" align="middle">
</details>




## Gaussian Time Machine: A Real-Time Rendering Methodology for   Time-Variant Appearances

**Authors:Licheng Shen, Ho Ngai Chow, Lingyun Wang, Tong Zhang, Mengqiu Wang, Yuxing Han**

Recent advancements in neural rendering techniques have significantly enhanced the fidelity of 3D reconstruction. Notably, the emergence of 3D Gaussian Splatting (3DGS) has marked a significant milestone by adopting a discrete scene representation, facilitating efficient training and real-time rendering. Several studies have successfully extended the real-time rendering capability of 3DGS to dynamic scenes. However, a challenge arises when training images are captured under vastly differing weather and lighting conditions. This scenario poses a challenge for 3DGS and its variants in achieving accurate reconstructions. Although NeRF-based methods (NeRF-W, CLNeRF) have shown promise in handling such challenging conditions, their computational demands hinder real-time rendering capabilities. In this paper, we present Gaussian Time Machine (GTM) which models the time-dependent attributes of Gaussian primitives with discrete time embedding vectors decoded by a lightweight Multi-Layer-Perceptron(MLP). By adjusting the opacity of Gaussian primitives, we can reconstruct visibility changes of objects. We further propose a decomposed color model for improved geometric consistency. GTM achieved state-of-the-art rendering fidelity on 3 datasets and is 100 times faster than NeRF-based counterparts in rendering. Moreover, GTM successfully disentangles the appearance changes and renders smooth appearance interpolation. 

[PDF](http://arxiv.org/abs/2405.13694v1) 14 pages, 6 figures

**Summary**
利用高斯时间机GTM实现实时三维重建，解决weather和lighting条件变化带来的挑战。

**Key Takeaways**
• 三维高斯Splatting（3DGS）技术的出现标志着三维重建的重要里程碑。
• 3DGS及其变体在实时渲染动态场景方面取得了成功，但是在不同天气和照明条件下训练图像时存在挑战。
• NeRF-based方法（NeRF-W、CLNeRF）可以处理这种挑战，但计算需求高，影响实时渲染能力。
• 高斯时间机GTM使用轻量级MLP模型时间嵌入矢量来模拟高斯primitive的时间依赖属性。
• GTM可以重建对象的可见性变化，并且具有更好的几何一致性。
• GTM在三个数据集上的渲染保真度达到最好，并且染速度是NeRF-based方法的100倍。
• GTM成功地分离了外观变化，并实现了平滑的外观插值。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**






1. Title: 高斯时间机器：实时渲染时间变换外观 (Gaussian Time Machine: A Real-Time Rendering Methodology for Time-Variant Appearances)


2. Authors: Licheng Shen, Ho Ngai Chow, Lingyun Wang, Tong Zhang, Mengqiu Wang, Yuxing Han


3. Affiliation: 清华大学深圳国际研究生院


4. Keywords: Neural Rendering · 3D Gaussian Splatting · Varying Appearance


5. Urls: arXiv:2405.13694v1, Github:None


6. Summary:


    - (1):近年来，神经渲染技术的发展极大地提高了三维重建的保真度。特别是，三维高斯点绘制（3DGS）提出了离散场景表示，提高了训练速度和实时渲染质量。
    
    - (2):过去的方法如NeRF-W和CLNeRF可以处理复杂的天气和照明条件，但是它们的计算需求限制了实时渲染能力。3DGS和其变体也存在着准确重建的挑战。
    
    - (3):本文提出了高斯时间机器（GTM），它使用离散时间嵌入向量和轻量级多层感知器（MLP）来建模高斯primitive的时间相关属性。通过调整高斯primitive的不透明度，可以重建对象的可见性变化。
    
    - (4):GTM在三个数据集上实现了最先进的渲染保真度，渲染速度是NeRF-based方法的100倍。此外，GTM还成功地分离了外观变化并实现了平滑的外观插值。
7. Methods:

- (1): 本文提出的高斯时间机器（Gaussian Time Machine，GTM）采用离散时间嵌入向量和轻量级多层感知器（MLP）来建模高斯primitive的时间相关属性。

- (2): GTM通过调整高斯primitive的不透明度，实现了对象可见性的变化，并成功地分离了外观变化。
  
- (3): 在三个数据集上，GTM展现出了最先进的渲染保真度，且渲染速度是基于NeRF的方法的100倍。此外，GTM还能够实现平滑的外观插值。





8. Conclusion:

- (1):本文提出的高斯时间机器（Gaussian Time Machine，GTM）在解决时间变换外观问题方面具有重要意义，可以应用于虚拟现实、数字孪生等领域。

- (2):创新点：GTM 提出了离散时间嵌入向量和轻量级多层感知器（MLP）来建模高斯primitive的时间相关属性，实现了对象可见性的变化和外观变化的分离；性能：GTM 在三个数据集上实现了最先进的渲染保真度，渲染速度是 NeRF-based 方法的 100 倍；工作量：GTM 需要较少的计算资源和训练时间，能够实现实时渲染。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-e37e39f80d95d9753e062031ea071292.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-8d45eb05bc11e95b4d1a05a781ee482b.jpg" align="middle">
</details>




## GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting   Editing with Image Prompting

**Authors:Haodong Chen, Yongle Huang, Haojian Huang, Xiangsheng Ge, Dian Shao**

The increasing prominence of e-commerce has underscored the importance of Virtual Try-On (VTON). However, previous studies predominantly focus on the 2D realm and rely heavily on extensive data for training. Research on 3D VTON primarily centers on garment-body shape compatibility, a topic extensively covered in 2D VTON. Thanks to advances in 3D scene editing, a 2D diffusion model has now been adapted for 3D editing via multi-viewpoint editing. In this work, we propose GaussianVTON, an innovative 3D VTON pipeline integrating Gaussian Splatting (GS) editing with 2D VTON. To facilitate a seamless transition from 2D to 3D VTON, we propose, for the first time, the use of only images as editing prompts for 3D editing. To further address issues, e.g., face blurring, garment inaccuracy, and degraded viewpoint quality during editing, we devise a three-stage refinement strategy to gradually mitigate potential issues. Furthermore, we introduce a new editing strategy termed Edit Recall Reconstruction (ERR) to tackle the limitations of previous editing strategies in leading to complex geometric changes. Our comprehensive experiments demonstrate the superiority of GaussianVTON, offering a novel perspective on 3D VTON while also establishing a novel starting point for image-prompting 3D scene editing. 

[PDF](http://arxiv.org/abs/2405.07472v2) On-going work

**Summary**
电子商务的日益突出彰显了虚拟试穿（VTON）的重要性。本文提出了GaussianVTON，将高斯点绘制（GS）编辑与2D VTON相结合，首次提出使用图像作为3D编辑提示，以及引入了ERR编辑策略，为3D VTON提供了新视角。

**Key Takeaways**
- 电子商务的日益突出彰显了虚拟试穿（VTON）的重要性。
- GaussianVTON将高斯点绘制（GS）编辑与2D VTON相结合，首次提出使用图像作为3D编辑提示。
- 通过三阶段的精细化策略逐步缓解潜在问题，进一步解决了面部模糊、服装不准确和编辑过程中视角质量下降等问题。
- 引入了ERR编辑策略来应对之前编辑策略的局限性，解决了复杂几何变化带来的问题。
- 实验结果显示，GaussianVTON具有卓越性能，为3D VTON提供了新视角，并建立了图像提示3D场景编辑的新起点。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**


1. Title: 高斯 Virtual Try-On：基于多阶段高斯 Splatting 的 3D 人体虚拟试衣（GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting）

2. Authors: Haodong Chen, Yongle Huang, Haojian Huang, Xiangsheng Ge, Dian Shao

3. Affiliation: 西北工业大学

4. Keywords: Virtual Try-On, 3D Human, Gaussian Splatting, Image Prompting

5. Urls: https://haroldchen19.github.io/gsvton/, Github:None

6. Summary:

    - (1):随着电子商务的兴起，虚拟试衣（Virtual Try-On, VTON）变得越来越重要。然而，之前的研究主要集中在 2D 领域，并且需要大量的训练数据。

    - (2):过去的方法主要集中在 2D VTON 领域，并且需要大量的训练数据。这些方法无法很好地解决 3D VTON 问题，例如服装形状与人体形状的不兼容问题

    - (3):本文提出了 GaussianVTON，一种基于多阶段高斯 Splatting 的 3D VTON 管道。该方法使用图像作为编辑提示，实现了从 2D 到 3D VTON 的无缝过渡。

    - (4):实验结果表明，GaussianVTON 方法在 3D VTON 任务上取得了优异的性能，证明了该方法的有效性。
7. 方法：

- (1)：输入重建的 3D 场景和相应的数据，包括一系列拍摄的图像、相应的相机姿态和相机标定参数。

- (2)：使用图像编辑提示来指导 3D 场景的编辑过程，以实现虚拟试衣。首先，引入 3D 高斯 Splatting 模型和基于扩散的 2D VTON 模型。

- (3)：提出了 Editing Recall Reconstruction (ERR) 策略，该策略在编辑过程中渲染整个数据集，以解决编辑不一致的问题。

- (4)：采用三阶段细化策略，包括人脸一致性、层次稀疏编辑和图像质量改进三个阶段，以解决编辑过程中遇到的各种问题。

- (5)：在 ERR 策略中，对整个数据集进行编辑和细化，然后对数据集进行更新，以确保编辑的一致性。

- (6)：使用 LaDI-VTON 模型对每个图像进行编辑，并将编辑结果与原始图像进行比较，以评估编辑的效果。

- (7)：对编辑结果进行可视化和评估，以验证 GaussianVTON 方法的有效性。





8. Conclusion: 

                    - (1):本文的工作对电子商务虚拟试衣领域的发展具有重要意义，可以为用户提供更加真实的试衣体验。
                    
                    - (2):创新点：本文提出了一种基于多阶段高斯 Splatting 的 3D 人体虚拟试衣方法，解决了 2D 到 3D 虚拟试衣的技术瓶颈；性能：实验结果表明，GaussianVTON 方法在 3D VTON 任务上取得了优异的性能；工作量：本文的方法需要大量的训练数据和计算资源，限制了其在实际应用中的普及性。







<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-e12873404001a9a09d996899cdfe1fc3.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-c590805a84c00f53de63efe5b169e438.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-28127860f8d303f51aff59430d547019.jpg" align="middle">
</details>




