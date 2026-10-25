from fastapi import FastAPI

app = FastAPI(title="AI Investigation Gateway")


@app.get("/")
def root():
    return {"message": "Gateway is running"}