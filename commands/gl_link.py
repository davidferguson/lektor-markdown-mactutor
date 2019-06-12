# -*- coding: utf-8 -*-

import re
import mistune


name = 'gl_link'
type = 'inline'
position = 0
regex = re.compile(r'\[gl\s*(?:=\s*(?P<glossary>\w+)\s*)](?P<text>.*?)\[\/gl\]')


def render(match):
    glossary = match.group('glossary')
    text = match.group('text')
    # format the appropriate link structure
    return '<a href="/Glossary/%s.html" data-glossary="%s" onclick="glossary_popup(this)">%s</a>' % (glossary,glossary,text)
