import random
from PIL import Image, ImageFont, ImageDraw


class PlaceholderPic(object):

    DEFAULTS = {
        'size': 300,
        'foreground': '#ffffff',
        'background': None,
        'font_file': 'SourceSansPro-Regular.ttf',
        'font_size': None,
    }

    BACKGROUNDS = [
        '#f34235',  # Red
        '#e81d62',  # Pink
        '#9b26af',  # Purple
        '#6639b6',  # Deep purple
        '#363f45',  # Slate
        '#3e50b4',  # Indigo
        '#2095f2',  # Blue
        '#009587',  # Teal
        '#8ac249',  # light green
        '#fe9700',  # Orange
        '#fe5621',  # Deep orange
        '#785447',  # Brown
        '#5f7c8a',  # Blue Grey
    ]

    def __init__(self, text, **kwargs):
        self.text = text
        options = PlaceholderPic.DEFAULTS.copy()
        options.update(**kwargs)
        if options['background'] is None:
            options['background'] = random.choice(PlaceholderPic.BACKGROUNDS)
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
