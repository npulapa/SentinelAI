from fastapi import APIRouter

router = APIRouter()

@router.post("/email")
def detect_email(data: dict):

    content = data.get("content")

    score = 0

    if "urgent" in content.lower():
        score += 30

    if "verify" in content.lower():
        score += 30

    if "click" in content.lower():
        score += 30

    fraud_probability = min(score + 10, 100)

    return {
        "fraud_probability": fraud_probability,
        "trust_score": 100 - fraud_probability,
        "status": "PHISHING" if fraud_probability > 60 else "SAFE"
    }
