def generate_reasons(module: str):

    reasons = {
        "internship": [
            "Email domain mismatch detected",
            "Suspicious website pattern",
            "Salary anomaly found"
        ],
        "email": [
            "Urgent keyword detected",
            "Suspicious sender domain",
            "Phishing pattern match"
        ],
        "website": [
            "Untrusted domain",
            "No SSL certificate",
            "Fake login pattern detected"
        ]
    }

    return reasons.get(module, ["Pattern anomaly detected"])
