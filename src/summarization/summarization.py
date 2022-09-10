import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

from transformers import pipeline

def luhn_summarizer(full_text:str,lang:str="portuguese", sentences_n:int=5) -> str : 

    parser =  PlaintextParser.from_string(full_text,Tokenizer(lang))
    summarization =LuhnSummarizer()
    summy_list =  summarization(parser.document,sentences_n)
    
    summy_text=""
    for sent in summy_list:
        summy_text+= str(sent)+" "
        
    return summy_text

def hug_wikilingua(full_text:str,lang:str="portuguese", max_length:int=100, min_length:int = 50)-> str:
    summarize = pipeline("summarization", model="phpaiola/ptt5-base-summ-wikilingua")
    if lang!="portuguese":
        summarize = pipeline("summarization", model="facebook/bart-large-cnn")
        
    return summarize(full_text,max_length=max_length,min_length=min_length)['summary_text']