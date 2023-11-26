from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
import os
import uvicorn

app = FastAPI()

count = 0

@app.get("/hello")
def hello():
    return {"message": "Hello Ry"}

@app.get("/count")
async def counter():
    global count
    count += 1
    return {"count": count}

@app.get("/getcount")
async def getcounter():
    return {"count": count}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/report")
async def receive_data(request: Request, screenshot1: Optional[UploadFile] = File(...), screenshot2: Optional[UploadFile] = File(...)):
    form = await request.form()
    issue = form.get('issue')

    # Save the files or process the data as needed
    print(issue)

    with open(os.path.join("uploads", screenshot1.filename), "wb") as buffer:
        content = await screenshot1.read()  # async read
        buffer.write(content)
    
    with open(os.path.join("uploads", screenshot2.filename), "wb") as buffer:
        content = await screenshot2.read()  # async read
        buffer.write(content)

    return JSONResponse(content={"status": "success"}, status_code=200)

# To run the application use command: uvicorn main:app --reload
