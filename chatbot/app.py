#importing the libraries
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

#importing the env variables
os.environ["COHERE_API_KEY"]=os.getenv("COHERE_API_KEY")

#LANGSMITH TRACKING
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


#prompt template

prompt = ChatPromptTemplate.from_messages(
    [ 
        ("system", "You are a helpful assistance. Please respond to the queries"),
        ("user", "Question:{question}")
    ]
)


#streamlit framework
st.title("langchain demo with cohere api")
input_text = st.text_input("search the topic u want")

#calling cohere ai llms 
llm = ChatCohere(model="command")
output_parser = StrOutputParser()

#chaining all
chain = prompt|llm|output_parser

#st.write
if input_text:
    st.write(chain.invoke({'question':input_text}))