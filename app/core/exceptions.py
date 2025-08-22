from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def http_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)}
        )
