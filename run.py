import uvicorn
from starlette.applications import Starlette
from app import routes
import os


app = Starlette(debug=True,
    routes = routes)

if __name__=="__main__":
    print("##### PORT: ",os.getenv("PORT"))
    print("##### PORT: ",os.getenv("HOST"))
    print("##### PORT: ",os.getenv("host"))
    # uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug",reload=True)
    uvicorn.run("run:app",workers=10,host=os.getenv("fwd"),port=os.getenv("PORT"),log_level="debug")