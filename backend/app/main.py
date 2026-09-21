from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth
from app.api.routes import channels
from app.api.routes import health
from app.api.routes import messages
from app.api.routes import notifications
from app.api.routes import users
from app.api.routes import websocket
from app.api.routes import workspaces

from app.db.database import Base, engine

from app.db import channel_members
from app.db import channel_models
from app.db import message_models
from app.db import models
from app.db import notification_models
from app.db import workspace_models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Real-Time Collaboration Platform",
    version="1.0.0",
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(workspaces.router)
app.include_router(channels.router)
app.include_router(messages.router)
app.include_router(websocket.router)
app.include_router(notifications.router)


@app.get("/")
def root():
    return {
        "message": "Real-Time Collaboration Platform API",
        "status": "running",
    }