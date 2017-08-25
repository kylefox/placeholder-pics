import pkg_resources
import random
from PIL import Image, ImageFont, ImageDraw


class PlaceholderPic(object):

    DEFAULT_FONT_FILE = pkg_resources.resource_filename(
        __name__, 'SourceSansPro-Regular.ttf')

    DEFAULTS = {
        'size': 300,
        'foreground': '#ffffff',
        'background': None,
        'font_file': DEFAULT_FONT_FILE,
        'font_size': None,
    }

    # https://www.google.com/design/spec/style/color.html#color-color-palette
    BACKGROUNDS = [
        '#F44336',  # Red
        '#E91E63',  # Pink
        '#9C27B0',  # Purple
        '#673AB7',  # Deep purple
        '#3F51B5',  # Indigo
        '#2196F3',  # Blue
        '#03A9F4',  # Light Blue
        '#00BCD4',  # Cyan
        '#009688',  # Teal
        '#4CAF50',  # Green
        '#8BC34A',  # Light Green
        '#CDDC39',  # Lime
        '#FFEB3B',  # Yellow
        '#FFC107',  # Amber
        '#FF9800',  # Orange
        '#FF5722',  # Deep Orange
        '#795548',  # Brown
        '#9E9E9E',  # Grey
        '#607D8B',  # Blue Grey
    ]

    @classmethod
    def random_color(self):
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def __init__(self, text, **kwargs):
        self.text = text
        options = PlaceholderPic.DEFAULTS.copy()
        options.update(**kwargs)
        if options['background'] is None:
            options['background'] = random.choice(PlaceholderPic.BACKGROUNDS)
        if options['background'].lower() == 'random':
            options['background'] = PlaceholderPic.random_color().upper()
        if options['font_size'] is None:
            options['font_size'] = int(options['size']/2)
        for key, value in options.items():
            setattr(self, key, value)
        self._image = None

    @property
    def image(self):
        if self._image is None:
            self._image = Image.new(
                mode='RGB',
                size=(self.size, self.size),
                color=self.background)
            draw = ImageDraw.Draw(self._image)
            font = ImageFont.truetype(font=self.font_file, size=self.font_size)
            text_width, text_height = draw.textsize(self.text, font=font)
            draw.text(
                (
                    (self.size-text_width)/2,
                    (self.size-text_height*1.275)/2,
                ),
                self.text,
                self.foreground,
                font=font)
        return self._image
