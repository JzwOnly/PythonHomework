#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime


tlds = ('com', 'edu', 'net', 'org', 'gov')
def pushData():
	datas = []
	for i in range(randrange(5,11)):
		dtint = randrange(maxsize/1000)
		dtstr = ctime(dtint)
		llen = randrange(4,8)
		dlen = randrange(llen, 13)
		login = ''.join(choice(lc) for j in range(dlen))
		dom = ''.join(choice(lc) for j in range(dlen))
		data = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
		datas.append(data)
		print(data)
	return datas
