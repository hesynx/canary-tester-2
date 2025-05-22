from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Canary Deployment Demo")

APP_VERSION = "v2.0"

@app.get("/")
async def root():
    return {
        "message": "Hello from Canary App",
        "version": APP_VERSION,
        "color": "green"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
