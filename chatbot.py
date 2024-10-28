from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def chat_with_me(question):
    template = """Question: {question}
    
    Answer: provide the answer based on the question provided in detail without any preamble"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.2:latest")

    chain = prompt | model

    out = chain.invoke({"question": {question}})

    return out