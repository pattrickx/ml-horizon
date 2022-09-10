from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.requests import Request
from src.summarization.summarization import *


async def summarize(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        
        if "text" not in body:
            raise Exception("invalid body, text not found")
        
    except Exception as e:
        return JSONResponse({"ERROR":e},status_code=500)
    
    try: 
        luhn_summy_text = luhn_summarizer(body["text"])
        hug_summy_text = hug_ptt5_base_summ_xlsum(body["text"])
        
    except Exception as e:
        return JSONResponse({"ERROR":f"text can't by summarized: {e}"},status_code=500)
        
    return JSONResponse({"luhn_summy_text":luhn_summy_text,"hug_summy_text":hug_summy_text},status_code=200)

async def test(request: Request) -> JSONResponse:
    return JSONResponse({"Online":"OK"},status_code=200)

routes =[ Route('/',endpoint=test,methods=["GET"]),
    Mount("/ai",routes=[
        Route('/summarize',endpoint=summarize,methods=["GET"])])
    ]
