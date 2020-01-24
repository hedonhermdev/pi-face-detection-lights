import lights, colors
import time

strip = lights.Lights(10)

while True:
    strip.fill(colors.Colors.RED)
    time.sleep(2)
    strip.fill(colors.ColorSets.RGB)
    time.sleep(2)
    strip.fill("#ffffff")
    time.sleep(2)

while True:
    strip.breathe(colors.Colors.WHITE)
