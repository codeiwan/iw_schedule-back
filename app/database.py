# Firebase 연결 관리
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# Firebase 인증 정보 불러오기
cred_path = os.getenv("FIREBASE_CREDENTIALS")

# Firebase 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Firestore DB 객체 생성
db = firestore.client()
