# -*- coding: utf-8 -*-

import re
import mistune


name = 'reference'
type = 'inline'
position = 0
regex = re.compile(r'\[ref=(?P<reference>.\d?)\]')


def render(match):
    reference = match.group('reference')
    # format the appropriate link structure
    return '<a href="/Reference/%s.html" data-reference="%s" onclick="reference_popup(this)">REFERENCE</a>' % (reference,reference)
