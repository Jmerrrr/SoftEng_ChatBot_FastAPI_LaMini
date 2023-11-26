# API import Section
from fastapi import FastAPI, Request
import asyncio
# LLM section import
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
# IMPORTS FOR TEXT GENERATION PIPELINE CHAIN
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import copy

app = FastAPI(
    title="Inference API for Lamini-T5-738M",
    description="A simple API that use MBZUAI/LaMini-Flan-T5-77M as a chatbot",
    version="1.0"
)

checkpoint = "./LaMini-T5-738M"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint,
device_map='auto',torch_dtype=torch.float32)
pipe = pipeline(
    'text2text-generation',
    model = base_model,
    tokenizer = tokenizer,
    max_length = 512,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
)


@app.get('/')
async def hello():
    return {"hello" : "Medium enthusiast"}

@app.get('/model')
async def model():
    res = pipe("What is climate change?")
    result = copy.deepcopy(res)
    return {"result": result}

@app.get('/lamini')
async def lamini(question : str):
    res = pipe(question)
    result = copy.deepcopy(res)
    return {"result": result}