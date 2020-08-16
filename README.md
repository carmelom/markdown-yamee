# markdown-yamee
YAMEE: Yet Another Markdown Emoji Extension

Inspired by <https://bytefish.de/blog/markdown_emoji_extension/>, but powered by the [emoji](https://pypi.org/project/emoji/) Python package: no need for a .png folder / a json font file, and supports aliases.

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
    'extensions': [EmojiExtension.get_extension()],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
```

## Usage

Double semicolons

`Emojis on Pelican!! ::smile:: ::grinning_face:: Great! ::+1::`

Emojis on Pelican!! 😄 😀 Great! 👍
