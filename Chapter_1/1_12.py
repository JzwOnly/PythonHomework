#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	匹配所有能够表示有效的网站地址的集合（URL）(从一个宽松的正则表达式开始，然后尝试使它尽可能严谨，不过要保持正确的功能)
'''

import re

patt = r'https?://(w{3}|\w+)(\.\w+)+(\.(com|net|edu|cn)$)?'
# data = 'http://www.baidu.com'
# data = 'http://192.168.0.1'
data = 'https://interface.djlchina.com'
m = re.match(patt, data)
if m is not None: print(m.group())