from fastapi import FastAPI
from app.routes import router
from app.database import create_table
import logging

logging.basicConfig(level=logging.INFO)

create_table()

app = FastAPI(title="Country Currency & Exchange API")

app.include_router(router, prefix="/api/v1")