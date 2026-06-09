from fastapi import APIRouter

router = APIRouter()

@router.post("/website")
def detect_website(data: dict):

    url = data.get("url")

    score = 0

    if "https" not in url:
        score += 40

    if "xyz" in url or "login" in url:
        score += 30

    return {
        "fraud_probability": min(score + 20, 100),
        "trust_score": 100 - score,
        "status": "FAKE" if score > 50 else "SAFE"
    }
