from typing import List
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState

def get_model():
    llm = ChatOpenAI(model="glm-4.7")
    return llm
class State(MessagesState):
    plan: List[str]
    past_steps: List[tuple]

class SupervisorState(MessagesState):
    plan: List[str]
    next: str
    past_steps: List[tuple]
