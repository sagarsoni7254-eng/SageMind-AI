from fastapi import FastAPI

app = FastAPI(
    title="SageMind AI",
    version="0.1.0",
    description="AI-powered multi-agent stock research platform",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to SageMind AI 🚀",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }