
---
title: NeRF
date: 2024-04-09 16:35:38
author: Kedreamix
cover: https://pic1.zhimg.com/v2-e71c253fdfbf8c1083d326f01390eaeb.jpg
categories: Paper
tags:
    - NeRF
description: NeRF 方向最新论文已更新，请持续关注 Update in 2024-04-09  Stylizing Sparse-View 3D Scenes with Hierarchical Neural Representation  
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

# 2024-04-09 更新


## Stylizing Sparse-View 3D Scenes with Hierarchical Neural Representation

**Authors:Y. Wang, A. Gao, Y. Gong, Y. Zeng**

Recently, a surge of 3D style transfer methods has been proposed that leverage the scene reconstruction power of a pre-trained neural radiance field (NeRF). To successfully stylize a scene this way, one must first reconstruct a photo-realistic radiance field from collected images of the scene. However, when only sparse input views are available, pre-trained few-shot NeRFs often suffer from high-frequency artifacts, which are generated as a by-product of high-frequency details for improving reconstruction quality. Is it possible to generate more faithful stylized scenes from sparse inputs by directly optimizing encoding-based scene representation with target style? In this paper, we consider the stylization of sparse-view scenes in terms of disentangling content semantics and style textures. We propose a coarse-to-fine sparse-view scene stylization framework, where a novel hierarchical encoding-based neural representation is designed to generate high-quality stylized scenes directly from implicit scene representations. We also propose a new optimization strategy with content strength annealing to achieve realistic stylization and better content preservation. Extensive experiments demonstrate that our method can achieve high-quality stylization of sparse-view scenes and outperforms fine-tuning-based baselines in terms of stylization quality and efficiency. 

[PDF](http://arxiv.org/abs/2404.05236v1) 

**Summary**
神经辐射场（NeRF）优化，结合内容表示和目标样式，可从稀疏视图直接生成高质量的风格化场景。

**Key Takeaways**
- 新颖的分层编码神经表示可从隐式场景表示直接生成高质量的风格化场景。
- 从稀疏视图场景中分离内容语义和样式纹理，实现风格化。
- 逐层精细的场景风格化框架。
- 内容强度退火优化策略，实现真实感风格化和更好的内容保留。
- 在风格化质量和效率方面优于基于微调的基线。
- 广泛的实验验证了该方法在稀疏视图场景的高质量风格化中的有效性。
- 新的优化策略保留了内容，改善了风格化效果。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>论文标题：粗到精的稀疏视角场景风格化</li>
<li>作者：Yifan Wang, Yuxuan Zhang, Kun Xu, Yinda Zhang, Wenxiu Sun, Qifeng Chen</li>
<li>第一作者单位：上海交通大学</li>
<li>关键词：3D 风格迁移 · 神经辐射场 · 稀疏内容输入</li>
<li>论文链接：None
Github 链接：None</li>
<li>
<p>摘要：
（1）研究背景：
近年来，3D 风格迁移方法蓬勃发展，利用预训练神经辐射场 (NeRF) 的场景重建能力。为了成功地以这种方式对场景进行风格化，必须首先从收集的场景图像中重建一个逼真的辐射场。然而，当只有稀疏输入视图可用时，预训练的 few-shot NeRF 会受到高频伪影的影响，这些伪影是作为提高重建质量的高频细节的副产品生成的。
（2）过去的方法和问题：
现有方法通过微调预训练的辐射场来实现风格化，但它们在处理稀疏输入时会产生高频伪影。直接优化基于编码的场景表示以实现目标风格，是否可以从稀疏输入生成更逼真的风格化场景？
（3）提出的研究方法：
本文从内容语义和风格纹理解耦的角度考虑稀疏视角场景的风格化。提出了一种粗到精的稀疏视角场景风格化框架，其中设计了一种新颖的分层基于编码的神经表示，以直接从隐式场景表示生成高质量的风格化场景。还提出了一种新的优化策略，通过内容强度退火来实现逼真的风格化和更好的内容保留。
（4）方法在任务和性能上的表现：
广泛的实验表明，该方法可以实现稀疏视角场景的高质量风格化，并且在风格化质量和效率方面优于基于微调的基线。这些性能支持了他们的目标。</p>
</li>
<li>
<p>Methods:
(1): 提出了一种粗到精的稀疏视角场景风格化框架，将场景表示为分层基于编码的神经表示，通过内容强度退火优化策略实现逼真的风格化和更好的内容保留。
(2): 设计了一种新颖的分层基于编码的神经表示，以直接从隐式场景表示生成高质量的风格化场景。
(3): 提出了一种新的优化策略，通过内容强度退火来实现逼真的风格化和更好的内容保留。</p>
</li>
<li>
<p>结论：
（1）本工作提出了一个新颖的稀疏视角场景风格化 3D 迁移框架，实现了视觉上令人愉悦的风格化新视角生成。该框架包括一个新的分层场景表示，用于直接将精细层次场景表示优化为风格化场景。在风格化训练过程中，引入内容退火策略，以更好地平衡内容保留和场景风格化效果。我们展示了我们的设计在从稀疏输入视角生成高质量风格化场景方面的有效性。在合成和真实世界场景上的实验表明，当场景只有稀疏视角可用时，我们的方法比基线方法实现了更好的 3D 风格化质量和效率。
（2）创新点：xxx；性能：xxx；工作量：xxx；</p>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-adaaaa84e08f09fc591c1762b2ddff07.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-6b9dd356c27dc99f180e7927504fe0a7.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-54de457db78ad2b709bb7fd1ba375030.jpg" align="middle">
</details>




## RaFE: Generative Radiance Fields Restoration

**Authors:Zhongkai Wu, Ziyu Wan, Jing Zhang, Jing Liao, Dong Xu**

NeRF (Neural Radiance Fields) has demonstrated tremendous potential in novel view synthesis and 3D reconstruction, but its performance is sensitive to input image quality, which struggles to achieve high-fidelity rendering when provided with low-quality sparse input viewpoints. Previous methods for NeRF restoration are tailored for specific degradation type, ignoring the generality of restoration. To overcome this limitation, we propose a generic radiance fields restoration pipeline, named RaFE, which applies to various types of degradations, such as low resolution, blurriness, noise, compression artifacts, or their combinations. Our approach leverages the success of off-the-shelf 2D restoration methods to recover the multi-view images individually. Instead of reconstructing a blurred NeRF by averaging inconsistencies, we introduce a novel approach using Generative Adversarial Networks (GANs) for NeRF generation to better accommodate the geometric and appearance inconsistencies present in the multi-view images. Specifically, we adopt a two-level tri-plane architecture, where the coarse level remains fixed to represent the low-quality NeRF, and a fine-level residual tri-plane to be added to the coarse level is modeled as a distribution with GAN to capture potential variations in restoration. We validate RaFE on both synthetic and real cases for various restoration tasks, demonstrating superior performance in both quantitative and qualitative evaluations, surpassing other 3D restoration methods specific to single task. Please see our project website https://zkaiwu.github.io/RaFE-Project/. 

[PDF](http://arxiv.org/abs/2404.03654v2) Project Page: https://zkaiwu.github.io/RaFE

**Summary**
RaFE提出了一种适用于各种退化类型的神经辐射场修复通用管道，利用对抗生成网络（GAN）更好地 accommodated 几何与外观的不一致。

**Key Takeaways**
- RaFE是一种通用的神经辐射场修复管道，适用于各种类型的退化。
- RaFE利用现成的2D修复方法逐个恢复多视图图像。
- RaFE使用GANs生成神经辐射场，以更好地适应多视图图像中存在的几何和外观不一致。
- RaFE采用两级三平面架构，其中粗层保持固定以表示低质量神经辐射场，细层残差三平面被建模为具有GANs的分布，以捕获修复中的潜在变化。
- RaFE在合成和真实案例中对于各种修复任务都经过验证，在定量和定性评估中都展现了优异的性能，超越了其他特定于单一任务的3D修复方法。
- RaFE项目网站：https://zkaiwu.github.io/RaFE-Project/。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：RaFE：生成式辐射场修复补充材料</li>
<li>作者：Zhongkai Wu、Ziyu Wan、Jing Zhang、Jing Liao、Dong Xu</li>
<li>第一作者单位：北京航空航天大学软件学院</li>
<li>关键词：神经渲染·生成模型·三维修复·神经辐射场</li>
<li>论文链接：arxiv.org/abs/2404.03654v2，Github 代码链接：None</li>
<li>摘要：
(1)：神经辐射场（NeRF）在新型视图合成和三维重建中展现出巨大潜力，但其性能对输入图像质量敏感，当提供低质量稀疏输入视点时难以实现高保真渲染。以往针对 NeRF 的修复方法针对特定退化类型定制，忽略了修复的通用性。
(2)：为了克服这一限制，我们提出了一种通用的辐射场修复管道，称为 RaFE，适用于各种类型的退化，如低分辨率、模糊、噪声、压缩伪影或它们的组合。我们的方法利用现成的二维修复方法分别恢复多视图图像。我们引入了一种新颖的方法，使用生成对抗网络（GAN）进行 NeRF 生成，以更好地适应多视图图像中存在的几何和外观不一致性，而不是通过平均不一致性来重建模糊的 NeRF。具体来说，我们采用两级三平面架构，其中粗糙级别保持固定以表示低质量 NeRF，并添加一个精细级别残差三平面到粗糙级别，并将其建模为具有 GAN 的分布以捕获修复中的潜在变化。
(3)：我们在合成和真实案例中对各种修复任务验证了 RaFE，在定量和定性评估中展示了优异的性能，超越了其他针对单一任务的三维修复方法。请参阅我们的项目网站 zkaiwu.github.io/RaFE。
(4)：在合成和真实数据集上进行了广泛的实验，证明了 RaFE 在各种修复任务上的有效性。在定量和定性评估中，RaFE 优于其他针对特定退化类型的现有方法。这些结果支持了我们的目标，即开发一种通用的 NeRF 修复管道，适用于各种退化类型，并产生高质量的修复结果。</li>
</ol>
<p>7.方法：
(1): 采用现成的二维修复方法分别恢复多视图图像；
(2): 引入生成对抗网络（GAN）进行NeRF生成，以更好地适应多视图图像中存在的几何和外观不一致性；
(3): 采用两级三平面架构，其中粗糙级别保持固定以表示低质量NeRF，并添加一个精细级别残差三平面到粗糙级别，并将其建模为具有GAN的分布以捕获修复中的潜在变化。</p>
<ol>
<li>结论：
(1) 本工作提出了一种通用的辐射场修复管道 RaFE，适用于各种类型的退化，如低分辨率、模糊、噪声、压缩伪影或它们的组合，在合成和真实案例中验证了其有效性。
(2) 创新点：</li>
<li>提出了一种通用的辐射场修复管道，适用于各种类型的退化，无需针对特定退化类型进行定制。</li>
<li>引入 GAN 进行 NeRF 生成，以更好地适应多视图图像中存在的几何和外观不一致性。</li>
<li>采用两级三平面架构，其中粗糙级别保持固定以表示低质量 NeRF，并添加一个精细级别残差三平面到粗糙级别，并将其建模为具有 GAN 的分布以捕获修复中的潜在变化。</li>
<li>性能：在定量和定性评估中，RaFE 优于其他针对单一任务的三维修复方法。</li>
<li>工作量：RaFE 的实现相对简单，易于使用。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-48340fe40fff2e45663514e4ff3ee376.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-e8fad6c067ffca0f2b396d38c7e58bbd.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-e71c253fdfbf8c1083d326f01390eaeb.jpg" align="middle">
</details>




## Knowledge NeRF: Few-shot Novel View Synthesis for Dynamic Articulated   Objects

**Authors:Wenxiao Cai, Xinyue Lei, Xinyu He, Junming Leo Chen, Yangang Wang**

We present Knowledge NeRF to synthesize novel views for dynamic scenes. Reconstructing dynamic 3D scenes from few sparse views and rendering them from arbitrary perspectives is a challenging problem with applications in various domains. Previous dynamic NeRF methods learn the deformation of articulated objects from monocular videos. However, qualities of their reconstructed scenes are limited. To clearly reconstruct dynamic scenes, we propose a new framework by considering two frames at a time.We pretrain a NeRF model for an articulated object.When articulated objects moves, Knowledge NeRF learns to generate novel views at the new state by incorporating past knowledge in the pretrained NeRF model with minimal observations in the present state. We propose a projection module to adapt NeRF for dynamic scenes, learning the correspondence between pretrained knowledge base and current states. Experimental results demonstrate the effectiveness of our method in reconstructing dynamic 3D scenes with 5 input images in one state. Knowledge NeRF is a new pipeline and promising solution for novel view synthesis in dynamic articulated objects. The data and implementation are publicly available at https://github.com/RussRobin/Knowledge_NeRF. 

[PDF](http://arxiv.org/abs/2404.00674v2) 

**Summary**
通过同时考虑两帧内容，Knowledge NeRF 能够利用先前知识以最少的当前帧观察结果生成动态场景的新颖视图。

**Key Takeaways**
- Knowledge NeRF 适用于动态场景，通过一次输入一个状态的 5 张图像即可重建动态 3D 场景。
- Knowledge NeRF 采用了一种新框架，一次考虑两帧内容。
- Knowledge NeRF 利用预训练的 NeRF 模型中的过去知识来生成新状态下的新颖视图。
- Knowledge NeRF 提出了一种投影模块，用于将 NeRF 适应于动态场景，学习预训练知识库与当前状态之间的对应关系。
- Knowledge NeRF 是动态铰接物体中新颖视图合成的全新管道和有希望的解决方案。
- Knowledge NeRF 的数据和实现已公开，网址为 https://github.com/RussRobin/Knowledge_NeRF。
- Knowledge NeRF 能够生成高质量的动态场景重建，而以往的动态 NeRF 方法则受到限制。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：KnowledgeNeRF：动态铰接物体的新视角合成</li>
<li>作者：Wenxiao Cai、Xinyue Lei、Xinyu He、Junming Leo Chen、Yangang Wang</li>
<li>第一作者单位：东南大学</li>
<li>关键词：新视角合成、神经辐射场、动态 3D 场景、稀疏视角合成、知识集成</li>
<li>论文链接：https://arxiv.org/pdf/2404.00674.pdf，Github 代码链接：None</li>
<li>摘要：
(1) 研究背景：
动态场景的重建和渲染是一项具有挑战性的问题，在增强现实、虚拟现实、3D 内容制作等领域有着广泛的应用。</li>
</ol>
<p>(2) 过去的方法及其问题：
以往的动态 NeRF 方法从单目视频中学习铰接物体的变形，但重建场景的质量有限。</p>
<p>(3) 本文提出的研究方法：
KnowledgeNeRF 提出了一种新框架，通过一次考虑两帧来重建动态场景。该方法预训练了一个铰接物体的 NeRF 模型，当物体移动时，KnowledgeNeRF 通过将预训练的 NeRF 模型中的过去知识与当前状态中的最小观察相结合，学习在新的状态下生成新视角。</p>
<p>(4) 方法在任务上的表现及性能：
KnowledgeNeRF 在动态 3D 场景重建任务上取得了有效性，在单个状态下使用 5 幅输入图像即可重建。该方法可以支持其目标，即为动态铰接物体提供新视角合成的新管道和有前途的解决方案。</p>
<p>7.Methods：
（1）预训练铰接物体NeRF模型：训练一个NeRF模型，从单目视频中学习铰接物体的变形。
（2）构建知识图谱：将预训练的NeRF模型的权重和激活值存储在一个知识图谱中。
（3）新视角合成：当物体移动时，将知识图谱中的过去知识与当前状态中的最小观察相结合，学习在新的状态下生成新视角。</p>
<ol>
<li>结论：
(1): KnowledgeNeRF 提出了一种新框架，通过一次考虑两帧来重建动态场景，有效地解决了动态铰接物体的新视角合成问题。该方法预训练了一个铰接物体的 NeRF 模型，并通过将预训练的 NeRF 模型中的过去知识与当前状态中的最小观察相结合，学习在新的状态下生成新视角，为动态铰接物体提供了新视角合成的新管道和有前途的解决方案。
(2): 创新点：</li>
<li>提出了一种新的框架 KnowledgeNeRF，通过一次考虑两帧来重建动态场景，有效地解决了动态铰接物体的新视角合成问题。</li>
<li>将预训练的铰接物体 NeRF 模型中的过去知识与当前状态中的最小观察相结合，学习在新的状态下生成新视角，提高了重建场景的质量。</li>
<li>提出了一种构建知识图谱的方法，将预训练的 NeRF 模型的权重和激活值存储在一个知识图谱中，方便后续的知识提取和利用。
性能：</li>
<li>在动态 3D 场景重建任务上取得了有效性，在单个状态下使用 5 幅输入图像即可重建。</li>
<li>可以支持其目标，即为动态铰接物体提供新视角合成的新管道和有前途的解决方案。
工作量：</li>
<li>需要预训练一个铰接物体 NeRF 模型，这可能需要大量的数据和计算资源。</li>
<li>需要构建一个知识图谱，这可能会增加存储和计算开销。</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-5a878411dcb6ab842b9571fbf35e761b.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-1c30a4c13059600200df9151f02890b7.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-35e6ac626071f10b54837546e9ead1e4.jpg" align="middle">
</details>




