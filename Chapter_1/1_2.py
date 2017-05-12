#!usr/bin/env python3
# -*- coding:utf-8 -*-
#

'''
	匹配由单个空格分隔的任意单词对，也就是姓和名
'''

import re

patt = r'\w+\s\w+'
m = re.match(patt, 'Guido van')
if m is not None:print(m.group())