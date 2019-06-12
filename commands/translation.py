# -*- coding: utf-8 -*-

import re
import mistune


name = 'translation'
type = 'inline'
position = 0
regex = re.compile(r'\[t=(?P<translation>.+?)\]')


def render(match):
    translation = match.group('translation')
    # format the appropriate link structure
    return '<a href="/Translation/%s.html" data-translation="%s" onclick="translation_popup(this)">TRANSLATION</a>' % (translation,translation)
