# -*- coding: utf-8 -*-

import re
import mistune


name = 'sup_text'
type = 'inline'
position = 0
regex = re.compile(r'\[sup\](?P<text>.+?)\[\/sup\]')


def render(match):
    text = match.group('text')
    return '<sup>%s</sup>' % text
