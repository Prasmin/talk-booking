from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/health-check/")
def health_check():
    return {"message": "OK"}