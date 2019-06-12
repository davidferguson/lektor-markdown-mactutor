# -*- coding: utf-8 -*-

import re
import mistune


name = 'color_text'
type = 'inline'
position = 0
regex = re.compile(r'\[colou?r\s*(?:=\s*(?P<color>\w+)\s*)?](?P<text>.*?)\[\/colou?r\]')


def render(match):
    color = match.group('color')
    text = match.group('text')
    return '<span style="color: %s;">%s</span>' % (color,text)
