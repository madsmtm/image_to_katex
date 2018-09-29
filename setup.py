# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from setuptools import setup
from os import path

# Read contents of the readme file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="katex",
    version="0.0.1", # Remember to update this in katex/__init__.py as well
    license="BSD 3-Clause",
    license_file="LICENSE",
    author="Mads Marquart",
    author_email="madsmtm@gmail.com",
    description="Convert an image into KaTeX to use in Facebook Messenger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Facebook KaTeX Messenger ",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications :: Chat",
        "Topic :: Games/Entertainment",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    url="http://github.com/madsmtm/katex",
    packages=["katex"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4.0",
    install_requires=["Pillow>=5.2.0", "attrs", "parse", "Click"],
    entry_points={"console_scripts": ["image_to_katex=katex.cli:image_to_katex"]},
)
