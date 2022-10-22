from fastapi import APIRouter

from auth.auth import jwt_authentication, SECRET, fastapi_users
from auth.handlers.users import on_after_register, on_after_forgot_password, after_verification_request
from auth.utils.db_init import database

router = APIRouter(
    tags=['auth'],
    responses={404: {"description": "Not found"}}
)

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()
