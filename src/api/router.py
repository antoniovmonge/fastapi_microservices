from fastapi.routing import APIRouter

from src.api import (
    orders,
    # users, ping, general
)

router = APIRouter()
router.include_router(orders.router, prefix="/orders", tags=["orders"])
# router.include_router(general.router, tags=["general"])
# router.include_router(users.router, prefix="/users", tags=["users"])
# router.include_router(ping.router, prefix="/ping", tags=["ping"])
