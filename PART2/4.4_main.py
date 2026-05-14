from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model_name="glm-4.7")

messages = [
    (
        "system",
        "당신은 사용자가 한 말을 영어로 번역하는 유능한 번역가입니다.",
    ),
    ("human", "안녕하세요. 오늘의 날씨는 어떻습니까? 기분은 어때요?"),
]
ai_msg = llm.invoke(messages)
print(ai_msg)