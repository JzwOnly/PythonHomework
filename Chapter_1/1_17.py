#usr/bin/env python3
#-*- coding: utf-8 -*-
#

'''
	判断在redata.txt中一周的每一天出现的次数(换句话说，读者也可以计算所选择的年份中每个月中出现的次数)
'''
import re
patt = 'Sat'
time = 0
with open('1_16.txt','r') as f:
	for data in f.readlines():
		m = re.findall(patt, data)
		time = time + len(m)
