from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Canary Deployment Demo")

APP_VERSION = "v1.0"

@app.get("/")
async def root():
    return {
        "message": "Hello from Canary App",
        "version": APP_VERSION,
        "color": "blue"
    }

@app.get("/health")
async def health():
    # Simulate a failure
    raise HTTPException(status_code=500, detail="Simulated internal server error in health check")
    # return {"status": "healthy"} # Original healthy response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
