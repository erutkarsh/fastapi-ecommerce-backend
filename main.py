from fastapi import FastAPI
from routes.user_routes import router as user_router
from database.connection import engine
from database.models import Base


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/users")
