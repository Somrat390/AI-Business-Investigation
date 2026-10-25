from fastapi import FastAPI  # type: ignore[import-not-found]

app = FastAPI(title="AI Investigation Gateway")


@app.get("/")
def root():
    return {"message": "Gateway is running"}