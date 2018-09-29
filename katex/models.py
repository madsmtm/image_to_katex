# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr

from colour import Color
from .core import ImageToKatex


@attr.s(slots=True)
class ImageToKatexFacebook(ImageToKatex):
    background = attr.ib(Color("#f1f0f0"), type=Color)
    max_length = attr.ib(20000, type=int)
    fontsize = attr.ib(14, type=float)
    max_size = attr.ib(50, type=int)
