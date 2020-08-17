#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created: 08-2020 - Carmelo Mordini <carmelo> <carmelo.mordini@unitn.it>

import emoji
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

EMOJI_RE = r'(::)(.*?)::'


class EmojiExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'span_class': [
                'emoji',
                'the class name of the encompassing `<span>` element (default: "emoji")'
                'if None, no element is created'
            ]
        }
        super(EmojiExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        pattern = EmojiInlinePattern(EMOJI_RE, self)
        md.inlinePatterns.add('emoji', pattern, '<not_strong')

    @staticmethod
    def get_extension(**kwargs):
        return EmojiExtension(**kwargs)


class EmojiInlinePattern(Pattern):

    def __init__(self, pattern, extension):
        super(EmojiInlinePattern, self).__init__(pattern)
        self.ext = extension

    def handleMatch(self, m):
        emoji_key = m.group(3)
        # get the Unicode symbol
        emoticon = emoji.emojize(f":{emoji_key}:", use_aliases=True)
        span_class = self.ext.getConfig('span_class')
        if span_class:
            # Apply style formatting
            element = etree.Element('span')
            element.text = emoticon
            element.set('class', span_class)
            return element
        else:
            return emoticon
