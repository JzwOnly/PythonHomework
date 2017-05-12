#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	匹配所有有效Python标识符集合
'''

import re

patt = r'^[A-Za-z_]\w+'
#data = 'NSString'
data = 'data'
m = re.match(patt, data)
if m is not None: print(m.group())