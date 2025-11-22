# imports
import os
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 

apikey = 'your-api-key'

os.environ['OPENAI_API_KEY'] = apikey

# App
st.title('🦜🔗 YouTube Script Generator')
prompt = st.text_input('Enter a Topic to Generate a Script About') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'], 
    template='write a youtube video script based on this title. TITLE: {title}'
)


# LangChain
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables = ['topic'], output_variables = ['title','script'], verbose=True)

# Dislpay Results
if prompt: 
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['script'])