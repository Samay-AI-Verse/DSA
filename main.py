from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def show():
    return "sarted...."



