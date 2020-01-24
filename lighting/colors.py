# Colors

OFF = (0,0,0)

def hex_to_rgb(hex_string):
    _hex = hex_string.lstrip("#")
    return tuple(int(_hex[i : i + 2], 16) for i in (0, 2, 4))


def scale(color, factor):
    return tuple(int(c * factor) for c in color)


class _Colors:
    OFF = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    VIOLET = (148, 0, 211)
    INDIGO = (75, 0, 130)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 127, 0)
    PURPLE = (128, 0, 128)

    def __setitem__(self, color_name, value):
        self.color_name = list_of_colors

    def __getitem__(self, color_name):
        return getattr(self, color_name)


class _ColorSets:
    VIBGYOR = [
        _Colors.VIOLET,
        _Colors.INDIGO,
        _Colors.BLUE,
        _Colors.GREEN,
        _Colors.YELLOW,
        _Colors.ORANGE,
        _Colors.RED,
    ]
    ROYGBIV = reversed(VIBGYOR)
    RGB = [_Colors.RED, _Colors.GREEN, _Colors.BLUE]
    OWG = [_Colors.ORANGE, _Colors.WHITE, _Colors.GREEN]
    RGBWYP = [
        _Colors.RED,
        _Colors.GREEN,
        _Colors.BLUE,
        _Colors.WHITE,
        _Colors.YELLOW,
        _Colors.PURPLE,
    ]

    def __setitem__(self, colorset_name, list_of_colors):
        self.colorset_name = list_of_colors

    def __getitem__(self, colorset_name):
        return getattr(self, color_name)


Colors = _Colors()
ColorSets = _ColorSets()

