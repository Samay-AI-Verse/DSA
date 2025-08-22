from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def show():
    return "sarted...."

lists = [1,2,3,4,5]

@app.get("/show")
def my():
    return lists



