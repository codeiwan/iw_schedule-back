# 로그인 및 인증 API
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/api/login")
async def login(request: LoginRequest):
    if request.email == "admin@rian.com" and request.password == "admin!":
        return {"message": "로그인 성공"}
    raise HTTPException(status_code=401, detail="로그인 실패")
