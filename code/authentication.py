import os
from dotenv import load_dotenv
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

load_dotenv()

AUTH_SERVICE_SECRET_KEY = os.getenv('AUTH_SERVICE_SECRET_KEY')
AUTH_SERVICE_ALGORITHM = os.getenv('AUTH_SERVICE_ALGORITHM')


def verify_token(credentials : HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, key=AUTH_SERVICE_SECRET_KEY, algorithms=[AUTH_SERVICE_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or Expired token')


