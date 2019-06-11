# -*- coding: utf-8 -*-

import re
import mistune


name = 'm_link'
type = 'inline'
position = 0
regex = re.compile(r'\[m\s*(?:=\s*(?P<name>\w+)\s*)?](?P<text>.*?)\[\/m\]')


def render(match):
    name = match.group('name')
    text = match.group('text')
    # special case if there is no explicit name specified, in which case we
    # have to derive it ourselves
    if name == None:
        name = text.split()[-1]
        # and remove all accents from it.
        name = purge(name)
    # format the appropriate link structure
    return '<a href="/Mathematicians/%s.html" data-name="%s" onclick="m_popup(this)">%s</a>' % (name,name,text)


def purge(s):
    # The below code is modified from the original htmlformat function
    # to ensure compatibility
    rawch   = ['á','à','â','ä','ã','Á','Â','Ä','é','è','ê','ë','É','î','í','ó','ô','ö','ò','õ','Ö','û','ú','ü','ù','Ü','ç','ï','ø','Ø','ñ']
    transch = ['a','a','a','a','a','A','A','A','e','e','e','e','E','i','i','o','o','o','o','o','O','u','u','u','u','U','c','i','o','O','n']
    for idx, raw in enumerate(rawch):
        s = s.replace(raw, transch[idx])
    return s
