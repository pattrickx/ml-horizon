import uvicorn
from starlette.applications import Starlette
from app import routes
import socket
import os

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
# from starlette.middleware.trustedhost import TrustedHostMiddleware

# # Ensure that all requests include an 'example.com' or '*.example.com' host header,
# # and strictly enforce https-only access.
# middleware = [
#   Middleware(TrustedHostMiddleware, allowed_hosts=['example.com', '*.example.com']),
#   Middleware(HTTPSRedirectMiddleware)
# ]


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(debug=True, routes=routes, middleware=middleware)

if __name__=="__main__":
    print("##### PORT: ",os.getenv("PORT"))
    host_name = socket.gethostname()
    print(host_name )
    print("##### BASE_IRI: ",socket.gethostbyname(host_name))
    # uvicorn.run("run:app",workers=10,host='0.0.0.0',port=5000,log_level="debug",reload=True)
    uvicorn.run("run:app",host=socket.gethostbyname(host_name),workers=1,port=int(os.getenv("PORT")),log_level="debug")