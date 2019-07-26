import requests
import base64
import cv2
import requests


URL = "http://127.0.0.1:5000/add_face"

#  first, encode our image with base64
cap = cv2.VideoCapture(0)
while(1):
    retval, image = cap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    response = requests.post(URL, data={"num":3, "img":jpg_as_text})
    print(response.content)
