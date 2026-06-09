def calculate_trust_score(fraud_probability: float):

    trust_score = 100 - fraud_probability

    if trust_score < 0:
        trust_score = 0

    return round(trust_score, 2)
