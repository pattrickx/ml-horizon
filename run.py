import uvicorn
from starlette.applications import Starlette
from app import routes
import socket
import os


app = Starlette(debug=True,
    routes = routes)

if __name__=="__main__":
    print("##### PORT: ",os.getenv("PORT"))
    host_name = socket.gethostname()
    print(host_name )
    print("##### BASE_IRI: ",socket.gethostbyname(host_name))
    uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug",reload=True)
    # uvicorn.run("run:app",host=socket.gethostbyname(host_name),workers=1,port=int(os.getenv("PORT")),log_level="debug")