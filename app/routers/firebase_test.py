# Firebase 연결 확인 API
from fastapi import APIRouter
from app.database import db

router = APIRouter()

@router.get("/firebase-test")
async def firebase_test():
    try:
        # 테스트용 Firestore 컬렉션 접근
        test_ref = db.collection("test").document("connection_test")
        test_ref.set({"message": "Firebase 연결 성공!"})
        
        return {"message": "Firebase 연결이 성공적으로 확인되었습니다!"}
    except Exception as e:
        return {"error": f"Firebase 연결 실패: {str(e)}"}
