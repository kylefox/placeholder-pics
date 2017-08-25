from setuptools import setup

setup(
    name='placeholder-pics',
    version='1.0.3',
    description="Easily generate placeholder pictures for your users.",
    url="https://github.com/kylefox/placeholder-pics",
    author="Kyle Fox",
    author_email="kylefox@gmail.com",
    license="MIT",
    packages=['placeholder_pics'],
    package_data={
        'placeholder_pics': ['SourceSansPro-Regular.ttf'],
    },
    install_requires=['Pillow'],
    zip_safe=False,
)
