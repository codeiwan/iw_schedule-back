# 로그인 및 인증 API
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

# .env에서 Firebase credentials 경로를 가져오기
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

# Firebase Admin SDK 초기화
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

# class LoginRequest(BaseModel):
#     id_token: str  # ID 토큰을 전달받습니다.

class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    email: str
    password: str

# 로그인
@router.post("/api/login")
async def login(request: LoginRequest):
    try:
        # 강제로 admin 계정으로 로그인 처리
        if request.email == "admin" and request.password == "admin!":
            # 강제로 로그인 성공 처리
            id_token = "your_generated_jwt_token"  # JWT 토큰을 발급하는 방법은 별도로 추가 가능

            return {"message": "로그인 성공", "user_id": "admin", "id_token": id_token}
        else:
            raise HTTPException(status_code=400, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Login failed: " + str(e))

# 회원가입
@router.post("/api/signup")
async def signup(request: SignupRequest):
    try:
        # Firebase Authentication을 이용해 새로운 사용자 등록
        user = auth.create_user(
            email=request.email,
            password=request.password
        )
        return {"message": "회원가입 성공", "user_id": user.uid}
    except firebase_admin.exceptions.FirebaseError as e:
        raise HTTPException(status_code=400, detail=str(e))
