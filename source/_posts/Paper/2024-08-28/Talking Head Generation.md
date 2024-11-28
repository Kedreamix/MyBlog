
---
title: Talking Head Generation
date: 2024-08-28 07:48:13
author: Kedreamix
cover: https://pic1.zhimg.com/v2-4760bb1b1f83c77ff470a2676d9247aa.jpg
categories: Paper
tags:
    - Talking Head Generation
description: Talking Head Generation 方向最新论文已更新，请持续关注 Update in 2024-08-28  SpeechCaps Advancing Instruction-Based Universal Speech Models with   Multi-Talker Speaking Style Captioning  
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

# 2024-08-28 更新


## SpeechCaps: Advancing Instruction-Based Universal Speech Models with   Multi-Talker Speaking Style Captioning

**Authors:Chien-yu Huang, Min-Han Shih, Ke-Han Lu, Chi-Yuan Hsiao, Hung-yi Lee**

Instruction-based speech processing is becoming popular. Studies show that training with multiple tasks boosts performance, but collecting diverse, large-scale tasks and datasets is expensive. Thus, it is highly desirable to design a fundamental task that benefits other downstream tasks. This paper introduces a multi-talker speaking style captioning task to enhance the understanding of speaker and prosodic information. We used large language models to generate descriptions for multi-talker speech. Then, we trained our model with pre-training on this captioning task followed by instruction tuning. Evaluation on Dynamic-SUPERB shows our model outperforming the baseline pre-trained only on single-talker tasks, particularly in speaker and emotion recognition. Additionally, tests on a multi-talker QA task reveal that current models struggle with attributes such as gender, pitch, and speaking rate. The code and dataset are available at https://github.com/cyhuang-tw/speechcaps. 

[PDF](http://arxiv.org/abs/2408.13891v1) SynData4GenAI 2024

**Summary**
多说话者风格字幕任务提升语言模型在说话者和韵律信息理解上的性能。

**Key Takeaways**
1. 指令式语音处理逐渐流行。
2. 多任务训练提升模型性能。
3. 收集多样、大规模数据集成本高昂。
4. 提出多说话者风格字幕任务作为基础任务。
5. 使用大语言模型生成多说话者语音描述。
6. 模型在字幕任务上进行预训练和指令微调。
7. 在Dynamic-SUPERB上优于仅训练单说话者任务的基线模型。
8. 在多说话者问答任务中，模型在性别、音高和语速等属性上表现不佳。
9. 模型代码和数据集可在GitHub上获取。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**



1. Title: SPEECHCAPS: Advancing Instruction-Based Universal Speech Models with Multi-Talker Speaking Style Captioning (SPEECHCAPS：通过多说话人说话风格字幕任务推进基于指令的通用语音模型)

2. Authors: Chien-yu Huang, Min-Han Shih, Ke-Han Lu, Chi-Yuan Hsiao, Hung-yi Lee

3. Affiliation: National Taiwan University, Taiwan

4. Keywords: speech captioning, speaking style, instruction tuning, large language model

5. Urls: https://arxiv.org/abs/2408.13891, Github: https://github.com/cyhuang-tw/speechcaps

6. Summary:

   - (1): 研究背景为基于指令的语音处理技术逐渐流行，但收集多样化的大规模任务和数据集成本高昂。因此，设计一个对下游任务有益的基础任务是高度期望的。
 
   - (2): 过去的方法包括LTU-AS、SALMONN、Qwen-Audio和WavLLM等，它们通过多任务训练或激活调整来提升性能。然而，这些方法存在数据收集成本高的问题，且对说话人和情感等任务的识别能力不足。所提出的方法是合理的，因为它旨在通过基础任务提升模型对通用语音的理解能力。
 
   - (3): 论文中提出的方法是创建一个名为SPEECHCAPS的多说话人说话风格字幕任务数据集，并使用大型语言模型生成多说话人语音的描述。然后，通过在字幕任务上进行预训练和指令调整来训练模型。
 
   - (4): 在Dynamic-SUPERB数据集上进行的评估表明，该方法在说话人和情感识别任务上优于仅对单说话人任务进行预训练的基线模型。此外，在多说话人问答任务上的测试显示，当前模型在处理性别、音调和说话速率等属性时存在困难。这些性能支持了研究的目标，即通过基础任务提升模型对说话人和韵律信息的理解。


8. Conclusion:

    - (1): 这项工作的重要意义在于，它提出了一种新的多说话人说话风格字幕任务（SPEECHCAPS），通过在指令基础上对通用语音模型进行训练，有效提升了模型对说话人和韵律信息的理解能力，为基于指令的语音处理技术提供了新的研究思路和方向。

    - (2): Innovation point: SPEECHCAPS的创新点在于提出了一个针对多说话人说话风格字幕的任务，结合了指令调整和预训练技术，为通用语音模型的训练提供了新的视角和途径；Performance: 在Dynamic-SUPERB数据集上的评估结果显示，该方法在说话人和情感识别任务上优于基线模型，但在多说话人问答任务上仍存在一些困难；Workload: 该方法需要收集大量多说话人语音数据并构建相应的字幕数据集，对数据收集和标注的工作量较大。




<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-8021415f823c5ce0acd5bb92d61e09b7.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-8e1c7406db684343030a6fdc9a395106.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-f5d9ab1e6a16acb6ef52191ed789cd35.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-5efff236d713d07c1290261d93c716a3.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-f110c7a74d2aae8799ee5d832e200c66.jpg" align="middle">
</details>




## TalkLoRA: Low-Rank Adaptation for Speech-Driven Animation

**Authors:Jack Saunders, Vinay Namboodiri**

Speech-driven facial animation is important for many applications including TV, film, video games, telecommunication and AR/VR. Recently, transformers have been shown to be extremely effective for this task. However, we identify two issues with the existing transformer-based models. Firstly, they are difficult to adapt to new personalised speaking styles and secondly, they are slow to run for long sentences due to the quadratic complexity of the transformer. We propose TalkLoRA to address both of these issues. TalkLoRA uses Low-Rank Adaptation to effectively and efficiently adapt to new speaking styles, even with limited data. It does this by training an adaptor with a small number of parameters for each subject. We also utilise a chunking strategy to reduce the complexity of the underlying transformer, allowing for long sentences at inference time. TalkLoRA can be applied to any transformer-based speech-driven animation method. We perform extensive experiments to show that TalkLoRA archives state-of-the-art style adaptation and that it allows for an order-of-complexity reduction in inference times without sacrificing quality. We also investigate and provide insights into the hyperparameter selection for LoRA fine-tuning of speech-driven facial animation models. 

[PDF](http://arxiv.org/abs/2408.13714v1) 

**Summary**
语音驱动的面部动画对电视、电影、游戏等领域至关重要，TalkLoRA通过低秩自适应和分块策略，有效解决现有模型的问题，实现高效风格适应和快速运行。

**Key Takeaways**
1. 语音驱动的面部动画应用广泛，transformer模型有效但存在适应性和速度问题。
2. TalkLoRA通过低秩自适应适应新说话风格，适应数据有限。
3. 小参数适配器实现针对不同主题的训练。
4. 分块策略降低transformer复杂度，支持长句处理。
5. TalkLoRA适用于任何基于transformer的语音驱动动画方法。
6. 实验证明TalkLoRA实现风格适应的突破，且不影响质量。
7. 研究提供LoRA微调面部动画模型的超参数选择见解。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**



1. Title: TalkLoRA: Low-Rank Adaptation for Speech-Driven Animation
                 (标题：TalkLoRA：用于语音驱动动画的低秩自适应)

2. Authors: Jack Saunders, Vinay P Namboodiri
                 (作者：Jack Saunders, Vinay P Namboodiri)

3. Affiliation: University of Bath
                 (所属机构：巴斯大学)

4. Keywords: Speech-Driven Animation, Transformer, Low-Rank Adaptation, Chunking
                 (关键词：语音驱动动画，Transformer，低秩自适应，分块)

5. Urls: https://jsaunders909.github.io/ or https://vinaypn.github.io/
                 (网址：https://jsaunders909.github.io/ 或 https://vinaypn.github.io/ , Github:None)

6. Summary:

                    - (1):该文章的研究背景是语音驱动面部动画在电视、电影、视频游戏、电信和AR/VR等领域的应用，而Transformer模型在此任务中表现出极高的有效性。
 
                    - (2):过去的方法包括基于Transformer的模型，但它们难以适应新的个性化说话风格，且由于Transformer的二次复杂性，运行长句子时速度较慢。该研究方法很好地解决了这些问题。
 
                    - (3)：该文提出的方法TalkLoRA使用低秩自适应有效地适应新的说话风格，即使数据有限。它通过为每个主题训练具有少量参数的适配器来实现。此外，还利用了分块策略来降低复杂性。
 
                    - (4)：该方法在语音驱动动画任务上实现了有效的性能，尤其是在适应新说话风格和提高运行速度方面。其性能支持了研究目标。
7. Methods:

    - (1): 本文针对现有的基于Transformer的语音驱动动画系统，提出了一种名为TalkLoRA的低秩自适应方法，以提升模型适应新说话风格的能力和运行速度。

    - (2): TalkLoRA利用低秩自适应（LoRA）技术，通过为模型添加少量参数的适配器，实现对现有模型的个性化调整。

    - (3): 为了降低模型复杂性，TalkLoRA引入了分块策略，将输入音频分割成重叠的固定大小的块，并行处理，从而减少Transformer的上下文窗口大小。

    - (4): 在音频编码器部分，由于其强大的泛化能力，TalkLoRA没有应用LoRA技术，以避免过度拟合。

    - (5): 对于解码器部分，TalkLoRA可以选择性地应用LoRA技术到Transformer解码器或运动解码器，以实现模型对单个身份的适应。

    - (6): 通过实验确定了LoRA的秩（r）的最佳值，以平衡模型的表示能力和正则化能力。

    - (7): 通过调整模型架构，实现Transformer的上下文窗口限制，从而提高长序列的推理速度。

    - (8): 在训练过程中，TalkLoRA使用AdamW优化器和适当的学习率，并在50个epoch后收敛。


8. Conclusion:

                    - (1): 该研究工作的重要性在于，它提出了一种名为TalkLoRA的低秩自适应方法，有效提高了基于Transformer的语音驱动动画模型的适应性和推理速度，这对于电视、电影、视频游戏等领域的应用具有重要意义。

                    - (2): Innovation point: 创新点在于提出了低秩自适应技术应用于语音驱动动画，实现了对现有模型的个性化调整，并通过分块策略降低了模型复杂性；Performance: 性能方面，TalkLoRA在适应新说话风格和提高运行速度方面均优于现有模型；Workload: 工作量方面，TalkLoRA通过优化模型架构和使用AdamW优化器等手段，使得训练过程高效且收敛。




<details>
  <summary>点此查看论文截图</summary>
<img src="https://pica.zhimg.com/v2-3313994c278d325c8ef3fb44a5ba2d76.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-7c2db76f55115f8dd725a17800048f2f.jpg" align="middle">
</details>




## Empowering Whisper as a Joint Multi-Talker and Target-Talker Speech   Recognition System

**Authors:Lingwei Meng, Jiawen Kang, Yuejiao Wang, Zengrui Jin, Xixin Wu, Xunying Liu, Helen Meng**

Multi-talker speech recognition and target-talker speech recognition, both involve transcription in multi-talker contexts, remain significant challenges. However, existing methods rarely attempt to simultaneously address both tasks. In this study, we propose a pioneering approach to empower Whisper, which is a speech foundation model, to tackle joint multi-talker and target-talker speech recognition tasks. Specifically, (i) we freeze Whisper and plug a Sidecar separator into its encoder to separate mixed embedding for multiple talkers; (ii) a Target Talker Identifier is introduced to identify the embedding flow of the target talker on the fly, requiring only three-second enrollment speech as a cue; (iii) soft prompt tuning for decoder is explored for better task adaptation. Our method outperforms previous methods on two- and three-talker LibriMix and LibriSpeechMix datasets for both tasks, and delivers acceptable zero-shot performance on multi-talker ASR on AishellMix Mandarin dataset. 

[PDF](http://arxiv.org/abs/2407.09817v2) Accepted to INTERSPEECH 2024

**Summary**
提出新方法，使Whisper模型同时处理多说话者和目标说话者语音识别任务。

**Key Takeaways**
- 同时处理多说话者和目标说话者语音识别。
- 使用Sidecar分离器分离混合嵌入。
- 引入目标说话者识别器。
- 需要简短的声音作为识别线索。
- 软提示调整解码器以适应任务。
- 在LibriMix和LibriSpeechMix数据集上优于先前方法。
- 在AishellMix数据集上实现可接受的零样本性能。

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**



1. Title: 赋能Whisper作为联合多说话者和目标说话者语音识别系统
                 2. Authors: Lingwei Meng, Jiawen Kang, Yuejiao Wang, Zengrui Jin, Xixin Wu, Xunying Liu, Helen Meng
                 3. Affiliation: 香港中文大学
                 4. Keywords: 多说话者语音识别，目标说话者语音识别，提示微调，领域自适应
                 5. Urls: https://arxiv.org/abs/2407.09817v2 or https://github.com/LingweiMeng/Whisper-Sidecar
       
                 6. Summary:
                    - (1):该研究背景是多说话者和目标说话者语音识别在多说话者环境下的转录仍然是一个重大挑战。
 
                    - (2):过去的方法包括传统的级联系统和端到端模型。级联系统通常由于优化目标不匹配而表现有限。端到端模型需要复杂的训练策略，如置换不变性训练（PIT）、启发式错误分配训练（HEAT）和序列输出训练（SOT），且通常需要从头开始训练或对预训练模型进行完全微调。这些方法虽然取得了显著成果，但未能充分利用标准单说话者ASR中开发的现有进步。该研究方法动机明确，旨在提高多说话者和目标说话者语音识别的性能。
 
                    - (3)：该论文提出的方法包括：冻结Whisper的权重，将其编码器中的Sidecar分离器用于多说话者嵌入分离；引入目标说话者识别器（TTI）模块以实时识别目标说话者的嵌入流，只需3秒钟的注册语音作为提示；探索解码器的软提示微调以更好地适应任务。
 
                    - (4)：该方法在两个和三个说话者的LibriMix和LibriSpeechMix数据集上实现了领先的性能，在AishellMix（普通话）数据集上达到了可接受的零样本多说话者ASR性能，支持了其研究目标。
7. Methods:

    - (1): 采用Whisper作为基础模型，并引入Sidecar分离器将多说话者嵌入分离，以处理多说话者语音识别任务。
  
    - (2): 设计目标说话者识别器（TTI）模块，通过3秒的注册语音作为提示，实时识别目标说话者的嵌入流。
  
    - (3): 对解码器进行软提示微调，以更好地适应多说话者和目标说话者语音识别任务。
  
    - (4): 在训练过程中，80%的概率进行多说话者ASR训练，20%的概率进行包含注册语音的联合多说话者和目标说话者ASR训练。
  
    - (5): 使用置换不变性训练（PIT）解决标签模糊性问题，并计算最终的损失函数，包括ASR损失和TTI的交叉熵损失。


8. Conclusion:

    - (1):该研究具有显著意义，因为它为多说话者和目标说话者语音识别领域提供了一种新的解决方案，通过引入Whisper模型和Sidecar分离器，有效提升了多说话者环境下语音识别的准确性和实时性。

    - (2):Innovation point: 该文章的创新点在于将Whisper模型与Sidecar分离器结合，并设计目标说话者识别器（TTI）模块，实现了高效的多说话者和目标说话者语音识别；Performance: 在LibriMix和LibriSpeechMix数据集上，该方法达到了领先的性能，在AishellMix数据集上也取得了可接受的零样本多说话者ASR性能；Workload: 该方法在保持高性能的同时，降低了训练和运行的工作量，通过软提示微调和解码器优化，简化了训练策略。




<details>
  <summary>点此查看论文截图</summary>
<img src="https://picx.zhimg.com/v2-ad0809bf1f2a0e13bfb58fed883c328f.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-4760bb1b1f83c77ff470a2676d9247aa.jpg" align="middle">
<img src="https://pic1.zhimg.com/v2-ba94c08ea3020d878a6417b75885d8b6.jpg" align="middle">
<img src="https://picx.zhimg.com/v2-bbbcd66af9e5a0c566946800bba17655.jpg" align="middle">
</details>




