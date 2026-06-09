from fastapi import FastAPI
from routes import internship, jobs, email, sms, website, qr, image, video

app = FastAPI(
    title="SentinelAI",
    description="Unified Cyber Fraud Detection Platform",
    version="1.0"
)

# Root
@app.get("/")
def home():
    return {"message": "SentinelAI Backend is Running"}

# Include routes
app.include_router(internship.router, prefix="/api")
app.include_router(jobs.router, prefix="/api")
app.include_router(email.router, prefix="/api")
app.include_router(sms.router, prefix="/api")
app.include_router(website.router, prefix="/api")
app.include_router(qr.router, prefix="/api")
app.include_router(image.router, prefix="/api")
app.include_router(video.router, prefix="/api")
