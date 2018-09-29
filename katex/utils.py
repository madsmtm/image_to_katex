# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, division

from PIL import Image
from colour import Color


def color_to_int(color):
    return tuple(int(round(x * 255)) for x in color.get_rgb())


def color_from_int(ints):
    color = Color()
    color.set_rgb(tuple(x / 255 for x in ints))
    return color


def get_rgb_image(fp, background):
    raw = Image.open(fp).convert("RGBA")
    bg = Image.new(raw.mode, raw.size, color=color_to_int(background))
    return Image.alpha_composite(bg, raw).convert("RGB")


def resize_image(image, size, resample=None):
    if resample is None:
        resample = Image.NEAREST

    # Preserve aspect ratio
    ratio = min(size / image.width, size / image.height)
    height = int(round(image.height * ratio))
    width = int(round(image.width * ratio))

    return image.resize((height, width), resample=resample)


def image_colors(image):
    for y in range(image.height):
        # Not yield from, since we want the result as a generator
        yield (color_from_int(image.getpixel((x, y))) for x in range(image.width))


def group(iterable):
    """Groups items in an iterable

    Example:
        >>> list(group([1, 2, 2, 1, 1, 3]))
        [(1, 1), (2, 2), (1, 2), (3, 1)]
    """
    iterable = iter(iterable)
    amount_equal = 1
    prev = next(iterable)
    for item in iterable:
        if prev != item:
            yield prev, amount_equal
            amount_equal = 0
        amount_equal += 1
        prev = item
    yield prev, amount_equal


def group_nested(nested_iterable):
    """A nested version of `group`"""
    yield from group(map(tuple, map(group, nested_iterable)))
