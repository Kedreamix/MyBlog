
---
title: Talking Head Generation
date: 2024-05-28 01:24:49
author: Kedreamix
cover: https://pic1.zhimg.com/v2-33e1c85bbd2586fc6e8eb024aa73c567.jpg
categories: Paper
tags:
    - Talking Head Generation
description: Talking Head Generation 方向最新论文已更新，请持续关注 Update in 2024-05-28  InstructAvatar Text-Guided Emotion and Motion Control for Avatar   Generation  
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

# 2024-05-28 更新


## InstructAvatar: Text-Guided Emotion and Motion Control for Avatar   Generation

**Authors:Yuchi Wang, Junliang Guo, Jianhong Bai, Runyi Yu, Tianyu He, Xu Tan, Xu Sun, Jiang Bian**

Recent talking avatar generation models have made strides in achieving realistic and accurate lip synchronization with the audio, but often fall short in controlling and conveying detailed expressions and emotions of the avatar, making the generated video less vivid and controllable. In this paper, we propose a novel text-guided approach for generating emotionally expressive 2D avatars, offering fine-grained control, improved interactivity, and generalizability to the resulting video. Our framework, named InstructAvatar, leverages a natural language interface to control the emotion as well as the facial motion of avatars. Technically, we design an automatic annotation pipeline to construct an instruction-video paired training dataset, equipped with a novel two-branch diffusion-based generator to predict avatars with audio and text instructions at the same time. Experimental results demonstrate that InstructAvatar produces results that align well with both conditions, and outperforms existing methods in fine-grained emotion control, lip-sync quality, and naturalness. Our project page is https://wangyuchi369.github.io/InstructAvatar/. 

[PDF](http://arxiv.org/abs/2405.15758v1) Project page: https://wangyuchi369.github.io/InstructAvatar/

**Summary**
提出了一种新的文本指导方法，生成情感丰富的2D虚拟头像，实现细粒度控制、交互性和通用性。

**Key Takeaways**
• 当前虚拟头像生成模型在唇音同步上取得了进展，但在表情和情感控制方面存在不足。
• 本文提出了一种文本指导方法，生成情感丰富的2D虚拟头像，实现细粒度控制和交互性。
• 该方法使用自然语言界面控制虚拟头像的情感和面部运动。
• 该方法使用自动注释管道构建训练数据集，并使用双分支扩散生成器预测虚拟头像。
• 实验结果表明，InstructAvatar方法在细粒度情感控制、唇音同步质量和自然度方面优于现有方法。
• 该方法可以生成更加生动和可控的虚拟头像视频。
• 项目页面为https://wangyuchi369.github.io/InstructAvatar/。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

<h2>Paper:1</h2>
<ol>
<li>
<p>Title: InstructAvatar：基于文本的表情和动作控制的Avatar生成（Text-Guided Emotion and Motion Control for Avatar Generation）</p>
</li>
<li>
<p>Authors: Yuchi Wang, Junliang Guo, Jianhong Bai, Runyi Yu, Tianyu He, Xu Tan, Xu Sun, and Jiang Bian</p>
</li>
<li>
<p>Affiliation: 北京大学</p>
</li>
<li>
<p>Keywords: Emotional Talking Avatar · Facial Motion Control · Text Guided · Diffusion Model</p>
</li>
<li>
<p>Urls: https://wangyuchi369.github.io/InstructAvatar/, Github: https://wangyuchi369.github.io/InstructAvatar/</p>
</li>
<li>
<p>Summary:</p>
</li>
<li>
<p>(1):近年来，谈话头像生成模型取得了实质性的进展，然而它们在控制和表达头像的情感和表情方面仍然存在不足，生成的视频因此缺乏生动性和可控性。</p>
</li>
<li>
<p>(2):过去的方法主要集中在音频同步方面，但是在控制和表达头像的情感和表情方面效果不佳，无法满足用户的需求。</p>
</li>
<li>
<p>(3):本文提出了一种基于文本的表情和动作控制方法，使用自然语言接口控制头像的情感和面部运动，设计了一条自动注释流水线来构建训练数据集，并使用基于扩散模型的生成器来预测头像。</p>
</li>
<li>
<p>(4):实验结果表明，InstructAvatar生成的结果与条件高度一致，超过了现有的方法在细粒度的情感控制、唇形同步质量和自然度方面的性能，达到了研究目标。</p>
</li>
<li>
<p>方法：</p>
</li>
<li>
<p>(1)：首先，提出了一种基于文本的表情和动作控制方法，使用自然语言接口控制头像的情感和面部运动。</p>
</li>
<li>
<p>(2)：设计了一条自动注释流水线来构建训练数据集，包括情感标签扩展、动作单元提取和大语言模型 paraphrase。</p>
</li>
<li>
<p>(3)：使用扩散模型作为文本指导运动生成器，学习条件于音频和文本指令的运动潜变量。</p>
</li>
<li>
<p>(4)：在运动生成器中，设计了一个两分支交叉注意机制，injecting 情感和运动控制信息到模型中。</p>
</li>
<li>
<p>(5)：使用Conformer作为扩散模型的主干网络，结合音频编码器和文本编码器，学习音频和文本指导的运动生成。</p>
</li>
<li>
<p>(6)：在练过程中，使用DDIM策略，迭代去噪音频指导的运动潜变量，获得最终的运动结果。</p>
</li>
<li>
<p>(7)：在实验中，使用多种评估指标，评估模型在细粒度的情感控制、唇形同步质量和自然度方面的性能。</p>
</li>
<li>
<p>Conclusion:</p>
</li>
<li>
<p>(1):本文提出的InstructAvatar方法对头像生成领域具有重要意义，可以实现细粒度的情感控制和唇形同步，满足用户的需求，具有广泛的应用前景。</p>
</li>
<li>
<p>(2):创新点：提出了基于文本的表情和动作控制方法，实现了头像的情感和面部运动控制；性能：实验结果表明，InstructAvatar生成的结果与条件高度一致，超过了现有的方法在细粒度的情感控制、唇形同步质量和自然度方面的性能；工作量：设计了一条自动注释流水线来构建训练数据集，使用了扩散模型和Conformer网络，需要一定的计算资源和数据支持。</p>
</li>
</ol>


<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-dc27e0e81b6be96603dd90e8aa23e081.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-33e1c85bbd2586fc6e8eb024aa73c567.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-444c4a6d0fe06756aad4ae2d015fe594.jpg" align="middle">
</details>




