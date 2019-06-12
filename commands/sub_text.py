# -*- coding: utf-8 -*-

import re
import mistune


name = 'sub_text'
type = 'inline'
position = 0
regex = re.compile(r'\[sub\](?P<text>.+?)\[\/sub\]')


def render(match):
    text = match.group('text')
    return '<sub>%s</sub>' % text
