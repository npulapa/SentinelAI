from fastapi import APIRouter

router = APIRouter()

@router.post("/video")
def detect_video(data: dict):

    return {
        "fraud_probability": 80,
        "trust_score": 20,
        "status": "DEEPFAKE_RISK",
        "note": "CNN model will be integrated later"
    }
