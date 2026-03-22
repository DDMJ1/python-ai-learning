# 第一个 Python + AI 入门脚本
# 功能：打印 AI 学习欢迎语，简单演示变量和函数
def ai_learning_welcome(name):
    """AI 学习欢迎函数"""
    welcome_msg = f"🎉 你好 {name}！欢迎开启 Python + AI 大模型应用开发学习之旅！"
    print(welcome_msg)
    print("📚 学习路线：Python 基础 → FastAPI → 大模型 API → RAG → 知识库项目")

# 调用函数，替换成你的名字
ai_learning_welcome("DDMJ1")

# 简单的 AI 相关变量演示
ai_tech = ["大模型 API", "Prompt 工程", "RAG", "LangChain", "向量数据库"]
print("\n📌 核心学习技术：")
for idx, tech in enumerate(ai_tech, 1):
    print(f"{idx}. {tech}")
