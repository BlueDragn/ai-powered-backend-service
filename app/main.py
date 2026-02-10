from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend service is up and running!"}