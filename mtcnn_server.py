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

import config as cf


server_socket = socket.socket()
server_socket.bind((cf.HOST_IP, cf.HOST_PORT)) server_socket.listen(0) connection = server_socket.accept()[0].makefile("rb")

MTCNN = mtcnn.MTCNN()


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
        # Convert the bytestream to an np array.
        image_array = np.array(image)
        # Use MTCNN to detect faces in the image_array
        detection = MTCNN.detect_faces(image_array)
        if len(detection) != 0:
            if detection[0]['confidence'] > cf.PREDICTION_THRESHOLD:
                print("PRESENT")
                present_count += 1
                absent_count = 0
            else:
                print("ABSENT")
                absent_count += 1
                present_count = 0
        else:
            print("ABSENT")
            absent_count += 1
            present_count = 0
        if present_count == 5:
            print("LIGHTS ON")
            requests.post(cf.PI_LIGHTS_SERVER + "/lights/fill/", json=cf.REQUEST_BODY)
            present_count = 0
            absent_count = 0
        if absent_count == 5:
            print("LIGHTS OFF")
            requests.get(cf.PI_LIGHTS_SERVER + "/lights/off/")
            present_count = 0
            absent_count = 0

finally:
    connection.close()
    server_socket.close()
