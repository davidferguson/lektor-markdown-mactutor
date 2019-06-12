# -*- coding: utf-8 -*-

import re
import mistune


name = 'bgcolor_text'
type = 'inline'
position = 0
regex = re.compile(r'\[bgcolou?r\s*(?:=\s*(?P<color>\w+)\s*)?](?P<text>.*?)\[\/bgcolou?r\]')


def render(match):
    color = match.group('color')
    text = match.group('text')
    return '<span style="background-color: %s;">%s</span>' % (color,text)
