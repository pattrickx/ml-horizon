import uvicorn
from starlette.applications import Starlette
from app import routes
import os



app = Starlette(debug=True,
    routes = routes)

if __name__=="__main__":
    print("##### PORT: ",os.getenv("PORT"))
    # uvicorn.run("run:app",workers=10,host='0.0.0.0',port=3000,log_level="debug",reload=True)
    uvicorn.run("run:app",workers=10,host='0.0.0.0',port=os.getenv("PORT"),log_level="debug")