from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('The base is cleaned')
    await create_tables()
    print('The base is ready')
    yield
    print('Turning off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
