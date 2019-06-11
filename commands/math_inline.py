# -*- coding: utf-8 -*-

import re
import mistune


name = 'mathjax_inline'
type = 'inline'
position = 1
regex = re.compile(r'\$(?P<math>.+?)\$')


def render(match):
    math = match.group('math')
    return 'MATH$%s$MATH' % math
