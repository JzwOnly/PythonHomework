#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	根据读者当地格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数量的街道单词，包括类型名称）。
	例如，美国街道地址使用如下格式：1180 Bordeaux Drive。
	使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De la Cruz Boulevard。

'''

import re

patt = r'\d+(\s[A-Za-z]+)*'
# data = '1180 Bordeaux Drive'
data = '3120 De la Cruz Boulevard'
m = re.match(patt, data)
if m is not None: print(m.group())