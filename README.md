# pi-face-detection-lights
Basically stuck a strip of lights on the wall behind my workspace and used some face detection to switch them on when I sit on the chair.
# Components (Hardware)
1. Raspberry Pi
2. NeoPixels (or any other WS2812 lights)
3. Raspberry Pi Camera module.
4. Linux/Mac host
Note: The Pi and the host computer must be on the same network. 

# Setting Up
Setting up is a pain. Will update this section with (hopefully) helpful images soon.  

# Working
1. Establish a TCP/IP connection between Pi and Mac.
2. Host a flask server on Pi.
3. Camera captures continuously and sends image as bytestream to Mac 
4. Process image on Mac.
5. If face detected, send POST request on Flask endpoint to switch on lights. Otherwise if face not detected in 10 successive frames, send POST request on Flask endpoint to switch off lights.

# Lighting
The lighting code is completely independent of the project and can be used as a part of any other project. It contains a bunch of effects you can use on any WS2812 lights (not necessarily NeoPixels)

# Lighting Server
The lighting server can be used in combination with the lighting module to build a portal for controlling the lights(?). That is what I am going to work on next, btw.

# The Rest
Other than the parts mentioned above, the code isnt really reusable right now as it is heavily dependent on my current setup, but you can take inspiration from it to build your own. That being said, I am working on making it as modular and reusable as possible. 

# Note
This can probably be done without both the socket and the webserver part but the above code was written after frustrating failed attempts to install OpenCV on my Raspberry Pi.
