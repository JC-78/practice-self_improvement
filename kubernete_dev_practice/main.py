from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Kubernetes!"}

@app.get("/process")
def process(data: str):
    return {"processed_data": data.upper()}
