'''
平台
https://apifox.com/apidoc/project-4798344/doc-5309262
----小爱发货内容----

1. 使用方法：
   - 关闭魔法（国外网）
   - 输入URL和key
2.使用文档 【示例代码大全教程】：
   - https://apifox.com/apidoc/project-4798344/doc-5309262
3.小爱导航 官网 chat 学术优化 lobe 查询余额地址 ：
   - https://a.xiaoai.plus/
注：商品仅供个人测试，请遵守法律法规。

接口：
   - 请求地址1：https://xiaoai.plus
   - 请求地址2：https://xiaoai.plus/v1
   - 路由请求：https://xiaoai.plus/v1/chat/completions
   * 依次测试接口

* key在最上面，有报错问题不要发淘宝，联系【使用文档】里有售后专员！

-----每周有老客户专属小额福利活动，可联系聊天室里专员了解----

api_key='sk-RBV8JqKocGMuwcUnBA0ZkYxzljHpS5l10iTjZWUq1bFNcAye'
'''

from openai import OpenAI

# 创建客户端
client = OpenAI(
    base_url='https://xiaoai.plus/v1',
    api_key='sk-RBV8JqKocGMuwcUnBA0ZkYxzljHpS5l10iTjZWUq1bFNcAye'
)

# 初始化对话历史
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Chat started! Type 'exit' to end the conversation.")

while True:
    # 获取用户输入
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    # 将用户消息添加到对话历史
    conversation_history.append({"role": "user", "content": user_input})

    # 调用 OpenAI API
    completion = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=conversation_history
    )

    # 获取助手的回复
    assistant_reply = completion.choices[0].message.content

    # 打印助手的回复
    print(f"Assistant: {assistant_reply}")

    # 将助手的回复添加到对话历史
    conversation_history.append({"role": "assistant", "content": assistant_reply})
