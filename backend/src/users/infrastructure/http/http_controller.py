from fastapi import APIRouter, Depends, HTTPException

from users.application.get_user import GetUserInfoUseCase, UserNoExistsException
from users.infrastructure.http.dto.user_info import UserInfoDto

from ..application_di.di import get_get_user_uc, get_login_user_uc, get_register_user_uc
from ...application.register_user import RegisterUserUseCase
from .dto.register_dto import RegisterDto
from ...application.auth_facade import UnauthorizedException, UnprocessableRegisterException, UserNotFoundException
from ...domain.token import EncryptedToken
from ...application.login_user import LoginUserUseCase
from .dto.login_dto import LoginDto


router = APIRouter(prefix="/users",tags=["users"])

@router.get("/{user_id}")
async def get_user_info(user_id : int, use_case : GetUserInfoUseCase = Depends(get_get_user_uc) ):
    try:
        db_user = await use_case.execute(user_id)
        return UserInfoDto(
            id = db_user.uid.uid,
            name = db_user.name.name,
            email = db_user.credentials.email.email
        )
    
    except UserNoExistsException:
        raise HTTPException(
            status_code=404,
            detail="User couldn't be found"
        )
    except Exception as e:
        print(e.__str__())
        raise e

@router.post(path="/login")
async def login_user(body : LoginDto, use_case : LoginUserUseCase = Depends(get_login_user_uc)):
    try:
        token : EncryptedToken = await use_case.execute(body.email,body.password)
        return {
            "access_token" : token.as_raw,
            "token_type" : "BEARER"
        }
    except UserNotFoundException:
        return HTTPException(
            status_code=401,
            detail="User does not exists"
        )
    except UnauthorizedException:
        return HTTPException(
            status_code=401,
            detail="Email or password wrong"
        )
    except Exception as e:
        print(e.__str__())
        raise e

@router.post(path="/register")
async def register_user(body : RegisterDto, use_case : RegisterUserUseCase = Depends(get_register_user_uc)):
    try:
        await use_case.execute(
            body.name,
            body.email,
            body.password
        )
    except UnprocessableRegisterException:
        raise HTTPException(
            status_code=422,
            detail="Impossible to register"
        )
    except Exception as e:
        print(e.__str__())
        raise e