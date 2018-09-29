# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import click

from colour import Color

from .core import ImageToKatex
from .models import ImageToKatexFacebook

CLASSES = {"facebook": ImageToKatexFacebook}


class ColorTypeBase(click.ParamType):
    name = "color"

    def convert(self, value, param, ctx):
        try:
            if not value.startswith("#"):
                value = "#{}".format(value)
            return Color(value)
        except Exception as e:
            self.fail("%s is not a valid color" % e)


ColorType = ColorTypeBase()


@click.command()
@click.argument("image", type=click.File(mode="rb"))
@click.option(
    "-s",
    "--size",
    default=16,
    type=int,
    help="The amount of pixels to use. The image will keep it's aspect ratio",
    show_default=True,
)
@click.option(
    "-t",
    "--type",
    "type_",
    default="facebook",
    type=click.Choice(tuple(CLASSES)),
    help="The engine to use. Currently this is only built for Facebook",
)
@click.option(
    "-ps",
    "--pixelsize",
    type=float,
    help="The size of a single pixel, in the unit `pt`. Can reduce output size if set",
    show_default="single pixel on the screen",
)
@click.option(
    "-f",
    "--fontsize",
    type=int,
    help="Facebook's font-size in pixels to take into account",
)
@click.option(
    "-b",
    "--background",
    type=ColorType,
    help="Background color of the image, in hexadecimal",
)
@click.option(
    "-r",
    "--resample",
    type=click.IntRange(min=0, max=3),
    help="Resampling level when resizing. Esentially means level of anti-aliasing",
)
@click.option(
    "-p",
    "--precision",
    type=int,
    help="How precise the pixel-sizes should be. Can reduce output size",
)
@click.pass_context
def cli(ctx, type_, image, size, resample=None, **kwargs):
    """Convert an image into KaTeX using \\rule"""
    kwargs = dict(filter(lambda item: item[1] is not None, kwargs.items()))
    image_to_katex = CLASSES[type_](**kwargs)

    if False:
        katex, size = image_to_katex.get_largest_latex(
            image, args.pixelsize, args.fontsize, args.precision, args.resample
        )
    else:
        katex = image_to_katex.get_katex(image, size, resample=resample)

    length = "{}/{}".format(len(katex), image_to_katex.max_length)
    if len(katex) > image_to_katex.max_length:
        ctx.fail("Length of resulting string too large: {}".format(length))

    click.echo(katex)
    click.echo("Total length of string: {}".format(length))
