# coding=utf-8
from LVLM import prompt1, prompt2
import base64
from openai import OpenAI

base_url = "https://maas-cn-southwest-2.modelarts-maas.com/v1/infers/503a4bee-652d-4630-a7e1-f606df2c30aa/v1"
api_key = "0NrnzZnaWtbghvBMWjnEfEHAZcct7q0eh_b7tUnoSjsakunaYIykhBDKlLYgQ-CwZCZvqPuDwYbNpVbuv1qQsw"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

picture_path = "/code/Qwen_Audio/picture/img.png"
base64_image = encode_image("/code/Qwen_Audio/picture/img.png")
base64_image2 = encode_image("/code/Qwen_Audio/picture/img_1.png")
client = OpenAI(api_key=api_key, base_url=base_url)
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
# input_ = "请根据图片内容生成一段描述"
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
            # {"type": "text", "text": picture_path},
        ],
    }
]
response = client.chat.completions.create(
    model="Qwen2-VL-7B",  # 模型名称
    messages=messages,
    max_tokens=1024,
    temperature=1,
    stream=False,
)
print(response.choices[0].message.content)








message1 = [
        {
            "role": "user",
            "content": [
                # {"type": "text", "text": input_},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}",
                    },
                },
            ],
        },
    ],