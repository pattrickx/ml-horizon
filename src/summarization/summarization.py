import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

# Tokenizer 
from transformers import T5Tokenizer

# PyTorch model 
from transformers import T5Model, T5ForConditionalGeneration

from transformers import pipeline

def luhn_summarizer(full_text:str,lang:str="portuguese", sentences_n:int=5) -> str : 

    parser =  PlaintextParser.from_string(full_text,Tokenizer(lang))
    summarization =LuhnSummarizer()
    summy_list =  summarization(parser.document,sentences_n)
    
    summy_text=""
    for sent in summy_list:
        summy_text+= str(sent)+" "
        
    return summy_text

def hug_ptt5_base_summ_xlsum(full_text:str,lang:str="portuguese", max_length:int=100, min_length:int = 50)-> str:
    print("hug_wikilingua")
    if lang!="portuguese":
        summarize = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarize(full_text)
        return summary["summary_text"]
    
    token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
    model_name = 'phpaiola/ptt5-base-summ-xlsum'

    tokenizer = T5Tokenizer.from_pretrained(token_name )
    model_pt = T5ForConditionalGeneration.from_pretrained(model_name)
    
    inputs = tokenizer.encode(full_text, max_length=1000, truncation=True, return_tensors='pt')
    summary_ids = model_pt.generate(inputs, max_length=1000, min_length=100, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0])
    print(summary)
    return summary