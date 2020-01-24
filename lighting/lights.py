try:
    import neopixel
    import board
except (ImportError, RuntimeError) as e:
    print("Could not import Neopixel libraries! Make sure that you are running as sudo and that the libraries are installed.")
    exit()

from . import colors
from .colors import hex_to_rgb, scale, OFF
import time


class Lights:
    def __init__(self, length, pin=board.D18, color_format=neopixel.GRB, auto_write=False):
        self.pin = pin
        self.length = length
        self.pixels = neopixel.NeoPixel(pin, length, pixel_order=color_format, auto_write=auto_write)
        self.state = 'OFF'

    def _fill_with_color(self, color, _range=None, _scale=1):
        print(_range)
        if not _range:
            _range = (0, self.length)
        for i in range(*_range):
            self.pixels[i] = scale(color, _scale)
        self.pixels.show()
        self.state = 'ON'

    def _fill_with_colorset(self, colorset, _range=None, _scale=1):
        if not _range:
            for i in range(self.length):
                self.pixels[i] = scale(colorset[i % len(colorset)], _scale)
        for i in range(*_range):
            self.pixels[i] = scale(colorset[i % len(colorset)], _scale)
        self.pixels.show()
        self.state = 'ON'

    def clear(self):
        for i in range(self.length):
            self.pixels[i] = colors.OFF
        self.pixels.show()
        self.state = 'OFF'

    def fill(self, color_or_colorset, _range=None, _scale=1):
        if isinstance(color_or_colorset, tuple):
            self._fill_with_color(color_or_colorset, _range=_range, _scale=_scale)
        elif isinstance(color_or_colorset, list):
            self._fill_with_colorset(color_or_colorset, _range=_range, _scale=_scale)
        elif isinstance(color_or_colorset, str):
            print(color_or_colorset)
            color = hex_to_rgb(color_or_colorset)
            self._fill_with_color(color, _range, _scale=_scale)

    def blink(self, color_or_colorset, duration=-1):
        if duration != -1:
            for i in range(duration):
                self.fill(color_or_colorset)
                time.sleep(0.5)
                self.clear()
                time.sleep(0.5)
        else:
            while True:
                self.fill(color_or_colorset)
                time.sleep(0.5)
                self.clear()
                time.sleep(0.5)

    def transition(self, color1, color2, transition_time=2, steps_per_second=10):
        # TODO Fix this function.
        steps = steps_per_second * transition_time
        color_step = tuple((color1[i])/ (steps*2) for i in range(3))
        color = color1
        for _ in range(steps // 2):
            self.fill(color)
            time.sleep(1/steps_per_second)
            color = tuple(int(color[i] - color_step[i]) for i in range(3))
        color_step = tuple((color2[i])/ (steps*2) for i in range(3))
        for _ in range(steps // 2):
            self.fill(color)
            time.sleep(1/steps_per_second)
            color = tuple(int(color[i] + color_step[i]) for i in range(3))

    def breathe(self, color):
        self.transition(color, color)

    def runner(self, color):
        for i in range(self.length):
            self.pixels[i] = color
            if i != 0:
                self.pixels[i - 1] = colors.OFF
            self.pixels.show()
            time.sleep(0.1)

