from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, firebase_test

app = FastAPI()
app.include_router(auth.router)
app.include_router(firebase_test.router)

# CORS 설정 (프론트엔드와 통신 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 특정 도메인만 허용하려면 ["http://localhost:5500"]처럼 설정 가능, 실제 서비스에서는 안전하게 특정 출처만 허용
    allow_credentials=True,
    allow_methods=["*"],  # 필요한 메서드만 허용하려면 ["GET", "POST"]처럼 설정 가능
    allow_headers=["*"],  # 필요한 헤더만 적용하려면 ["Authorization", "Content-Type"]처럼 설정 가능
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return {"status": "success", "message": "백엔드와 프론트엔드 연결 성공!"}
