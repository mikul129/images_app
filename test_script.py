import argparse
from fastapi.testclient import TestClient
import json
from main import *
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-res", "--resize", nargs='+', help='width_height')
parser.add_argument("-cro", "--crop", nargs='+', help='point1_point2_point3_point4')
parser.add_argument("-rot", "--rotate", help='degrees')
parser.add_argument("-com", "--compression", help='quality')
parser.add_argument("-neg", "--negative", nargs='?', help='width_height', const='')

parser.add_argument("-i", "--input", help='path_input_image')
parser.add_argument("-o", "--output", help='output_name_image')
parser.add_argument("-u", "--url", help='url_serwer', default="http://127.0.0.1:8000")

args = parser.parse_args()

image = args.input

client = TestClient(app)


def resize_image():
    with open(args.input, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json_body = {"base64": str(image_base64)}
    request_url = (str(args.url) + "/augmentation/resize?width=" + str(args.resize[0]) + "&height=" + str(args.resize[1]))
    response = (json.loads(requests.post(request_url, json=json_body).text))["resize_image"]
    new_image = Image.open(BytesIO(base64.b64decode(response)))
    new_image.save(args.output)


def crop_image():
    with open(args.input, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json_body = {"base64": str(image_base64)}
    request_url = (str(args.url) + "/augmentation/crop?point1=" + str(args.crop[0]) + "&point2=" + str(args.crop[1]) + "&point3=" + str(args.crop[2]) + "&point4=" + str(args.crop[3]))
    response = (json.loads(requests.post(request_url, json=json_body).text))["cropped_image"]
    new_image = Image.open(BytesIO(base64.b64decode(response)))
    new_image.save(args.output)


def rotate_image():
    with open(args.input, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json_body = {"base64": str(image_base64)}
    request_url = (str(args.url) + "/augmentation/rotate?degrees=" + args.rotate)
    response = (json.loads(requests.post(request_url, json=json_body).text))["rotate_image"]
    new_image = Image.open(BytesIO(base64.b64decode(response)))
    new_image.save(args.output)


def compression_image():
    with open(args.input, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json_body = {"base64": str(image_base64)}
    request_url = (str(args.url) + "/augmentation/compression?quality=" + args.compression)
    response = (json.loads(requests.post(request_url, json=json_body).text))["compression_image"]
    new_image = Image.open(BytesIO(base64.b64decode(response)))
    new_image.save(args.output)


def negative_image():
    with open(args.input, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read())
    image_base64 = image_base64.decode("utf-8")
    json_body = {"base64": str(image_base64)}
    request_url = (str(args.url) + "/augmentation/negative")
    response = (json.loads(requests.post(request_url, json=json_body).text))["negative_image"]
    new_image = Image.open(BytesIO(base64.b64decode(response)))
    new_image.save(args.output)


if args.resize != None:
    resize_image()

if args.crop != None:
    crop_image()

if args.rotate != None:
    rotate_image()

if args.compression != None:
    compression_image()

if args.negative != None:
    negative_image()
