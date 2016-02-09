![](http://drops.kylefox.ca/114za+)

# Placeholder Pics

Easily generate placeholder pictures for your users.

It's really good at rendering one or two letters inside a colored square, and terrible at everything else.

# Install

If you guessed pip, you are totally correct!

`pip install placeholder-pics`

# Basic Use

```python
from placeholder_pics import PlaceholderPic

placeholder = PlaceholderPic('KF')
placeholder.image.save('KF.png')
```

The `image` property is an instance of [`PIL.Image.Image`](http://pillow.readthedocs.org/en/3.0.x/reference/Image.html#the-image-class). This means you can save it however you like, or even apply additional manipulations. You could rotate it, for example, which would be kind of silly. Don't do that!

# Parameters

The only required parameter to `Placeholder` is the text you want to render.

The following optional parameters are accepted.

| Parameter  | Default | Description |
| ------------- | ------------- | ------------- |
| `size` | `300` | Image dimensions (always square) |
| `foreground` | `"#ffffff"` | Text color (hex format, _with_ leading #) |
| `background` | `None` | Background color (hex format, _with_ leading #). If `None`, our algorithm (`random.choice`) will choose a nice [Material Design](https://www.google.com/design/spec/style/color.html#color-color-palette) color for you, no sweat. Pass `"random"` to generate a _totally_ random color. |
| `font_file` | `"SourceSansPro-Regular.ttf"` | File name of the font you'd like to use. [Source Sans Regular](https://www.google.com/fonts/specimen/Source+Sans+Pro) is included by default. See [`PIL.ImageFont`](http://pillow.readthedocs.org/en/3.0.x/reference/ImageFont.html) for more info on how fonts are loaded. |
| `font_size` | `None` | Font size, in points. If `None`, will default to `size/2`, which seems to be a decent proportion. |

# Are you SO mad because of bugs or missing features?!?!

![](https://camo.githubusercontent.com/df781f87da2f2db87b5cc3125d5459bc70812112/687474703a2f2f64726f70732e6b796c65666f782e63612f31637147502b)

Just kidding, you know what to do. [Submit an issue.](https://github.com/kylefox/placeholder-pics/issues)

# Font Credits

[Source Sans Pro](https://www.google.com/fonts/specimen/Source+Sans+Pro) was designed by [Paul D. Hunt](https://plus.google.com/108888178732927400671/about) and is distributed under the [SIL Open Font License, 1.1.](http://scripts.sil.org/OFL)

# License (MIT)

Placeholder Pics is distributed under the MIT License.
Learn more at http://opensource.org/licenses/mit-license.php

Copyright (c) 2016 Kyle Fox

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
