#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

import re

with open('1_16.txt','r') as f:
	for data in f.readlines():

		'''
			1_19 提取每行中完整的时间戳
		'''
		m = re.search(r'[A-Za-z]{3}\s[A-Za-z]{3}\s+\d+\s\d{2}:\d{2}:\d{2}\s\d+',data)

		'''
			1_20 提取每行中完整的电子邮件地址
		'''
		m = re.search(r'[A-Za-z]+@[A-Za-z]+\.(com|edu|org|net|gov)', data)

		'''
			1_21 仅仅提取时间戳中的月份
		'''
		m = re.search(r'[A-Za-z]{3}\s([A-Za-z]{3})\s+\d+\s\d{2}:\d{2}:\d{2}\s\d+',data).group(1)
	
		'''
			1_22 仅仅提取时间戳中的年份
		'''
		m = re.search(r'[A-Za-z]{3}\s[A-Za-z]{3}\s+\d+\s\d{2}:\d{2}:\d{2}\s(\d+)',data).group(1)

		'''
			1_23 仅仅提取时间戳中的时间
		'''
		m = re.search(r'[A-Za-z]{3}\s[A-Za-z]{3}\s+\d+\s(\d{2}:\d{2}:\d{2})\s\d+', data).group(1)

		'''
			1_24 仅仅从电子邮件地址中提取登录名和域名(包括主域名和高级域名一起提取)
		'''
		m = re.search(r'([A-Za-z]+)@([A-Za-z]+)\.(com|edu|org|net|gov)', data).groups()

		'''
			汗和前面一题是一样的，不知道是翻译问题还是原文就这样
			1_25 仅仅从电子邮件地址中提取登录名和域名(包括主域名和高级域名)
		'''

		'''
			1_26 使用你的电子邮件地址替换每一行数据中的电子邮件地址
		'''
		m = re.sub(r'[A-Za-z]+@[A-Za-z]+\.(com|edu|org|net|gov)', '836579250@qq.com', data)

		'''
			1_27 从时间戳中提取月、日和年，然后以“月，日，年”的格式，每一行仅仅迭代一次
		'''
		m = re.search(r'\b([A-Za-z]{3})\s+(\d+) .{8} (\d+)::',data).groups()
