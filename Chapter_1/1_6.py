#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	匹配以“www”起始且以“.com”结尾的简单Web域名；
	例如，http://www.yahoo.com/。
	选做题：你的正则表达式也可以支持其他高级域名，如.edu、.net等（例如，http://www.foothill.edu）
'''

import re

patt = r'https?://www\.\w+\.(com|net|edu)'
# data = 'http://www.yahoo.com'
data = 'https://www.foothill.edu'
m = re.match(patt, data)
if m is not None: print(m.group())