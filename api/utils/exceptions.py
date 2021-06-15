from typing import Optional

from starlette.requests import Request
from starlette.responses import JSONResponse


class Exception_500(Exception):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name


class Exception_400(Exception):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name


class Exception_404(Exception):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name


class Exception_409(Exception):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name


class Exception_422(Exception):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name

#
# @app.exception_handler(Exception_500)
# async def Exception_500_Handler(request: Request, exception: Exception_500):
#     return JSONResponse(status_code=500, content={"message": "Server critical error"})
#
#
# @app.exception_handler(Exception_400)
# async def Exception_404_Handler(request: Request, exception: Exception_400):
#     return JSONResponse(status_code=400, content={"message": "400 error"})
#
#
# @app.exception_handler(Exception_404)
# async def Exception_404_Handler(request: Request, exception: Exception_404):
#     return JSONResponse(status_code=404, content={"message": "not found"})
#
#
# @app.exception_handler(Exception_422)
# async def Exception_422_Handler(request: Request, exception: Exception_422):
#     return JSONResponse(status_code=422, content={"message": "validation error"})
