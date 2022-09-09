import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
import nltk
nltk.download('punkt')

def luhn_summarizer(full_text:str,lang:str="portuguese", sentences_n:int=5) -> str : 

    parser =  PlaintextParser.from_string(full_text,Tokenizer(lang))
    summarization =LuhnSummarizer()
    summy_list =  summarization(parser.document,sentences_n)
    
    summy_text=""
    for sent in summy_list:
        summy_text+= str(sent)+" "
        
    return summy_text