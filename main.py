from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image, ImageOps
from io import BytesIO
import base64

class Img(BaseModel):
    base64: str

app = FastAPI()

def format_checking(image):
    if image[0:5] == "iVBOR":
        format_img = "PNG"
    elif image[0:4] == "/9j/":
        format_img = "JPEG"
    elif image[0:2] == "Qk":
        format_img = "BMP"
    else:
        print("Unknown image format")
    return(format_img)

@app.post("/augmentation/resize")
async def resize(img: Img, width: int, height: int):
    format_img = format_checking(img.base64)
    image = Image.open(BytesIO(base64.b64decode(img.base64)))
    resize_image = image.resize((width,height))

    buffered = BytesIO()
    resize_image.save(buffered, format=format_img)
    result_image = base64.b64encode(buffered.getvalue())
    return {"resize_image": result_image}

@app.post("/augmentation/crop")
async def crop(img: Img, point1: int, point2: int, point3: int, point4: int):
    format_img = format_checking(img.base64)
    image = Image.open(BytesIO(base64.b64decode(img.base64)))
    box = (point1, point2, point3, point4)
    cropped_image = image.crop(box)

    buffered = BytesIO()
    cropped_image.save(buffered, format=format_img)
    result_image = base64.b64encode(buffered.getvalue())
    return {"cropped_image": result_image}

@app.post("/augmentation/rotate")
async def rotate(img: Img, degrees: int):
    format_img = format_checking(img.base64)
    image = Image.open(BytesIO(base64.b64decode(img.base64)))
    rotate_image = image.rotate(degrees)

    buffered = BytesIO()
    rotate_image.save(buffered, format=format_img)
    result_image = base64.b64encode(buffered.getvalue())
    return {"rotate_image": result_image}

@app.post("/augmentation/compression")
async def compression(img: Img, quality: int):
    format_img = format_checking(img.base64)
    image = Image.open(BytesIO(base64.b64decode(img.base64)))

    buffered = BytesIO()
    image.save(buffered, format_img, optimize = True, quality=quality)
    result_image = base64.b64encode(buffered.getvalue())
    return {"compression_image": result_image}

@app.post("/augmentation/negative")
async def negative(img: Img):
    format_img = format_checking(img.base64)
    image = Image.open(BytesIO(base64.b64decode(img.base64)))

    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        negative_image = ImageOps.invert(rgb_image)
        r2, g2, b2 = negative_image.split()
        negative_image = Image.merge('RGBA', (r2, g2, b2, a))
    else:
        negative_image = ImageOps.invert(image)

    buffered = BytesIO()
    negative_image.save(buffered, format=format_img)
    result_image = base64.b64encode(buffered.getvalue())
    return {"negative_image": result_image}
