from fastapi import HTTPException, status, Header 
from app.core.config import settings
from app.core.security import verify_token
from jose import JWTError

def get_api_token(token: str = Header(...)):
    
    if token != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
def get_current_user(token: str = Header(...)):
    try:
        payload = verify_token(token)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
