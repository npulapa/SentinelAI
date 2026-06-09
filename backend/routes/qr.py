from fastapi import APIRouter

router = APIRouter()

@router.post("/qr")
def detect_qr(data: dict):

    url = data.get("url")

    if "http" in url and "login" in url:
        return {
            "fraud_probability": 85,
            "trust_score": 15,
            "status": "DANGEROUS"
        }

    return {
        "fraud_probability": 20,
        "trust_score": 80,
        "status": "SAFE"
    }
