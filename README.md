# Python KaTeX
Contains functionality to convert an image into [KaTeX](https://github.com/Khan/KaTeX), using `\rule`s

Also currently only set up to work with Facebook Messengers KaTeX setup, but it should be simple to adapt for other applications.

More functionality is planned, and PRs welcome!


# Installation

```sh
$ # This will install the python package `katex`, along with the shell command
$ # `image_to_katex`
$ pip install katex
```

# Basic usage

```sh
$ # This will generate KaTeX output for that image, where the image is scaled
$ # down to 30 pixels, and where each pixel is 5 units wide
$ image_to_katex image.png -s 30 -ps 5
```

```sh
$ # Display help message
$ image_to_katex --help
```

# Facebook KaTeX info
Custom KaTeX version, above v0.8.2 (17/8-2017) but below v0.9.0. At least commit [211c86d](https://github.com/KaTeX/KaTeX/commit/211c86d39bcdc421149628f7b266891138cbdb1a).

Max length of Facebook messages is 20000 chars - though they've added an extra check to not execute KaTeX if the message is above 1000 chars, or the depth level is above 20. Probably parameters they can tune remotely.

Facebook renders any KaTeX error messages in the html `title` attribute (which means you can hover over to view it).

You can use `$$`, `\(`+`\)` or `\[`+`\]` as delimeters. `$$` or `\[`+`\]` renders the LaTeX in displayMode, `\(`+`\)` renders it inline.

Facebook wraps all inputs in a `\color` block, like this: `\color{#fff}{inp}`, where `inp` is the input

Known current KaTeX options:

- displayMode = true if using `$$` else false
- colorIsTextColor: default
- maxSize: 5
