from fastapi import FastAPI
from routes.events import event_router
from routes.users import user_router


app = FastAPI()
app.include_router(router=event_router)
app.include_router(router=user_router)