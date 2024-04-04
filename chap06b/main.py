from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.events import event_router
from routes.users import user_router
import uvicorn


app = FastAPI()
app.include_router(router=event_router, prefix="/event")
app.include_router(router=user_router, prefix="/user")

@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    """Landing node"""
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
    )
