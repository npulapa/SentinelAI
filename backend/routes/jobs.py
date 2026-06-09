from fastapi import APIRouter

router = APIRouter()

@router.post("/jobs")
def detect_job(data: dict):

    email = data.get("email")
    salary = data.get("salary")

    score = 10

    if "gmail" in email:
        score += 50

    if int(salary) > 150000:
        score += 20

    fraud_probability = min(score, 100)
    trust_score = 100 - fraud_probability

    return {
        "fraud_probability": fraud_probability,
        "trust_score": trust_score,
        "status": "FAKE" if fraud_probability > 60 else "SAFE"
    }
