from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Welcome to gpt'D", "code": 200}