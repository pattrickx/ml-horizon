import uvicorn
from starlette.applications import Starlette
from app import routes



app = Starlette(debug=True,
    routes = routes)

if __name__=="__main__":
    uvicorn.run("run:app",workers=10,host='0.0.0.0',port=80,log_level="debug",reload=True)
    # uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug")