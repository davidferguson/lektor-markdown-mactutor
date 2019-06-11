# -*- coding: utf-8 -*-

import re
import mistune


name = 'gl_link'
type = 'inline'
position = 0
regex = re.compile(r'\[glossary\s*(?:=\s*(?P<glossary>\w+)\s*)?](?P<text>.*?)\[\/glossary\]')


def render(match):
    glossary = match.group('glossary')
    text = match.group('text')
    # special case if there is no explicit name specified, in which case we
    # have to derive it ourselves
    if glossary == None:
        glossary = text.strip()
    # format the appropriate link structure
    return '<a href="/Glossary/%s.html" data-glossary="%s" onclick="glossary_popup(this)">%s</a>' % (glossary,glossary,text)
