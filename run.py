import uvicorn
from starlette.applications import Starlette
from app import routes
import os

print("##### PORT: ",os.getenv("PORT"))
print("##### PORT: ",os.getenv("fwd"))
app = Starlette(debug=True,
    routes = routes)

if __name__=="__main__":
    uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug",reload=True)
    # uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug")