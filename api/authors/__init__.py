from fastapi import APIRouter

from .views import router as authors_router

router = APIRouter()
router.include_router(router=authors_router, prefix="/authors")
