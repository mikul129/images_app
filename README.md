# image_app
## Description
A tool for making photo operations:
- resize the image
- crop the image
- rotate the image
- compression the image
- create a negative image

## Files

main.py - file with api methods<br />
test_script.py - file with test script methods<br />
unit_tests.py - file with unit tests<br />


## Libraries

requirements.txt:<br />
certifi==2020.12.5<br />
chardet==4.0.0<br />
fastapi==0.63.0<br />
idna==2.10<br />
Pillow==8.2.0<br />
pydantic==1.8.1<br />
requests==2.25.1<br />
starlette==0.13.6<br />
typing-extensions==3.7.4.3<br />
urllib3==1.26.4<br />

## Quick start
In folder with files write a command:
```
uvicorn main:app --reload
```
Now we should have access to swagger on address:<br />
http://127.0.0.1:8000/docs<br />
(for example in your browser)<br />

#Test tool
test_script.py is script for tests.

Example run in cmd:<br />
```
test_script.py --input testin.jpg --output testout.jpg --resize 200 200
```

You have many options to choose from:<br />
```--input path_to_image``` - input file<br />
```--output path_to_save_image``` - output file<br />
```--resize value_width value_height``` - option for resize image<br />
```--crop point1 point2 point3 point4``` - option for crop image<br />
```--rotate degrees``` - option for rotate image<br />
```--compression quality``` - option for compression image<br />
```--negative``` - option for negative image<br />
```--url``` - url api server default - http://127.0.0.1:8000<br /><br />

## API methods
### POST /augmentation/resize<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/resize?width=value_width&height=value_height<br />

value_width - target width<br />
value_height - target height<br />

Request body:<br />
```
{
  "base64": "string"#image in base64 code
}
```
Response body:<br />
```
{
  "resize_image": "string"#image in base64 code
}
```
### POST /augmentation/crop<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/crop?point1='value1'&point2='value2'&point3='value3'&point4='value4'<br />
value1 - coordinate x of the point<br />
value2 - coordinate y of the point<br />
value3 - distance from a point on the x axis<br />
value4 - distance from a point on the y axis<br />

Request body:<br />
```
{
  "base64": "string"#image in base64 code
}
```
Response body:<br />
```
{
  "cropped_image": "string"#image in base64 code
}
```
### POST /augmentation/rotate<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/rotate?degrees='value_degrees'<br />
value_degrees - degrees of rotation<br />

Request body:<br />
```
{
  "base64": "string"#image in base64 code
}
```
Response body:<br />
```
{
  "rotate_image": "string"#image in base64 code
}
```
### POST /augmentation/compression<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/compression?quality='value_quality'

value_quality - target quality(0 - low 100 - high)

Request body:<br />
```
{
  "base64": "string"#image in base64 code
}
```
Response body:<br />
```
{
  "compression_image": "string"#image in base64 code
}
```
### POST /augmentation/negative<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/negative

Request body:<br />
```
{
  "base64": "string"#image in base64 code
}
```
Response body:<br />
```
{
  "negative_image": "string"#image in base64 code
}
```

## Contact
mikulski.michal2@gmail.com
