from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever

model = OllamaLLM(model="llama3.2:1b")

template="""
You are an expert in answering questions about a pizza restaurant. Help users with their doubts.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}    
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

reviews = retriever.invoke("What is the best pizza place in Goiânia?")

result = chain.invoke({
    "reviews": reviews,
    "question": "How are the vegan options?"
    })

print(result)

