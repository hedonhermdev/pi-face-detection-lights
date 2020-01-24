import io
import socket
import struct
import requests
from PIL import Image
import time
import json
from datetime import datetime

import mtcnn
import numpy as np


server_socket = socket.socket()
server_socket.bind(("10.3.141.184", 5000))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile("rb")

CONFIG_FILE = "./config.json"

try:
    with open(CONFIG_FILE) as cf:
        CONFIG = json.load(cf)
except FileNotFoundError:
    print("Could not load config file!")
    exit(1)

MTCNN = mtcnn.MTCNN()

PI_LIGHTS_SERVER = "http://10.3.141.1:5000"

absent_count = 0
present_count = 0

try:
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack("<L", connection.read(struct.calcsize("<L")))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        now = datetime.now()
        image_array = np.array(image)
        detection = MTCNN.detect_faces(image_array)
        if detection:
            if detection[0]["confidence"] > 0.9:
                print("PRESENT")
                present_count += 1
        else:
            absent_count += 1
            print("ABSENT")
        if present_count > 5:
            state = requests.get(PI_LIGHTS_SERVER + "/lights/state/").json()["state"]
            if state == "OFF":
                requests.post(PI_LIGHTS_SERVER + "/lights/fill/", json=CONFIG)
            present_count = 0
            print("ON")
        if absent_count > 5:
            absent_count = 0
            requests.get(PI_LIGHTS_SERVER + "/lights/off/")
            print("OFF")
finally:
    connection.close()
    server_socket.close()
