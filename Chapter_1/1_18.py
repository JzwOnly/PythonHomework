#usr/bin/env python3
#-*- coding: utf-8 -*-
#

'''
	通过确认整数字段中的第一个整数匹配在每个输出行起始部分的时间戳，确保在redata.txt中没有数据损坏
'''

import re
from time import ctime
m = True
patt = r'([A-Za-z]{3}\s[A-Za-z]{3}\s+\d+\s\d{2}:\d{2}:\d{2}\s\d+)::.*?::(\d+)-[4-8]-\d'
with open('1_16.txt','r') as f:
	for data in f.readlines():
		m = re.search(patt, data)
		if ctime(int(m.group(2))) == m.group(1):
			pass
		else:
			m = False

		
