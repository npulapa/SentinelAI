from fastapi import APIRouter

router = APIRouter()

@router.post("/image")
def detect_image(data: dict):

    return {
        "fraud_probability": 70,
        "trust_score": 30,
        "status": "SUSPICIOUS",
        "note": "Deepfake model will be added later"
    }
