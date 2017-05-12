#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	匹配所有能够表示有效电子邮件地址的集合（从一个宽松的正则表达式开始，然后尝试使它尽可能的严谨，不过要保持正确的功能）。
'''

import re

patt = r'\w+(\.\w+)*@\w+\.(com|cn|net)$'
#data = '836579250@qq.com'
data = 'bill.gates@microsoft.net'
m = re.match(patt, data)
if m is not None: print(m.group())