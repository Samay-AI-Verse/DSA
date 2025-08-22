from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()



@app.get("/")
def show():
    return "sarted...."
