#!/usr/bin/env python
import os
import random
import string
from placeholder_pics import PlaceholderPic


def _chars():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2))


if __name__ == '__main__':

    if not os.path.isdir('demo-images'):
        os.mkdir('demo-images')

    for idx, bg in enumerate(PlaceholderPic.BACKGROUNDS):
        p = PlaceholderPic(_chars(), background=bg, size=100)
        filename = '{}-{}.png'.format(idx, bg.replace('#', ''))

        p.image.save(os.path.join('demo-images', filename), format='PNG')
