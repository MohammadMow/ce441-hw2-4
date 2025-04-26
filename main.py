from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def redirect_to_secret():
    return RedirectResponse(url="http://127.0.0.1:5004/secret")
