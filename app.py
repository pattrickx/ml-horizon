from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.requests import Request
from src.summarization.summarization import luhn_summarizer


async def summarize(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        
        if "text" not in body:
            raise Exception("invalid body, text not found")
        if "sentences_n" not in body:
            raise Exception("invalid body, sentences_n not found")
        
    except Exception as e:
        return JSONResponse({"ERROR":e},status_code=500)
    
    try: 
        summy_text = luhn_summarizer(body["text"],body["sentences_n"])
        
    except Exception as e:
        return JSONResponse({"ERROR":f"text can't by summarized: {e}"},status_code=500)
        
    return JSONResponse({"summarized_text":summy_text},status_code=200)

async def test(request: Request) -> JSONResponse:
    return JSONResponse({"Online":"OK"},status_code=200)

routes =[ Route('/',endpoint=test,methods=["GET"]),
    Mount("/ai",routes=[
        Route('/summarize',endpoint=summarize,methods=["POST"])])
    ]
