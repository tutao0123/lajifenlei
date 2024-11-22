from pathlib import Path
from openai import OpenAI
client = OpenAI(
    api_key="sk-EuxvVtTWVKEnMu9WX406luCzoMjEs75kXwshr4ptjbNvNTJP",  # 替换为你的API Key
    base_url="https://api.moonshot.cn/v1",
)

file_object = client.files.create(file=Path("G:/fenlei/eval/1.jpg"), purpose="file-extract")

# 获取结果
# file_content = client.files.retrieve_content(file_id=file_object.id)
# 注意，某些旧版本示例中的 retrieve_content API 在最新版本标记了 warning, 可以用下面这行代替
# （如果使用旧版本的 SDK，可以继续延用 retrieve_content API）
file_content = client.files.content(file_id=file_object.id).text

# 把文件内容通过系统提示词 system prompt 放进请求中
messages = [
    {
        "role": "system",
        "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
    },
    {
        "role": "system",
        "content": file_content,  # <-- 这里，我们将抽取后的文件内容（注意是文件内容，而不是文件 ID）放置在请求中
    },
    {"role": "user", "content": "请简单介绍这个图片。"},
]

# 然后调用 chat-completion, 获取 Kimi 的回答
completion = client.chat.completions.create(
    model="moonshot-v1-32k",
    messages=messages,
    temperature=0.3,
)

print(completion.choices[0].message)