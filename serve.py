from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/vr7/Desktop/Ollama/venv4/.env")
groq_api_key=os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)


## 1. Create a prompt template
system_template="Translate the following into{language}:"
prompt_template=ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)

parser=StrOutputParser()

## Create a chain
chain=prompt_template|model|parser


### App Definitions
app=FastAPI(title="langchain Server",
            version="0.1",
            description="A simple API server using Langchain runnable interfaces")


### Adding chain routers
add_routes(
    app,
    chain,
    path="/chain"
)



if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="Localhost",port=8000)