#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created: 08-2020 - Carmelo Mordini <carmelo> <carmelo.mordini@unitn.it>

"""Module docstring

"""

import emoji
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern

EMOJI_RE = r'(::)(.*?)::'


class EmojiExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {}
        super(EmojiExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        pattern = EmojiInlinePattern(EMOJI_RE)
        md.inlinePatterns.add('emoji', pattern, '<not_strong')

    @staticmethod
    def get_extension():
        return EmojiExtension()


class EmojiInlinePattern(Pattern):

    def __init__(self, pattern):
        super(EmojiInlinePattern, self).__init__(pattern)

    def handleMatch(self, m):
        emoji_key = m.group(3)
        return emoji.emojize(f":{emoji_key}:", use_aliases=True)
