from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import *
import json as json2

client = TestClient(app)

def image_resize_test(image):
    with open(image, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json={"base64": str(image_base64)}
    response = client.post("augmentation/resize?width=300&height=300", json=json)
    print(response.status_code)
    assert response.status_code == 200
    json_data = json2.loads(response.text)
    result_image = json_data["resize_image"]
    new_image = Image.open(BytesIO(base64.b64decode(result_image)))

def image_crop_test(image):
    with open(image, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json={"base64": str(image_base64)}
    response = client.post("augmentation/crop?point1=50&point2=50&point3=200&point4=300", json=json)
    print(response.status_code)
    assert response.status_code == 200
    json_data = json2.loads(response.text)
    result_image = json_data["cropped_image"]
    new_image = Image.open(BytesIO(base64.b64decode(result_image)))

def image_rotate_test(image):
    with open(image, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json={"base64": str(image_base64)}
    response = client.post("augmentation/rotate?degrees=90", json=json)
    print(response.status_code)
    assert response.status_code == 200
    json_data = json2.loads(response.text)
    result_image = json_data["rotate_image"]
    new_image = Image.open(BytesIO(base64.b64decode(result_image)))

def image_compression_test(image):
    with open(image, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json={"base64": str(image_base64)}
    response = client.post("augmentation/compression?quality=90", json=json)
    print(response.status_code)
    assert response.status_code == 200
    json_data = json2.loads(response.text)
    result_image = json_data["compression_image"]
    new_image = Image.open(BytesIO(base64.b64decode(result_image)))

def image_negative_test(image):
    with open(image, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json={"base64": str(image_base64)}
    response = client.post("augmentation/negative", json=json)
    print(response.status_code)
    assert response.status_code == 200
    json_data = json2.loads(response.text)
    result_image = json_data["negative_image"]
    new_image = Image.open(BytesIO(base64.b64decode(result_image)))

print("Resize test")
image_resize_test("test.jpg")
image_resize_test("test.bmp")
image_resize_test("test.png")

print("Crop test")
image_crop_test("test.jpg")
image_crop_test("test.bmp")
image_crop_test("test.png")

print("Rotate test")
image_rotate_test("test.jpg")
image_rotate_test("test.bmp")
image_rotate_test("test.png")

print("compression test")
image_compression_test("test.jpg")
image_compression_test("test.bmp")
image_compression_test("test.png")

print("Negative test")
image_negative_test("test.jpg")
image_negative_test("test.bmp")
image_negative_test("test.png")
