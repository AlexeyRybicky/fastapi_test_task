from fastapi import APIRouter

from .views import router as profile_router

router = APIRouter()
router.include_router(router=profile_router, prefix="/profile")
