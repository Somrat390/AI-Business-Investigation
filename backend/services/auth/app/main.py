from fastapi import FastAPI  #type: ignore[import-not-found]

app = FastAPI(title="Auth Service")


@app.get("/")
def root():
    return {"message": "Auth Service is running"}