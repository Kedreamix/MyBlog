import openai

# openai.log = "debug"
openai.api_key = "sk-OdR1hkiUc3OCgKLh9hB35zI085uHd6NHG64rxJVPGsxuxaDh"
openai.api_base = "https://api.chatanywhere.com.cn/v1"

# 非流式响应
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    try:
        response = openai.ChatCompletion.create(
            # model='gpt-3.5-turbo',
            model='gpt-3.5-turbo-1106',
            messages=messages,
            stream=True,
        )
        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                # print(f'收到的完成数据: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                # print(f'流响应数据: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v
        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, '', completion)
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')



if __name__ == '__main__':
    text = 'This paper addresses the challenge of 3D instance segmentation by simultaneously leveraging 3D geometric and multi-view image information. Many previous works have applied deep learning techniques to 3D point clouds for instance segmentation. However, these methods often failed to generalize to various types of scenes due to the scarcity and low-diversity of labeled 3D point cloud data. Some recent works have attempted to lift 2D instance segmentations to 3D within a bottom-up framework. The inconsistency in 2D instance segmentations among views can substantially degrade the performance of 3D segmentation. In this work, we introduce a novel 3D-to-2D query framework to effectively exploit 2D segmentation models for 3D instance segmentation. Specifically, we pre-segment the scene into several superpoints in 3D, formulating the task into a graph cut problem. The superpoint graph is constructed based on 2D segmentation models, where node features are obtained from multi-view image features and edge weights are computed based on multi-view segmentation results, enabling the better generalization ability. To process the graph, we train a graph neural network using pseudo 3D labels from 2D segmentation models. Experimental results on the ScanNet, ScanNet++ and KITTI-360 datasets demonstrate that our method achieves robust segmentation performance and can generalize across different types of scenes. Our project page is available at this https URL.'
    summary_prompt= '''User
Ignore all previous instructions. You are a highly proficient researcher that can read and write properly and fluently, and can extract all important information from any text. Your task is to summarize and extract all key takeaways of the following text delimited by triple backticks in all relevant aspects. 

Output a summary and a list of key takeaways respectively. The summary should be a one-liner in at most 100 words. The key takeaways should be in up to seven bulletpoints, the fewer the better.

Use the following format:
### Summary
<summary of the text>

### Key Takeaways
<list of key takeaways>

Respond in Simplified Chinese.

Text:
```
%s
```
'''
    question = summary_prompt % text
    messages = [{'role': 'user','content': question},]
    answer = gpt_35_api_stream(messages)
    print(answer)
    content = answer[2]['content']
    print(content)
    # print(messages)
    