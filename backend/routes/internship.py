from fastapi import APIRouter

router = APIRouter()

@router.post("/internship")
def detect_internship(data: dict):

    company = data.get("company")
    email = data.get("email")
    salary = data.get("salary")
    website = data.get("website")

    # SIMPLE RULE-BASED MODEL (for now)
    score = 0

    if "gmail" in email:
        score += 40

    if "xyz" in website or "careers" in website:
        score += 30

    if int(salary) > 100000:
        score += 20

    fraud_probability = min(score + 20, 100)
    trust_score = 100 - fraud_probability

    status = "FAKE" if fraud_probability > 60 else "SAFE"

    return {
        "fraud_probability": fraud_probability,
        "trust_score": trust_score,
        "status": status,
        "reasons": [
            "Checked email domain",
            "Website pattern analysis",
            "Salary anomaly detection"
        ]
    }
