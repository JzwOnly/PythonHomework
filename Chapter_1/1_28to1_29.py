#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	处理电话号码。对于练习1_28和1_29，回顾1.2节介绍的正则表达式\d{3}-\d{3}-\d{4}，它匹配电话号码，但是允许可选的区号作为前缀。
	更新正则表达式，使它满足以下条件。
'''

import re

'''
	1_28 区号（三个整数集合中的第一部分和后面的连字符）是可选的，也就是说，正则表达式应当匹配800-555-1212，也能匹配555-1212
'''

patt = r'(\d{3}-)?\d{3}-\d{4}'
data = '800-555-1212'
#data = '555-1212'
m = re.match(patt, data)
if m is not None: print(m.group())


'''
	1_29 支持使用圆括号或者连字符连接的区号(更不用说是可选的内容);
	     使正则表达式匹配800-555-1212、555-1212以及(800) 555-1212
'''
patt = r'((\d{3}-)?|(\(\d{3}\)\s))?\d{3}-\d{4}'
data = '800-555-1212'
#data = '555-1212'
#data = '(800) 555-1212'
m = re.match(patt, data)
if m is not None: print(m.group())