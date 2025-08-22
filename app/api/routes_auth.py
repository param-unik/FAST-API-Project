from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.core.security import create_access_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str
    
@router.post("/login", response_model=AuthInput)
async def login(auth: AuthInput):
    if auth.username == 'admin' and auth.password == 'admin':
        token = create_access_token(data={"sub": auth.username})
        return {"access_token": token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")





        
