# NeoPixels with Face Detection
Basically stuck a strip of lights on the wall behind my workspace and used some face detection to switch them on when I sit on the chair.

![Image](image.jpg?raw=true "Image")
# Components (Hardware)
1. Raspberry Pi
2. NeoPixels (or any other WS2812 lights)
3. Raspberry Pi Camera module.
4. Linux/Mac host
Note: The Pi and the host computer must be on the same network. 

# Setting Up
Setting up is a pain. Will update this section with (hopefully) helpful images soon.

# Working
![Diagram](diagram.png?raw=true "Diagram")
1. Establish a TCP/IP connection between Pi and Mac.
2. Host a flask server on Pi.
3. Camera captures continuously and sends image as bytestream to Mac 
4. Process image on Mac.
5. If face detected, send POST request on Flask endpoint to switch on lights. Otherwise if face not detected in 10 successive frames, send POST request on Flask endpoint to switch off lights.

# Lighting
The lighting code is completely independent of the project and can be used as a part of any other project. It contains a bunch of effects you can use on any WS2812 lights (not necessarily NeoPixels)
Example Use:
```
import time

from lighting.lights import Lights
from lighting.colors import Colors, ColorSets

# Initialize lights
l = Lights(50)

# Fill a strip with a color
l.fill('#ff0000') # Using hex code
l.fill(Colors.RED) # Using the Colors object.
l.fill(Colors['RED']) # Using the Colors object as a dictionary.

# Fill a strip with a colorset.
l.fill(ColorSets.VIBGYOR)
```

# Face Detection
The face detection server uses an [https://github.com/ipazc/mtcnn](MTCNN) model to detect faces in the image sent by the Pi (client). If a face is detected in 5 subsequent frames, then it sends a request to the Lighting Server. Else if a face is not detected in 5 subsequent frames, then it sends a request to switch off the lights.
# Lighting Server
The lighting server can be used in combination with the lighting module to build a portal for controlling the lights(?). That is what I am going to work on next, btw.
Example requests on the lighting server:

1. To fill the lights
```
$ curl --location --request POST 'tirthraspberrypi.local:5000/lights/fill/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"color": "#00cfef",
	"range": [70, 230],
	"scale": 0.5
}'

```

2. To switch off the lights
```
$ curl --location --request GET 'tirthraspberrypi.local:5000/lights/fill/'
```

# The Rest
Other than the parts mentioned above, a lot of the code isnt really reusable right now as it is heavily dependent on my current setup, but you can take inspiration from it to build your own. That being said, I am working on making it as modular and reusable as possible. 
