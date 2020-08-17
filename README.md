# markdown-yamee
YAMEE: Yet Another Markdown Emoji Extension

Inspired by <https://bytefish.de/blog/markdown_emoji_extension/>, but powered by the [emoji](https://pypi.org/project/emoji/) Python package: no need for a .png folder / a json font file, and supports aliases.

Another stolen idea form <https://github.com/kernc/mdx_unimoji>: wrap the unicode charachter in a suitable html element to use an Emoji font.

## Install
Install (I'm not on PyPI yet)

```
pip install git+https://github.com/carmelom/markdown-yamee.git
```

Configure Pelican
```python
# pelicanconf.py
from yamee import EmojiExtension

MARKDOWN = {
    'extensions': [EmojiExtension.get_extension(span_class='emoji')],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
```

Use the `span_class` in your css like:
```css
.emoji {
    font-family: "Apple Color Emoji", "Segoe UI Emoji",
                 "Noto Color Emoji", EmojiSymbols, "DejaVu Sans", Symbola;
}
```

Make sure your font files are locally / globally installed and available. Some (Arch-oriented) source:

- Noto Color Emoji: <https://www.archlinux.org/packages/extra/any/noto-fonts-emoji/>
- Apple Color Emoji: <https://aur.archlinux.org/packages/ttf-apple-emoji/>

## Usage

Double semicolons

`Emojis on Pelican!! ::smile:: ::grinning_face:: Great! ::+1::`

Emojis on Pelican!! 😄 😀 Great! 👍
