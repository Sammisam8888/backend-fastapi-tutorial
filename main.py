from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"welcome note":'heyy welcome to the world of sammisam'}

