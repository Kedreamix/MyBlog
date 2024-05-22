
---
title: 3DGS
date: 2024-04-22 17:32:29
author: Kedreamix
cover: https://pic1.zhimg.com/v2-c36e0e4bd338738e2a5420e68cd6ab5d.jpg
categories: Paper
tags:
    - 3DGS
description: 3DGS 方向最新论文已更新，请持续关注 Update in 2024-04-22  Learn2Talk 3D Talking Face Learns from 2D Talking Face  
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

# 2024-04-22 更新


## Learn2Talk: 3D Talking Face Learns from 2D Talking Face

**Authors:Yixiang Zhuang, Baoping Cheng, Yao Cheng, Yuntao Jin, Renshuai Liu, Chengyang Li, Xuan Cheng, Jing Liao, Juncong Lin**

Speech-driven facial animation methods usually contain two main classes, 3D and 2D talking face, both of which attract considerable research attention in recent years. However, to the best of our knowledge, the research on 3D talking face does not go deeper as 2D talking face, in the aspect of lip-synchronization (lip-sync) and speech perception. To mind the gap between the two sub-fields, we propose a learning framework named Learn2Talk, which can construct a better 3D talking face network by exploiting two expertise points from the field of 2D talking face. Firstly, inspired by the audio-video sync network, a 3D sync-lip expert model is devised for the pursuit of lip-sync between audio and 3D facial motion. Secondly, a teacher model selected from 2D talking face methods is used to guide the training of the audio-to-3D motions regression network to yield more 3D vertex accuracy. Extensive experiments show the advantages of the proposed framework in terms of lip-sync, vertex accuracy and speech perception, compared with state-of-the-arts. Finally, we show two applications of the proposed framework: audio-visual speech recognition and speech-driven 3D Gaussian Splatting based avatar animation. 

[PDF](http://arxiv.org/abs/2404.12888v1) 

**Summary**
通过借鉴2D说话人面部的唇形同步和言语感知领域的专业知识，提出了一种学习框架，可以构建更好的3D说话人面部网络。

**Key Takeaways**
- 3D说话人面部研究在唇形同步和言语感知方面不如2D说话人面部研究深入。
- Learn2Talk框架利用2D说话人面部领域的两个专业知识点来构建更好的3D说话人面部网络。
- 3D同步唇专家模型旨在实现音频和3D面部运动之间的唇形同步。
- 2D说话人面部方法中选择的教师模型用于指导音频到3D运动回归网络的训练，以提高3D顶点精度。
- 广泛的实验表明，该框架在唇形同步、顶点精度和言语感知方面优于现有技术。
- 该框架有语音-视觉语音识别和语音驱动3D高斯飞溅基于头像动画两个应用。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：Learn2Talk：3D 说话人脸从 2D 说话人脸学习</p>
</li>
<li>
<p>作者：Yixiang Zhuang, Baoping Cheng, Yao Cheng, Yuntao Jin, Renshuai Liu, Chengyang Li, Xuan
Cheng, Jing Liao, Juncong Lin</p>
</li>
<li>
<p>单位：暂缺</p>
</li>
<li>
<p>关键词：Speech-driven, 3D Facial Animation, 2D Talking face, Transformer, 3D Gaussian Splatting</p>
</li>
<li>
<p>论文链接：https://arxiv.org/abs/2404.12888v1
Github：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：说话人脸动画方法通常包含 3D 和 2D 说话人脸两大类，近年来两者都备受研究关注。然而，据我们所知，3D 说话人脸的研究在唇形同步（lip-sync）和语音感知方面并未像 2D 说话人脸那样深入。</p>
<p>（2）：过去的方法及其问题：本文方法动机充分。</p>
<p>（3）：本文提出的研究方法：提出一个名为 Learn2Talk 的学习框架，该框架通过利用 2D 说话人脸领域的两个专业知识点来构建一个更好的 3D 说话人脸网络。首先，受音频视频同步网络的启发，设计了一个 3D 同步唇形专家模型，以追求音频和 3D 面部动作之间的唇形同步。其次，选择一个来自 2D 说话人脸方法的教师模型来指导音频到 3D 运动回归网络的训练，以产生更高的 3D 顶点精度。</p>
<p>（4）：方法性能：本文方法在唇形同步、顶点精度和语音感知方面均优于现有技术。这些性能可以支持其目标。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出一个名为 Learn2Talk 的学习框架，该框架通过利用 2D 说话人脸领域的两个专业知识点来构建一个更好的 3D 说话人脸网络。</p>
<p>（2）：设计了一个 3D 同步唇形专家模型，以追求音频和 3D 面部动作之间的唇形同步。</p>
<p>（3）：选择一个来自 2D 说话人脸方法的教师模型来指导音频到 3D 运动回归网络的训练，以产生更高的 3D 顶点精度。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种名为 Learn2Talk 的学习框架，该框架通过利用 2D 说话人脸领域的两个专业知识点来构建一个更好的 3D 说话人脸网络，在唇形同步、顶点精度和语音感知方面均优于现有技术。</p>
<p>（2）：创新点：提出了一种新的 3D 说话人脸动画方法，该方法利用了 2D 说话人脸领域的专业知识；性能：在唇形同步、顶点精度和语音感知方面均优于现有技术；工作量：需要收集和标注大量的数据。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-c2e8566372db83537dc565617387f4cf.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-c36e0e4bd338738e2a5420e68cd6ab5d.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-3fe7530e7260eff001a6736622671663.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-3f8c50de092534c8ec8b833626c35e42.jpg" align="middle">
</details>




## Contrastive Gaussian Clustering: Weakly Supervised 3D Scene Segmentation

**Authors:Myrna C. Silva, Mahtab Dahaghin, Matteo Toso, Alessio Del Bue**

We introduce Contrastive Gaussian Clustering, a novel approach capable of provide segmentation masks from any viewpoint and of enabling 3D segmentation of the scene. Recent works in novel-view synthesis have shown how to model the appearance of a scene via a cloud of 3D Gaussians, and how to generate accurate images from a given viewpoint by projecting on it the Gaussians before $\alpha$ blending their color. Following this example, we train a model to include also a segmentation feature vector for each Gaussian. These can then be used for 3D scene segmentation, by clustering Gaussians according to their feature vectors; and to generate 2D segmentation masks, by projecting the Gaussians on a plane and $\alpha$ blending over their segmentation features. Using a combination of contrastive learning and spatial regularization, our method can be trained on inconsistent 2D segmentation masks, and still learn to generate segmentation masks consistent across all views. Moreover, the resulting model is extremely accurate, improving the IoU accuracy of the predicted masks by $+8\%$ over the state of the art. Code and trained models will be released soon. 

[PDF](http://arxiv.org/abs/2404.12784v1) 

**Summary**
使用来自不同视角的对比高斯聚类实现 3D 场景分割。

**Key Takeaways**
- 提出一种新的对比高斯聚类方法，能够从任何视角提供分割掩模，并实现场景的 3D 分割。
- 受新视角合成领域研究的启发，使用 3D 高斯云建模场景的外观。
- 通过将高斯投影到给定视点并对其颜色进行α混合，从给定视点生成准确的图像。
- 训练模型，使每个高斯都包含一个分割特征向量。
- 通过根据其特征向量对高斯进行聚类，可用于 3D 场景分割；通过将高斯投影到平面上并对其分割特征进行 α 混合，可生成 2D 分割掩模。
- 使用对比学习和空间正则化的组合，可以在不一致的 2D 分割掩模上训练我们的方法，并学习生成在所有视图中都一致的分割掩模。
- 所提出的方法非常准确，与现有技术相比，预测掩模的 IoU 准确度提高了 8%。
- 代码和训练好的模型即将发布。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：对比高斯聚类：弱监督 3D 场景分割</p>
</li>
<li>
<p>作者：Myrna C. Silva、Mahtab Dahaghin、Matteo Toso、Alessio Del Bue</p>
</li>
<li>
<p>单位：意大利理工学院模式分析与计算机视觉（PAVIS）</p>
</li>
<li>
<p>关键词：3D 高斯散射、3D 分割、对比学习</p>
</li>
<li>
<p>论文链接：arXiv:2404.12784v1 [cs.CV]
   Github 链接：无</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：近年来，新视角合成领域的研究表明，可以通过 3D 高斯云对场景的外观进行建模，并通过在给定视角上投影高斯并 α 混合其颜色来生成准确的图像。</p>
<p>（2）：过去方法与问题：高斯分组和 LangSplat 等方法存在以下问题：
   - 训练和评估需要大量 GPU 内存，导致某些场景无法处理。
   - 无法从任意视角提供分割掩码，也无法实现场景的 3D 分割。</p>
<p>（3）：研究方法：本文提出对比高斯聚类方法，该方法通过以下步骤实现 3D 场景分割和 2D 分割掩码预测：
   - 训练模型为每个高斯体添加分割特征向量。
   - 根据特征向量对高斯体进行聚类，实现 3D 场景分割。
   - 将高斯体投影到平面上并 α 混合其分割特征，生成 2D 分割掩码。
   - 使用对比学习和空间正则化，在不一致的 2D 分割掩码上训练模型，生成跨所有视角一致的分割掩码。</p>
<p>（4）：性能与目标：
   - 任务：3D 场景分割和 2D 分割掩码预测。
   - 性能：IoU 准确率比现有技术提高 +8%，表明该方法能够有效实现其目标。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：将场景表示为 3D 高斯体集合，编码几何、外观和实例分割信息；</p>
<p>（2）：使用基础模型生成 2D 分割掩码；</p>
<p>（3）：优化 3D 高斯体，最小化渲染图像和真实图像之间的差异；</p>
<p>（4）：使用对比分割损失监督 3D 特征场；</p>
<p>（5）：引入正则化项，强制高斯体在欧几里得和分割特征空间中的距离相关；</p>
<p>（6）：渲染 2D 特征图，根据对应的 2D 分割掩码对渲染特征进行聚类，计算对比聚类损失；</p>
<p>（7）：最大化同一分割内特征之间的相似度，最小化不同分割内的特征相似度。</p>
<p><strong>8. 结论</strong></p>
<p><strong>(1)</strong> 本工作的主要意义在于：</p>
<p>提出了对比高斯聚类方法，实现了 3D 场景分割和 2D 分割掩码预测，有效提高了分割精度。</p>
<p><strong>(2)</strong> 本文优缺点总结（创新点、性能、工作量）：</p>
<p><strong>创新点：</strong></p>
<ul>
<li>引入对比学习和空间正则化，提高了分割掩码的一致性。</li>
<li>使用 3D 高斯体表示场景，编码几何、外观和实例分割信息。</li>
</ul>
<p><strong>性能：</strong></p>
<ul>
<li>IoU 准确率比现有技术提高 +8%，分割精度高。</li>
</ul>
<p><strong>工作量：</strong></p>
<ul>
<li>训练和评估需要大量 GPU 内存，大场景处理困难。</li>
<li>无法从任意视角提供分割掩码，无法实现场景的完整 3D 分割。</li>
</ul>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-252e679c7e0a5cfc8056b41c43d99b59.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-668e640c91611b7b91220b00abd05f4e.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-03dada656b628530891ef19dcbebedba.jpg" align="middle">
</details>




## RainyScape: Unsupervised Rainy Scene Reconstruction using Decoupled   Neural Rendering

**Authors:Xianqiang Lyu, Hui Liu, Junhui Hou**

We propose RainyScape, an unsupervised framework for reconstructing clean scenes from a collection of multi-view rainy images. RainyScape consists of two main modules: a neural rendering module and a rain-prediction module that incorporates a predictor network and a learnable latent embedding that captures the rain characteristics of the scene. Specifically, based on the spectral bias property of neural networks, we first optimize the neural rendering pipeline to obtain a low-frequency scene representation. Subsequently, we jointly optimize the two modules, driven by the proposed adaptive direction-sensitive gradient-based reconstruction loss, which encourages the network to distinguish between scene details and rain streaks, facilitating the propagation of gradients to the relevant components. Extensive experiments on both the classic neural radiance field and the recently proposed 3D Gaussian splatting demonstrate the superiority of our method in effectively eliminating rain streaks and rendering clean images, achieving state-of-the-art performance. The constructed high-quality dataset and source code will be publicly available. 

[PDF](http://arxiv.org/abs/2404.11401v1) 

**Summary**
雨景重建：无监督地从多视角雨景图重建干净场景。

**Key Takeaways**
- 提出无监督框架 RainyScape，重建干净场景。
- RainyScape 由神经渲染和降雨预测模块组成。
- 降雨预测模块包含预测网络和可学习潜嵌入，捕捉场景的降雨特征。
- 基于神经网络的光谱偏差属性，优化神经渲染管道，获得低频场景表示。
- 利用自适应方向敏感梯度重建损失，优化两个模块，区分场景细节和雨痕。
- 在神经辐射场和 3D 高斯喷溅中进行的实验表明，该方法能有效消除雨痕、渲染干净图像，达到最先进性能。
- 将公开构建高质量数据集和源代码。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>标题：RainyScape：基于解耦神经渲染的无监督雨景重建</p>
</li>
<li>
<p>作者：Xianqiang Lyu, Hui Liu, Junhui Hou</p>
</li>
<li>
<p>单位：香港城市大学计算机科学系</p>
</li>
<li>
<p>关键词：雨景重建、神经渲染、无监督损失</p>
</li>
<li>
<p>论文链接：xxx，Github 链接：None</p>
</li>
<li>
<p>摘要：</p>
</li>
</ol>
<p>（1）：研究背景：神经辐射场（NeRF）在学习场景的连续体积表示方面取得了突破性进展，但当输入图像因模糊、噪声或雨水等因素而退化时，渲染结果不可避免地会出现明显伪影。</p>
<p>（2）：过去方法：现有方法针对不同的退化因素提出了特定任务的解决方案，但针对雨景重建任务的方法较少，且难以通过附加神经渲染场来表示雨水。</p>
<p>（3）：研究方法：本文提出 RainyScape，一个解耦的神经渲染框架，能够从雨景图像中无监督地重建无雨场景。该框架包括一个神经渲染模块和一个雨滴预测模块，通过学习雨滴嵌入和使用预测器来预测雨滴条纹，并提出自适应角度估计策略和梯度旋转损失来解耦场景高频细节和雨滴条纹。</p>
<p>（4）：方法性能：在经典神经辐射场和最近提出的 3D 高斯 splatting 上的广泛实验表明，该方法在有效消除雨滴条纹和渲染清晰图像方面优于现有方法，达到最先进的性能。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出 RainyScape，一个解耦的神经渲染框架，能够从雨景图像中无监督地重建无雨场景。</p>
<p>（2）：该框架包括一个神经渲染模块和一个雨滴预测模块，通过学习雨滴嵌入和使用预测器来预测雨滴条纹。</p>
<p>（3）：提出自适应角度估计策略和梯度旋转损失来解耦场景高频细节和雨滴条纹。</p>
<ol>
<li>结论：<pre><code>            （1）：RainyScape 在雨景重建领域具有重要意义，它首次提出了一个解耦神经渲染框架，能够从雨景图像中无监督地重建无雨场景。 该框架通过将场景高频细节和雨滴条纹解耦，有效地消除了雨滴条纹，并渲染出清晰的图像。

            （2）：创新点：RainyScape 创新性地提出了一个解耦神经渲染框架，将场景高频细节和雨滴条纹解耦，有效地消除了雨滴条纹，并渲染出清晰的图像。

            性能：RainyScape 在经典神经辐射场和最近提出的 3D 高斯 splatting 上的广泛实验表明，该方法在有效消除雨滴条纹和渲染清晰图像方面优于现有方法，达到最先进的性能。

            工作量：RainyScape 的工作量中等，需要训练神经渲染模块和雨滴预测模块，并提出自适应角度估计策略和梯度旋转损失来解耦场景高频细节和雨滴条纹。
</code></pre>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-789763f7ebb6ec7a923539611ab1fe24.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-89f176b1378008d1c0b63c9241adfdb2.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-5f7fb8305c36c1fe2572adfd98b584f7.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-76be36036e15658d754b57c4864b0abf.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-3765b699865b1d89cc9f5f13f9843a0e.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-34d10a80ece07ba92081dfc066d00427.jpg" align="middle">
</details>




## DeblurGS: Gaussian Splatting for Camera Motion Blur

**Authors:Jeongtaek Oh, Jaeyoung Chung, Dongwoo Lee, Kyoung Mu Lee**

Although significant progress has been made in reconstructing sharp 3D scenes from motion-blurred images, a transition to real-world applications remains challenging. The primary obstacle stems from the severe blur which leads to inaccuracies in the acquisition of initial camera poses through Structure-from-Motion, a critical aspect often overlooked by previous approaches. To address this challenge, we propose DeblurGS, a method to optimize sharp 3D Gaussian Splatting from motion-blurred images, even with the noisy camera pose initialization. We restore a fine-grained sharp scene by leveraging the remarkable reconstruction capability of 3D Gaussian Splatting. Our approach estimates the 6-Degree-of-Freedom camera motion for each blurry observation and synthesizes corresponding blurry renderings for the optimization process. Furthermore, we propose Gaussian Densification Annealing strategy to prevent the generation of inaccurate Gaussians at erroneous locations during the early training stages when camera motion is still imprecise. Comprehensive experiments demonstrate that our DeblurGS achieves state-of-the-art performance in deblurring and novel view synthesis for real-world and synthetic benchmark datasets, as well as field-captured blurry smartphone videos. 

[PDF](http://arxiv.org/abs/2404.11358v2) 

**Summary**
从模糊运动图像重建清晰 3D 场景方法，优化 3D 高斯投射，实现精确摄像机位姿初始化。

**Key Takeaways**
- DeblurGS 优化高斯投射，提高运动模糊图像 3D 重建精度。
- 利用高斯投射的重建能力，还原精细锐利场景。
- 估计每幅模糊图像的 6 自由度摄像机运动，生成模糊渲染用于优化。
- 高斯密度退火策略防止错误位置生成不准确的高斯。
- DeblurGS 在去模糊和合成新视角方面取得了最先进的性能。
- 适用于真实世界和合成基准数据集，以及现场拍摄的模糊智能手机视频。
- DeblurGS 极大地扩展了运动模糊图像的 3D 重建的实际应用。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>
<p>Title: DeblurGS: 高斯溅射相机运动模糊 (DeblurGS: Gaussian Splatting for Camera Motion Blur)</p>
</li>
<li>
<p>Authors: Jeongtaek Oh, Jaeyoung Chung, Dongwoo Lee, and Kyoung Mu Lee</p>
</li>
<li>
<p>Affiliation: 首尔国立大学人工智能与信息处理研究所 (IPAI, Seoul National University)</p>
</li>
<li>
<p>Keywords: 3D Gaussian Splatting · Camera Motion Deblurring</p>
</li>
<li>
<p>Urls: None, Github: None</p>
</li>
<li>
<p>Summary:</p>
</li>
</ol>
<p>(1): 尽管从运动模糊图像重建清晰的 3D 场景方面取得了重大进展，但向实际应用的过渡仍然具有挑战性。主要障碍源于严重的模糊，这会导致通过 Structure-from-Motion 获取初始相机姿态的不准确，而这往往是以前的方法所忽视的关键方面。</p>
<p>(2): 过去的方法主要集中于模糊图像的去模糊处理，但对于初始相机姿态的噪声初始化不鲁棒。</p>
<p>(3): 本文提出 DeblurGS，这是一种从运动模糊图像优化清晰的 3D 高斯溅射的方法，即使在噪声相机姿态初始化的情况下也是如此。我们利用 3D 高斯溅射的出色重建能力来恢复细粒度的清晰场景。我们的方法估计每个模糊观测的 6 自由度相机运动，并为优化过程合成相应的模糊渲染。此外，我们提出了高斯致密化退火策略，以防止在相机运动仍然不精确的早期训练阶段在错误的位置生成不准确的高斯。</p>
<p>(4): 综合实验表明，我们的 DeblurGS 在真实世界和合成基准数据集以及现场捕获的模糊智能手机视频的去模糊和新视图合成方面实现了最先进的性能。</p>
<ol>
<li>方法：</li>
</ol>
<p>（1）：提出 DeblurGS，一种从运动模糊图像优化清晰的 3D 高斯溅射的方法；</p>
<p>（2）：利用 3D 高斯溅射的重建能力恢复细粒度的清晰场景；</p>
<p>（3）：估计每个模糊观测的 6 自由度相机运动，并合成相应的模糊渲染；</p>
<p>（4）：提出高斯致密化退火策略，防止在相机运动不精确的早期训练阶段生成不准确的高斯。</p>
<ol>
<li>结论：</li>
</ol>
<p>（1）：本文提出了一种从运动模糊图像优化清晰的 3D 高斯溅射的方法，即使在噪声相机姿态初始化的情况下也是如此。该方法利用 3D 高斯溅射的出色重建能力来恢复细粒度的清晰场景，估计每个模糊观测的 6 自由度相机运动，并为优化过程合成相应的模糊渲染。此外，该方法提出了高斯致密化退火策略，以防止在相机运动仍然不精确的早期训练阶段在错误的位置生成不准确的高斯。综合实验表明，该方法在真实世界和合成基准数据集以及现场捕获的模糊智能手机视频的去模糊和新视图合成方面实现了最先进的性能。</p>
<p>（2）：创新点：利用 3D 高斯溅射的重建能力恢复细粒度的清晰场景，即使在噪声相机姿态初始化的情况下也是如此；</p>
<p>性能：在真实世界和合成基准数据集以及现场捕获的模糊智能手机视频的去模糊和新视图合成方面实现了最先进的性能；</p>
<p>工作量：该方法需要估计每个模糊观测的 6 自由度相机运动，并为优化过程合成相应的模糊渲染，这可能会增加计算成本。</p>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-d1b62fa212aabdf515b9baf8fdc306be.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-32c4f56eaf456fe86ff5f42abfbd6ffb.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-50b9e9cff40ee36449b6b3559539186a.jpg" align="middle">
</details>




