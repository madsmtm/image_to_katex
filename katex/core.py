# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, division

import attr

from colour import Color

from .utils import group_nested, image_colors, get_rgb_image, resize_image


@attr.s(slots=True)
class ImageToKatex(object):
    background = attr.ib(type=Color)
    max_length = attr.ib(type=int)
    fontsize = attr.ib(type=float)
    precision = attr.ib(5, type=float)
    transparency = attr.ib(True, type=bool)
    _pixelsize = attr.ib(None, type=float)
    _katex_multiplier = attr.ib(1.21, type=float)
    _unit_multiplier = attr.ib(0.1, type=float)

    formatters = dict(
        cell="\\color{{{}}}\\rule{}pt{}pt".format,
        columns="".join,
        rows_spacer="\\\\[-{}pt]".format,
        table="\\(\\begin{{aligned}}{}\\end{{aligned}}\\)".format,
    )

    @property
    def pixelsize(self):
        if self._pixelsize is None:
            self._pixelsize = 1 / (
                self.fontsize * self._katex_multiplier * self._unit_multiplier
            )
        return self._pixelsize

    @pixelsize.setter
    def pixelsize(self, value):
        self._pixelsize = value

    def in_background(self, color):
        # TODO: Make this work for colors close to the background color
        if not self.transparency:
            return False
        return color == self.background

    def get_float_value(self, number):
        return str(float(round(number, self.precision))).strip("0").rstrip(".")

    def _row(self, row, height):
        formatted_height = self.get_float_value(height)
        for pixel, equal_pixels in row:
            width = self.pixelsize * equal_pixels
            if self.in_background(pixel):
                color = "transparent"
            else:
                color = pixel.hex
            while width > 0:
                formatted_width = self.get_float_value(min(width, self.max_size))
                yield self.formatters["cell"](color, formatted_width, formatted_height)
                width -= self.max_size

    def _rows(self, rows):
        for row, equal_rows in rows:
            height = self.pixelsize * equal_rows
            while height > 0:
                row_data = self._row(row, min(height, self.max_size))
                yield self.formatters["columns"](row_data)
                height -= self.max_size

    def get(self, image):
        spacing = self.get_float_value(15 - min(self.pixelsize, 8.4))
        spacer = self.formatters["rows_spacer"](spacing)

        rows = self._rows(group_nested(image_colors(image)))

        return self.formatters["table"](spacer.join(rows))

    def get_katex(self, fp, size, resample=None):
        image = get_rgb_image(fp, self.background)
        im = resize_image(image, size, resample=resample)
        return self.get(im)

    def get_largest_latex(self, fp, resample=None):
        old, new = "", ""
        size = 0
        image = get_rgb_image(fp, self.background)
        while len(new) < self.max_length:
            old = new
            size += 1
            im = resize_image(image, size, resample=resample)
            new = self.get(new_im)
        return old, size
