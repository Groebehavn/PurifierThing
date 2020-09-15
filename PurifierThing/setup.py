import setuptools
import sys

if sys.version_info < (3,4):
    sys.exit("Python 3.4 or newer is required.")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="purifier-thing",
    version="0.1.0",
    author="Tamas Pepo",
    author_email="pepo.tamas@gmail.com",
    description="Mozilla IoT Thing for controlling Philips air purifiers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Groebehavn/PurifierThing",
    packages=['mozilla_thing'],
    install_requires=[
        'py-air-control>=2.1.0',
        'webthing>=0.13.2'
        ],
    entry_points={
        'console_scripts': [
            'purifier=purifierthing:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)