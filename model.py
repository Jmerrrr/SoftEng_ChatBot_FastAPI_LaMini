import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import copy
from langchain.llms import HuggingFacePipeline

def qa_llm(prompt: str):
    checkpoint = "./LaMini-T5-738M"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    base_model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint,
    device_map='cpu',torch_dtype=torch.float32)

    pipe = pipeline(
        'text2text-generation',
        model = base_model,
        tokenizer = tokenizer,
        max_length = 512,
        do_sample=True,
        temperature=0.3,
        top_p=0.95,
    )

    llm_pipe = HuggingFacePipeline(pipeline=pipe)
    res = llm_pipe(prompt)
    # result = copy.deepcopy(res)
    print(res)
    return res
    # return pipe(prompt)

