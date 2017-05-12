#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	匹配由单个逗号和单个空白符分隔的任意单词和单个字母，如姓氏首字母
'''

import re

patt = r'\w+[, ]\w+'
data = 'J,Smith'
#data = 'J Smith'
m = re.match(patt, data)
if m is not None: print(m.group())