import logging
import urllib
from typing import Union
from typing import Annotated
from binascii import a2b_base64

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.requests import Request
from base64 import b64decode
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemImage(BaseModel):
    base64: str
    item_name: str


class Image(BaseModel):
    base64: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/dunno/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        with open('batman.jpg', 'wb') as f:
            # print(type(file))
            data = await file.read()
            f.write(data)
        return {"filename": file.filename}


@app.post("/create_category/")
async def create_category(item_image: ItemImage):
    print(item_image)
    return {"item_image": item_image}


@app.post("/get/")
async def inference(image: Image):
    with open("imageToSave.jpg", "wb") as fh:
        fh.write(b64decode(image.base64))

    return {"image": image.base64}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    logging.error(f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

import uvicorn
uvicorn.run(app)