from fastapi import Request, status
from fastapi.responses import JSONResponse

class CustomAppException(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "Đã xảy ra lỗi hệ thống."

    def __init__(self, detail: str = None, status_code: int = None):
        if detail:
            self.detail = detail
        if status_code:
            self.status_code = status_code

class EmailAlreadyExistsException(CustomAppException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Email này đã được đăng ký trên hệ thống."

class InvalidCredentialsException(CustomAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Email hoặc mật khẩu không chính xác."

class UserNotFoundException(CustomAppException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Không tìm thấy người dùng này."

async def global_app_exception_handler(request: Request, exc: CustomAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.__class__.__name__, # Tự động lấy tên Class làm Code lỗi (ví dụ: EmailAlreadyExistsException)
                "message": exc.detail
            }
        },
    )