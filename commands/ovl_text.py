# -*- coding: utf-8 -*-

import re
import mistune


name = 'ovl_text'
type = 'inline'
position = 0
regex = re.compile(r'\[ovl\](?P<text>.+?)\[\/ovl\]')


def render(match):
    text = match.group('text')
    return '<span style="text-decoration: overline;">%s</span>' % text
