from fastapi import APIRouter, HTTPException
from typing import Optional
import os
from app.models.record import AudioRecorder

router = APIRouter()

# AudioRecorder 객체 생성
audio_recorder = AudioRecorder()

# 녹음 시작
@router.post("/start_record")
async def start_record():
    try:
        audio_recorder.start_recording()
        return {"message": "녹음이 시작되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="녹음 시작 실패: " + str(e))

# 녹음 종료 및 파일 저장
@router.post("/stop_record")
async def stop_record(filename: Optional[str] = "output_audio.wav"):
    try:
        audio_recorder.stop_recording(filename)
        return {"message": f"녹음이 종료되었습니다. 파일 저장: {filename}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="녹음 종료 실패: " + str(e))

# 녹음 취소
@router.post("/cancel_record")
async def cancel_record():
    try:
        audio_recorder.cancel_recording()
        return {"message": "녹음이 취소되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="녹음 취소 실패: " + str(e))