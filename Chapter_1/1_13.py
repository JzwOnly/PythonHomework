#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	type()。内置函数type()返回一个类型对象，如下所示，该对象将表示为一个Pythonic类型的字符串。
	>>> type(0)
	<type 'int'>
	>>> type(.34)
	<type 'float'>
	>>> type(dir)
	<type 'builtin_function_or_method'>
	创建一个能够从字符串中提取实际类型名称的正则表达式。函数将对类似于<type 'int'>的字符串返回int(其他类型也是如此，如'float'、'builtin_function_or_method'等)。
	注意：你所实现的值将存入类和一些内置类型的__name__属性中
'''
import re

def checkType(obj):
	typeStr = str(type(obj))
	print(typeStr)
	patt = r'^<class\s\'(\w+(_\w+)?)\'>$'
	m = re.match(patt, typeStr)
	if m is not None: return m.group(1)
# result = checkType('1')
 result = checkType(1)
# result = checkType(dir)
print(result)