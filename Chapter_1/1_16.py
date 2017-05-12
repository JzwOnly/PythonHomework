#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	基于gendata.py的数据
	为gendata.py更新代码，使数据直接输出到redata.txt而不是屏幕
'''
import gendata
with open('1_16.txt','a') as f:
	for data in gendata.pushData():
		f.writelines(data+'\r\n')