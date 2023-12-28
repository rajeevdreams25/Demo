from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class FileResponse(BaseModel):
    filename: str

@app.get("/")
def read_root():
    return {"message": "Hello, Mindspace ai!"}

@app.post("/items/")
def create_item(item: Item):
    return item.dict()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return FileResponse(filename=file.filename)


