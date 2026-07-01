import datetime

import jwt
from users.domain.token import EncryptedToken, Token
from users.domain.user import User, UserId
from users.domain.token_handler import TokenHandler
from shared.infrastructure.config.config import settings

class JwtTokenHandler(TokenHandler):
    
    def create_token(self, user : User) -> EncryptedToken:
        now = datetime.datetime.utcnow()
        exp = now + datetime.timedelta(minutes=settings.JWT_EXPIRE_TIME_IN_MINUTES)
        payload: dict[str, str | datetime.datetime] = {
            "sub" : str(user.uid.uid),
            "exp" : exp,
            "iat" : now
        }
        return EncryptedToken(
            jwt.encode( #type: ignore
                payload,
                key=settings.JWT_SECRET_KEY,
                algorithm=settings.JWT_ALGORITHM,
            ) 
        )
    
    def decode_token(self, token : EncryptedToken) -> Token:
        decoded : dict[str, str | datetime.datetime] = jwt.decode( #type: ignore
            token.as_raw,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        assert decoded["sub"] is not None and isinstance(decoded["sub"],str)
        return Token(
            UserId(int(decoded["sub"]))
        )
