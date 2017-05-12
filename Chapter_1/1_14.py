#!usr/bin/env python3
# -*- coding:utf-8 -*-
#

'''
	处理日期，1.2节提供了来匹配单个或者两个数字字符串的正则表达式模式，来表示1~9的月份(0?[1~9])。
	创建一个正则表达式来表示标准日历中剩余三个月的数字。

'''
import re

patt = r'^(0?[[1-9]|1[0-2])$'
data = '11'
m = re.match(patt, data)
if m is not None: print(m.group())