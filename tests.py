import unittest

from placeholder_pics import PlaceholderPic


class TestDefaults(unittest.TestCase):

    def setUp(self):
        self.placeholder = PlaceholderPic('KF')

    def test_default_size(self):
        self.assertEqual(
            self.placeholder.size,
            PlaceholderPic.DEFAULTS['size'])

    def test_default_foreground(self):
        self.assertEqual(
            self.placeholder.foreground,
            PlaceholderPic.DEFAULTS['foreground'])

    def test_default_background(self):
        self.assertIn(
            self.placeholder.background,
            PlaceholderPic.BACKGROUNDS)

    def test_default_font_file(self):
        self.assertEqual(
            self.placeholder.font_file,
            PlaceholderPic.DEFAULTS['font_file'])

    def test_default_font_size(self):
        self.assertEqual(
            self.placeholder.font_size,
            self.placeholder.size/2)


class TestCustom(unittest.TestCase):

    def test_custom_size(self):
        self.assertEqual(
            PlaceholderPic('KF', size=50).size,
            50)

    def test_custom_foreground(self):
        self.assertEqual(
            PlaceholderPic('KF', foreground='#000000').foreground,
            '#000000')

    def test_custom_background(self):
        self.assertEqual(
            PlaceholderPic('KF', background='#000000').background,
            '#000000')

    def test_custom_font_file(self):
        self.assertEqual(
            PlaceholderPic('KF', font_file='Comic-Sans.ttf').font_file,
            'Comic-Sans.ttf')

    def test_custom_font_size(self):
        self.assertEqual(
            PlaceholderPic('KF', font_size=10).font_size,
            10)

    def test_random_background(self):
        self.assertRegexpMatches(
            PlaceholderPic('KF', background='random').background,
            r'#([0-9A-F]{6})')

        self.assertRegexpMatches(
            PlaceholderPic('KF', background='RANDOM').background,
            r'#([0-9A-F]{6})')
