#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

import re

'''
	匹配所有能够表示python整数的字符串集
'''
# 1_7

patt = r'-?\d+'
data = '-10 ' 
m = re.match(patt, data)
if m is not None: print(m.group())


'''
	匹配所有能够表示python长整数的字符串集
'''

# 1_8
'''
	python3中已经把int 和 long 合并为 int了，所以python3中没有长整数之说
'''

'''
	匹配所有能够表示python浮点数的字符串集
'''

# 1_9
patt = r'-?\d+(\.\d+)?'
data = '20.333'
m = re.match(patt, data)
if m is not None: print(m.group())

'''
	匹配所有能够表示python复数的字符串集
'''
# 1_10
# 第一个匹配只有虚部的情况, 如果用第二个匹配这种情况就会出现-20被实部匹配
patt = r'(-?\d+(\.\d+)?[jJ])' or r'(-?\d+(\.\d+)?)?[+-]?(-?\d+(\.\d+)?[jJ])?'
#data = '1--20j'
data = '-20j'
#data = '-20'
m = re.match(patt, data)
if m is not None: print(m.group())