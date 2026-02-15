from openai import OpenAI
import os
import base64
from prompt import *

client = OpenAI(
    api_key="your_api",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


#  base 64 编码格式
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_first_response(messages):
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=messages
    )
    return completion

# messages = [{'role': 'system', 'content': prompt1}]
# data = {'input': [], 'output': []}
# score = []
# for i in range(4):
#     user_input = input("请输入：")
#     # 将用户问题信息添加到messages列表中
#     messages.append({'role': 'user', 'content': user_input})
#     assistant_output = get_first_response(messages).choices[0].message.content
#     # 将大模型的回复信息添加到messages列表中
#     messages.append({'role': 'assistant', 'content': assistant_output})
#     print(f'用户输入：{user_input}')
#     print(f'模型输出：{assistant_output}')
#     print('\n')
#     data['input'].append(user_input)
#     data['output'].append(assistant_output)
# score.append(data['output'][-1])
# print(data)

# str([data, score])
input_data = """
【患者姓名】：华小为
【心率】：89
【血氧含量】：99%
【语言】:75
【躯体和物体使用】: 35
【交往】: 50
【感觉】: 60
【社会生活自理】: 48
"""
picture_path = "./picture/img_1.png"
base64_image = encode_image("./picture/img.png")
base64_image2 = encode_image(picture_path)
messages = [
{
        "role": "system", "content": prompt2},
    {
        "role": "user",
        "content": [
            # {
            #     "type": "image_url",
            #     "image_url": {
            #         "url": f"data:image/jpeg;base64,{base64_image}",
            #     },
            # },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image2}",
                },
            },
            {"type": "text", "text": input_data},
            {"type": "text", "text": picture_path},
        ],
    }
]
completion = client.chat.completions.create(
    model="qwen-vl-max",
    messages=messages,
)
print(f"{completion.choices[0].message.content}")




# assistant_message = completion.choices[0].message
# messages.append(assistant_message.model_dump())
#
# messages.append(
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "测得他心率较低，注意力不集中，眼神迷离，他有可能是自闭症患者吗？不用给出理由"
#             }
#         ]
#     })
# completion = client.chat.completions.create(
#     model="qwen-vl-max-latest",
#     messages=messages,
# )
# print(f"第二轮输出：{completion.choices[0].message.content}")
