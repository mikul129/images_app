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

fastapi==0.63.0
Pillow==8.2.0

## Quick start
In folder with files write a command:
```
uvicorn main:app --reload
```
Now we should have access to swagger on address:
http://127.0.0.1:8000/docs
(for example in your browser)

#Test tool
test_script.py is script for tests.<br /><br />

Example run in cmd:<br />
```
test_script.py --input test.jpg --output test22.jpg --resize 200 200
```<br /><br />

You have many options to choose from:<br />
```--input path_to_image``` - input file<br />
```--output path_to_save_image``` - output file<br />
```--resize value_width value_height``` - option for resize image<br />
```--crop point1 point2 point3 point4``` - option for crop image<br />
```--rotate degrees``` - option for rotate image<br />
```--compression quality``` - option for compression image<br />
```--negative``` - option for negative image<br />
```--url``` - url api server default - http://127.0.0.1:8000<br />

## API methods
### POST /augmentation/resize<br />
Example request URL<br />
http://127.0.0.1:8000//augmentation/resize?width='value_width'&height='value_height'

value_width - target width
value_height - target height

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
http://127.0.0.1:8000//augmentation/crop?point1='value1'&point2='value2'&point3='value3'&point4='value4'
value1 - coordinate x of the point
value2 - coordinate y of the point
value3 - distance from a point on the x axis
value4 - distance from a point on the y axis

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
http://127.0.0.1:8000//augmentation/rotate?degrees='value_degrees'
value_degrees - degrees of rotation

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

value_quality - target quality(100-low 0-high)

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
