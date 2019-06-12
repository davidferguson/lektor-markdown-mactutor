# -*- coding: utf-8 -*-

import re
import mistune


name = 'e_link'
type = 'inline'
position = 0
regex = re.compile(r'\[e\s*(?:=\s*(?P<extra>\w+)\s*)](?P<text>.*?)\[\/e\]')


def render(match):
    extra = match.group('extra')
    text = match.group('text')
    # format the appropriate link structure
    return '<a href="/Extras/%s.html" data-extra="%s" onclick="extra_popup(this)">%s</a>' % (extra,extra,text)
