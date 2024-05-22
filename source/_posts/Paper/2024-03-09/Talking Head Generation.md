
---
title: Talking Head Generation
date: 2024-03-09 18:19:18
author: Kedreamix
cover: https://picx.zhimg.com/v2-f9beb664fee087369a84229a9751302f.jpg
categories: Paper
tags:
    - Talking Head Generation
description: Talking Head Generation 方向最新论文已更新，请持续关注 Update in 2024-03-09  FaceChain-ImagineID Freely Crafting High-Fidelity Diverse Talking Faces   from Disentangled Audio  
keywords: Talking Head Generation
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

# 2024-03-09 更新


## FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces   from Disentangled Audio

**Authors:Chao Xu, Yang Liu, Jiazheng Xing, Weida Wang, Mingze Sun, Jun Dan, Tianxin Huang, Siyuan Li, Zhi-Qi Cheng, Ying Tai, Baigui Sun**

In this paper, we abstract the process of people hearing speech, extracting meaningful cues, and creating various dynamically audio-consistent talking faces, termed Listening and Imagining, into the task of high-fidelity diverse talking faces generation from a single audio. Specifically, it involves two critical challenges: one is to effectively decouple identity, content, and emotion from entangled audio, and the other is to maintain intra-video diversity and inter-video consistency. To tackle the issues, we first dig out the intricate relationships among facial factors and simplify the decoupling process, tailoring a Progressive Audio Disentanglement for accurate facial geometry and semantics learning, where each stage incorporates a customized training module responsible for a specific factor. Secondly, to achieve visually diverse and audio-synchronized animation solely from input audio within a single model, we introduce the Controllable Coherent Frame generation, which involves the flexible integration of three trainable adapters with frozen Latent Diffusion Models (LDMs) to focus on maintaining facial geometry and semantics, as well as texture and temporal coherence between frames. In this way, we inherit high-quality diverse generation from LDMs while significantly improving their controllability at a low training cost. Extensive experiments demonstrate the flexibility and effectiveness of our method in handling this paradigm. The codes will be released at https://github.com/modelscope/facechain. 

[PDF](http://arxiv.org/abs/2403.01901v1) 

**Summary**
聆听与想象任务：从单音频生成高保真、多样的会说话的面孔，解决了身份、内容、情感解耦和维持视频内多样性、视频间一致性的双重挑战。

**Key Takeaways**
- 抽象人们聆听语音、提取有意义的线索并创建各种动态音频一致会说话的面孔的过程，称为“聆听与想象”。
- 面临身份、内容和情感从纠缠音频中有效解耦和维持视频内多样性、视频间一致性两大挑战。
- 提出渐进式音频解耦方法，用于准确的面部几何和语义学习。
- 引入可控连贯帧生成，将三个可训练适配器与冻结的潜在扩散模型（LDM）灵活集成，以专注于保持面部几何和语义，以及帧之间的纹理和时间连贯性。
- 继承了 LDM 的高质量多样化生成，同时以低训练成本显著提高了它们的控制能力。
- 广泛的实验表明了该方法在处理此范式方面的灵活性和有效性。
- 代码将在 https://github.com/modelscope/facechain 发布。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>题目：FaceChain-ImagineID：自由生成高保真多样化的说话人脸（人脸链-想象识别：从分离音频中自由生成高保真多样化的说话人脸）</li>
<li>作者：Chao Xu, Yang Liu, Jiazheng Xing, Weida Wang, Mingze Sun, Jun Dan, Tianxin Huang, Siyuan Li, Zhi-Qi Cheng, Ying Tai, Baigui Sun</li>
<li>第一作者单位：阿里巴巴集团</li>
<li>关键词：说话人脸生成、音频分离、控制生成、生成式对抗网络</li>
<li>论文链接：https://arxiv.org/abs/2403.01901</li>
<li>摘要：
（1）研究背景：说话人脸生成技术旨在根据提供的音频和图像合成视频，广泛应用于虚拟交互等实际场景。然而，用户在使用过程中面临隐私泄露和虚拟头像与自身声音不匹配的困境。
（2）过去方法：现有方法主要集中于从图像中提取特征来生成说话人脸，但存在隐私泄露、生成质量不高等问题。
（3）研究方法：本文提出了一种新的范式——聆听和想象，将人类听到语音、提取有意义线索并创造各种动态音频一致说话人脸的过程抽象为从单个音频生成高保真多样化说话人脸的任务。该方法主要包括两个关键挑战：一是有效地从纠缠的音频中分离身份、内容和情感；二是保持视频内多样性和视频间一致性。为此，本文设计了一种渐进式音频分离方法，用于准确学习人脸几何和语义；并提出了可控连贯帧生成方法，通过将三个可训练适配器与冻结的潜在扩散模型灵活集成，专注于保持帧间的人脸几何、语义、纹理和时间连贯性。
（4）方法性能：在说话人脸生成任务上，该方法展现出良好的灵活性与有效性。实验结果表明，该方法在保持音频一致性的同时，可以生成视觉上多样化的高保真说话人脸，满足了用户对隐私保护和生成质量的双重需求。</li>
</ol>
<p>7.Methods：
(1) 提出渐进式音频分离方法，准确学习人脸几何和语义。
(2) 设计可控连贯帧生成方法，通过将三个可训练适配器与冻结的潜在扩散模型灵活集成，保持帧间的人脸几何、语义、纹理和时间连贯性。</p>
<ol>
<li>结论：
(1): FaceChain-ImagineID 为说话人脸生成领域提供了一种新的范式，有效地解决了隐私泄露和生成质量不高等问题，满足了用户对隐私保护和生成质量的双重需求。
(2): 创新点：<ul>
<li>提出渐进式音频分离方法，准确学习人脸几何和语义。</li>
<li>设计可控连贯帧生成方法，通过将三个可训练适配器与冻结的潜在扩散模型灵活集成，保持帧间的人脸几何、语义、纹理和时间连贯性。
 性能：</li>
<li>在说话人脸生成任务上，该方法展现出良好的灵活性与有效性。</li>
<li>实验结果表明，该方法在保持音频一致性的同时，可以生成视觉上多样化的高保真说话人脸。
 工作量：</li>
<li>该方法的实现需要较高的技术门槛，包括音频分离、生成式对抗网络和潜在扩散模型等方面的知识。</li>
</ul>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-f9beb664fee087369a84229a9751302f.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f7122e8a5514f08293520b989812bde2.jpg" align="middle">
<img src="https://pica.zhimg.com/v2-bca46fa0ffc8639dfa0117a5baad6ae0.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-6323f54d35add5790fd10654dbb8dd9d.jpg" align="middle">
</details>




## G4G:A Generic Framework for High Fidelity Talking Face Generation with   Fine-grained Intra-modal Alignment

**Authors:Juan Zhang, Jiahao Chen, Cheng Wang, Zhiwang Yu, Tangquan Qi, Di Wu**

Despite numerous completed studies, achieving high fidelity talking face generation with highly synchronized lip movements corresponding to arbitrary audio remains a significant challenge in the field. The shortcomings of published studies continue to confuse many researchers. This paper introduces G4G, a generic framework for high fidelity talking face generation with fine-grained intra-modal alignment. G4G can reenact the high fidelity of original video while producing highly synchronized lip movements regardless of given audio tones or volumes. The key to G4G's success is the use of a diagonal matrix to enhance the ordinary alignment of audio-image intra-modal features, which significantly increases the comparative learning between positive and negative samples. Additionally, a multi-scaled supervision module is introduced to comprehensively reenact the perceptional fidelity of original video across the facial region while emphasizing the synchronization of lip movements and the input audio. A fusion network is then used to further fuse the facial region and the rest. Our experimental results demonstrate significant achievements in reenactment of original video quality as well as highly synchronized talking lips. G4G is an outperforming generic framework that can produce talking videos competitively closer to ground truth level than current state-of-the-art methods. 

[PDF](http://arxiv.org/abs/2402.18122v2) 

**Summary**
高质量会说话头像生成框架 G4G 可生成高度同步的唇部动作，实现逼真视频重现。

**Key Takeaways**
- G4G 框架可生成高度逼真的会说话头像，唇部动作与任意音频高度同步。
- G4G 采用对角矩阵增强视音频模态内特征对齐，提升正负样本比较学习。
- 多尺度监督模块全面重现视频感知保真度，强调唇部动作与输入音频同步。
- 融合网络进一步融合面部区域与其他区域。
- 实验结果表明，G4G 在重现原始视频质量和唇部动作同步方面取得显著成就。
- G4G 优于现有方法，可生成更接近真实水平的会说话头像视频。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<ol>
<li>标题：G4G：一个用于高保真说话人脸生成和精细化模态内对齐的通用框架</li>
<li>作者：Juan Zhang, Jiahao Chen, Cheng Wang, Zhiwang Yu, Tangquan Qi, Di Wu</li>
<li>第一作者单位：长沙万兴科技股份有限公司</li>
<li>关键词：说话人脸生成、模态内对齐、多尺度监督、融合网络</li>
<li>论文链接：https://arxiv.org/abs/2402.18122</li>
<li>摘要：
(1) 研究背景：说话人脸生成旨在合成一个目标人物的高保真视频，其唇部动作与任意音频同步。尽管有许多研究，但要实现高保真说话人脸生成并使其唇部动作与任意音频高度同步仍然是一个重大挑战。
(2) 过去方法：以往方法存在的问题主要在于：1）无法重现原始视频的高保真度；2）生成的唇部动作与音频不同步；3）生成的人脸视频保真度低。
(3) 研究方法：本文提出了 G4G，这是一个用于高保真说话人脸生成和精细化模态内对齐的通用框架。G4G 采用对角矩阵来增强音频-图像模态内特征的普通对齐，显著增加了正负样本之间的比较学习。此外，还引入了一个多尺度监督模块，以全面重现原始视频在面部区域的感知保真度，同时强调唇部动作与输入音频的同步性。然后使用融合网络进一步融合面部区域和其他部分。
(4) 性能：G4G 在重现原始视频质量和高度同步的说话人嘴唇方面取得了显著成就。实验结果表明，G4G 生成的说话人视频比当前最先进的方法更接近真实水平。</li>
</ol>
<p>7.Methods：
(1)：提出G4G框架，采用对角矩阵增强音频-图像模态内特征对齐，增加正负样本比较学习；
(2)：引入多尺度监督模块，重现原始视频面部区域感知保真度，强调唇部动作与音频同步；
(3)：使用融合网络融合面部区域和其他部分。</p>
<p><strong>8. 结论</strong>
(1): 本工作提出了 G4G 框架，用于生成高保真且高度同步的说话人脸视频。该框架由两个关键组件组成：对角精细化对齐网络和多尺度监督自适应空间变换网络。这些组件协同工作，生成具有卓越保真度和多尺度细节的说话人脸视频。对角精细化对齐网络专门设计用于解决模态内和模态间对齐的挑战。通过保留源图像的面部身份、属性和丰富的纹理细节，我们的网络确保生成的视频与源角色高度相似。此对齐过程对于保持生成视频的真实性和视觉质量至关重要。多尺度监督自适应空间变换网络进一步增强了生成视频的保真度。通过对嘴形和头部姿势进行空间变形，我们的网络实现了嘴唇运动的非凡准确性和真实性。生成嘴唇运动与给定音频之间的这种同步水平明显超过了现有的人脸通用方法。大量实验表明，我们的 G4G 框架在保留角色身份、皮肤纹理和与真实情况高度相似的细节方面是有效的。此外，我们的方法在生成与任意给定音频相对应的、高度同步的嘴唇运动方面表现出色。这些结果优于现有人脸通用方法，突出了我们方法的优越性。虽然我们的 G4G 框架代表了说话人脸生成领域的重大进步，但我们认识到仍有挑战需要解决。例如，生成具有大头部姿势角度的视频以及处理快速变化的背景和光照条件仍然是持续的研究领域。我们正在积极应对这些挑战，并计划在不久的将来发布进一步的研究结果。总之，我们提出的 G4G 框架为生成高保真且高度同步的说话人脸视频提供了一种强大且有效的解决方案。通过保留角色身份、皮肤纹理和细节，我们的方法为包括娱乐、教育和医疗保健在内的各个领域的应用开辟了新的可能性。
(2): <strong>创新点：</strong>
* 提出对角精细化对齐网络，增强音频-图像模态内特征对齐，增加正负样本比较学习。
* 引入多尺度监督自适应空间变换网络，重现原始视频面部区域感知保真度，强调唇部动作与音频同步。
* 使用融合网络融合面部区域和其他部分。
<strong>性能：</strong>
* 在重现原始视频质量和高度同步的说话人嘴唇方面取得了显著成就。
* 生成的说话人视频比当前最先进的方法更接近真实水平。
<strong>工作量：</strong>
* 模型复杂度和训练时间中等。</p>
<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-e12c89676d8b67fdf727809d6024eb2f.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-153d9657273ba05cfef190ef2e389848.jpg" align="middle">
</details>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pic1.zhimg.com/v2-0ed20de4df697f188c4e24a324ed403c.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-153d9657273ba05cfef190ef2e389848.jpg" align="middle">
</details>




