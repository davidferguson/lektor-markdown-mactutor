# -*- coding: utf-8 -*-

import re
import mistune


name = 'text'
type = 'inline'
regex = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~\$]|https?://| {2,}\n|$)')
