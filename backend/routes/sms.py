from fastapi import APIRouter

router = APIRouter()

@router.post("/sms")
def detect_sms(data: dict):

    text = data.get("text")

    keywords = ["win", "lottery", "click", "prize", "urgent"]

    score = sum(15 for k in keywords if k in text.lower())

    return {
        "fraud_probability": min(score, 100),
        "trust_score": 100 - score,
        "status": "SCAM" if score > 50 else "SAFE"
    }
