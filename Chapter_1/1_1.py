#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	识别后续的字符串：“bat”、“bit”、“but”、“hat”、“hit”、“hut” 
'''

import re

patt = r'^(bat|bit|but|hat|hit|hut)'
m = re.match(patt, 'hat')
if m is not None: print(m.group())