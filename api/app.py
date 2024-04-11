#importing all librarires 
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

os.environ["COHERE_API_KEY"]=os.getenv("COHERE_API_KEY")

app = FastAPI(
    title= "Langchain server",
    version="1.0",
    description="api server"

)

add_routes(
    app,
    ChatCohere(),
    path="/cohere"

)

model = ChatCohere()
##ollama llama2
# llm=Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about a {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about a {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

# add_routes(
#     app,
#     prompt2|llm,
#     path="/poem"
# )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
