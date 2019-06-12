# -*- coding: utf-8 -*-

import re
import mistune


name = 'center_text'
type = 'inline'
position = 0
regex = re.compile(r'\[(?:center|centre)\](?P<text>.+?)\[\/(?:center|centre)\]')


def render(match):
    text = match.group('text')
    return '<div style="text-align: center;">%s</div>' % text
