# -*- coding: utf-8 -*-

import re
import mistune


name = 'ac_link'
type = 'inline'
position = 0
regex = re.compile(r'\[ac\s*(?:=\s*(?P<academy>\w+)\s*)](?P<text>.*?)\[\/ac\]')


def render(match):
    academy = match.group('academy')
    text = match.group('text')
    # format the appropriate link structure
    return '<a href="/Academy/%s.html" data-academy="%s" onclick="academy_popup(this)">%s</a>' % (academy,academy,text)
