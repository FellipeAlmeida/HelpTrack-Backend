from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import (
    ModuleNotFound,
    UserBlocked,
    UserNotAuthorized,
    TokenError,
    CredentialsError,
    UserNotActive,
    InvalidData,
    ExistingModule
)

async def module_not_found_handler(request: Request, exc: ModuleNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "detail": exc.message
        }
    )

async def user_blocked_handler(request: Request, exc: UserBlocked):
    return JSONResponse(
        status_code=403,
        content={
            "detail": exc.message
        }
    )

async def user_not_authorized_handler(request: Request, exc: UserNotAuthorized):
    return JSONResponse(
        status_code=403,
        content={
            "detail": exc.message
        }
    )

async def token_error_handler(request: Request, exc: TokenError):
    return JSONResponse(
        status_code=401,
        content={
            "detail": exc.message
        }
    )

async def credentials_error_handler(request: Request, exc: CredentialsError):
    return JSONResponse(
        status_code=401,
        content={
            "detail": exc.message
        }
    )

async def user_not_active_handler(request: Request, exc: UserNotActive):
    return JSONResponse(
        status_code=403,
        content={
            "detail": exc.message
        }
    )

async def invalid_data_handler(request: Request, exc: InvalidData):
    return JSONResponse(
        status_code=401,
        content={
            "detail": exc.message
        }
    )

async def existing_module_handler(request: Request, exc: ExistingModule):
    return JSONResponse(
        status_code=409,
        content={
            "detail": exc.message
        }
    )