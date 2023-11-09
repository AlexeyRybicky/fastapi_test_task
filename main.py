from contextlib import asynccontextmanager

import uvicorn
from api.auth.schemas import UserRead, UserCreate
from api.auth.strategy import auth_backend, fastapi_users
from api.books import router as router_books
from api.authors import router as router_authors
from api.profile import router as router_profile
from core.config import settings
from core.logger import listener

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Тестовое задание",
)
app.include_router(
    router=router_authors,
    prefix=settings.api_authors_prefix,
)
app.include_router(
    router=router_books,
    prefix=settings.api_books_prefix,
)
app.include_router(
    router=router_profile,
    prefix=settings.api_profile_prefix,
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
    prefix="/auth",
    tags=["auth"],
)


@app.on_event("shutdown")
async def shut_down_event():
    listener.stop()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
