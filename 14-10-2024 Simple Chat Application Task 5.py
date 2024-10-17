from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.schema import HumanMessage, AIMessage, SystemMessage
llm =  OllamaLLM(model='llama3.2')

users = input('How can i halpe you : ')

response = llm(users)

print(response)