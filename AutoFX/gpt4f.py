import requests
import json
import os

def get_access_token(api_key, secret_key):
    """
    使用 API Key 和 Secret Key 获取access_token。
    :param api_key: 应用的API Key
    :param secret_key: 应用的Secret Key
    :return: access_token
    """
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    
    response = requests.post(url, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception("获取 access_token 失败")

def call_wenxin_api(access_token, message):
    """
    发送请求到文心一言的API。
    :param access_token: 用于认证的access_token
    :param message: 用户消息
    :return: 文心一言的响应
    """
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token={access_token}"
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": message
            }],
        "system": "You are a researcher in the field of deeplearning who is good at summarizing papers using concise statements"
    })
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API 请求失败")

def main():
    # 请将你的 API Key 和 Secret Key 替换到下面的变量中
    api_key = 'ZgaeXqX9WkmCoEvCZEcWDATZ'
    secret_key = '7cKeQW3nlica7kHGuV3VKi5QBtmDm6K8'
    
    try:
        access_token = get_access_token(api_key, secret_key)
        message = '''{"role": "user", "content": "This is the title, author, link, abstract and introduction of an English document. I need your help to read and summarize the following questions: Title:\u201cGood Robot!\u201d: Ef\ufb01cient Reinforcement Learning for Multi-Step Visual Tasks with Sim to Real TransferUrl:Abstract:Paper_info:6724\nIEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 5, NO. 4, OCTOBER 2020\n\u201cGood Robot!\u201d: Ef\ufb01cient Reinforcement Learning for\nMulti-Step Visual Tasks with Sim to Real Transfer\nAndrew Hundt\n, Benjamin Killeen\n, Nicholas Greene, Hongtao Wu\n, Heeyeon Kwon,\nChris Paxton\n, and Gregory D. Hager\nAbstract\u2014Current Reinforcement Learning (RL) algorithms\nstruggle with long-horizon tasks where time can be wasted explor-\ning dead ends and task progress may be easily reversed. We develop\nthe SPOT framework, which explores within action safety zones,\nlearns about unsafe regions without exploring them, and prioritizes\nexperiences that reverse earlier progress to learn with remarkable\nef\ufb01ciency. The SPOT framework successfully completes simulated\ntrials of a variety of tasks, improving a baseline trial success rate\nfrom 13% to 100% when stacking 4 cubes, from 13% to 99% when\ncreating rows of 4 cubes, and from 84% to 95% when clearing toys\narranged in adversarial patterns. Ef\ufb01ciency with respect to actions\nper trial typically improves by 30% or more, while training takes\njust 1-20 k actions, depending on the task. Furthermore, we demon-\nstrate direct sim to real transfer. We are able to create real stacks\nin 100% of trials with 61% ef\ufb01ciency and real rows in 100% of\ntrialswith59%ef\ufb01ciencybydirectlyloadingthesimulation-trained\nmodel on the real robot with no additional real-world \ufb01ne-tuning.\nToourknowledge,thisisthe\ufb01rstinstanceofreinforcementlearning\nwith successful sim to real transfer applied to long term multi-step\ntasks such as block-stacking and row-making with consideration\nof progress reversal. Code is available at https://github.com/jhu-\nlcsr/good_robot.\nIndex Terms\u2014Computer vision for other robotic applications,\ndeep learning in grasping and manipulation, reinforcement\nlearning.\nI. INTRODUCTION\nM\nULTI-STEP robotic tasks in real-world settings are no-\ntoriously challenging to learn. They intertwine learning\nthe immediate physical consequences of actions with the need\nto understand how these consequences affect progress towards\nthe overall goal. Furthermore, in contrast to traditional motion\nplanning, which assumes perfect information and known action\nmodels, learning only has access to the spatially and temporally\nlimited information from sensing the environment.\nManuscript received February 24, 2020; accepted July 20, 2020. Date of\npublication August 11, 2020; date of current version August 27, 2020. This letter\nwas recommended for publication by Associate Editor J. Kober and Editor T.\nAsfour upon evaluation of the reviewers\u2019. comments. This work was supported\nby the NSF NRI Awards nos. 1637949 and 1763705, and in part by Of\ufb01ce\nof Naval Research Award N00014-17-1-2124. (Corresponding author: Andrew\nHundt.)\nAndrew Hundt, Benjamin Killeen, Nicholas Greene, Hongtao Wu, Heeyeon\nKwon, and Gregory D. Hager are with The Johns Hopkins University,\nBaltimore, MD 21218 USA (e-mail: ahundt@jhu.edu; killeen@jhu.edu;\nngreen29@jhu.edu; hwu67@jhu.edu; hkwon28@jhu.edu; hager@cs.jhu.edu).\nChris Paxton is with NVIDIA, Seattle, WA, 98105 USA (e-mail:\ncpaxton@nvidia.com).\nThis article has supplementary downloadable material available at https://\nieeexplore.ieee.org, provided by the authors.\nDigital Object Identi\ufb01er 10.1109/LRA.2020.3015448\nFig. 1.\nRobot-created stacks and rows of cubes with sim to real transfer. Our\nSchedule for Positive Task (SPOT) framework allows us to ef\ufb01ciently\n\ufb01nd\npolicies\nwhich\ncan\ncomplete\nmulti-step\ntasks.\nVideo\noverview:\nhttps://youtu.be/MbCuEZadkIw\nOur key observation is that reinforcement learning wastes sig-\nni\ufb01cant time exploring actions which are unproductive at best.\nFor example, in a block stacking task (Fig. 1), the knowledge\nthat grasping at empty air will never snag an object is \u201ccommon\nsense\u201d for humans, but may take some time for a vanilla algo-\nrithm to discover. To address this, we propose the Schedule for\nPositive Task (SPOT) framework, which incorporates common\nsense constraints in a way that signi\ufb01cantly accelerates both\nlearning and \ufb01nal task ef\ufb01ciency.\nWhile these types of constraints are intuitive, incorporating\nthem into Deep RL (DRL) in a manner that leads to reliable and\nef\ufb01cient learning is nontrivial [1], [2]. Our methods (Section III)\ntakeinspirationfromahumaneandeffectiveapproachtotraining\npets sometimes called \u201cPositive Conditioning.\u201d Consider the\ngoal of training a dog \u201cSpot\u201d to ignore an object or event she\n\ufb01nds particularly interesting on command. Spot is rewarded with\ntreats whenever partial compliance with the desired end behavior\nis shown, and simply removed from regressive situations with\nzero treats (reward). One way to achieve this is to start with\nmultiple treats in hand, place one treat in view of Spot, and, if\nshe eagerly jumps at the treat (a negative action), the human\nsnatches and hides the treat immediately for zero reward on\nthat action. With repetition, Spot will eventually hesitate, and so\nshe is immediately praised with \u201cGood Spot!\u201d and gets a treat\n2377-3766 \u00a9 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.\nSee https://www.ieee.org/publications/rights/index.html for more information.\nAuthorized licensed use limited to: University of Science & Technology of China. Downloaded on July 10,2022 at 08:56:24 UTC from IEEE Xplore.  Restrictions apply. \n\u4ee3\u7801\u5f00\u6e90\u4e86\uff0c\u5f3a\u5316\n\u7528\u7684\u662f\u57fa\u7840\u63a7\u5236\u7b56\u7565\uff08pick place push\uff09\uff0c\u4ee5\u53ca\u7cbe\u5fc3\u8bbe\u8ba1\u7684\u5956\u52b1\u3002\n\u51e0\u5343\u6b21\u5c31\u53ef\u4ee5\u5b66\u4f1a\uff01\nAbstract\u2014Current Reinforcement Learning (RL) algorithms struggle with long-horizon tasks where time can be wasted exploring dead ends and task progress may be easily reversed. We develop the SPOT framework, which explores within action safety zones, learns about unsafe regions without exploring them, and prioritizes experiences that reverse earlier progress to learn with remarkable ef\ufb01ciency. The SPOT framework successfully completes simulated trials of a variety of tasks, improving a baseline trial success rate from 13% to 100% when stacking 4 cubes, from 13% to 99% when creating rows of 4 cubes, and from 84% to 95% when clearing toys arranged in adversarial patterns. Ef\ufb01ciency with respect to actions per trial typically improves by 30% or more, while training takes just 1-20 k actions, depending on the task. Furthermore, we demonstrate direct sim to real transfer. We are able to create real stacks in 100% of trials with 61% ef\ufb01ciency and real rows in 100% of trialswith59%ef\ufb01ciencybydirectlyloadingthesimulation-trained model on the real robot with no additional real-world \ufb01ne-tuning. Toourknowledge,thisisthe\ufb01rstinstanceofreinforcementlearning with successful sim to real transfer applied to long term multi-step tasks such as block-stacking and row-making with consideration of progress reversal. Code is available at https://github.com/jhulcsr/good_robot. Index Terms\u2014Computer vision for other robotic applications, deep learning in grasping and manipulation, reinforcement learning. I.                  \n                 1. Mark the title of the paper (with Chinese translation)\n                 2. list all the authors' names (use English)\n                 3. mark the first author's affiliation (output Chinese translation only)                 \n                 4. mark the keywords of this article (use English)\n                 5. link to the paper, Github code link (if available, fill in Github:None if not)\n                 6. summarize according to the following four points.Be sure to use Chinese answers (proper nouns need to be marked in English)\n                    - (1):What is the research background of this article?\n                    - (2):What are the past methods? What are the problems with them? Is the approach well motivated?\n                    - (3):What is the research methodology proposed in this paper?\n                    - (4):On what task and what performance is achieved by the methods in this paper? Can the performance support their goals?\n                 Follow the format of the output that follows:                  \n                 1. Title: xxx\n\n\n                 2. Authors: xxx\n\n\n                 3. Affiliation: xxx\n\n                 \n                 4. Keywords: xxx\n\n   \n                 5. Urls: xxx or xxx , xxx \n\n      \n                 6. Summary: \n\n\n                    - (1):xxx;\n \n                    - (2):xxx;\n \n                    - (3):xxx;\n  \n                    - (4):xxx.\n\n     \n                 \n                 Be sure to use Chinese answers (proper nouns need to be marked in English), statements as concise and academic as possible, do not have too much repetitive information, numerical values using the original numbers, be sure to strictly follow the format, the corresponding content output to xxx, in accordance with \n line feed.                 \n                 "}, "system": "You are a researcher in the field of [reinforcement learning] who is good at summarizing papers using concise statements"'''  # 你可以替换成你想要的任何消息
        
        response = call_wenxin_api(access_token, message)
        print(response)
        print(response['result'])
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == '__main__':
    main()
