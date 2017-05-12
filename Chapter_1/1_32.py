#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	亚马逊爬虫脚本。创建一个脚本，帮助你追踪你最喜欢的书，以及这些书在亚马逊上的表现（或者能够追踪图书排名的任何其他的在线书店）。
	例如，亚马逊对于任何一本图书提供以下链接：http://amazon.com/dp/ISBN(例如，http://amazon.com/dp/0132678209)。
	读者可以改变域名，检查亚马逊在其他国家的站点上相同的图书排名，例如BeautifulSoup、lxml或者html5lib来解析排名，
	然后让用户传入命令行参数，指明输出是否应当在一个纯文本中，也许包含在一个电子邮件正文中，还是用于Web的格式化HTML中。
'''

'''
	注意这里的header需要定期更换，亚马逊会给无账号访客一个id，这个id是会过期的，cookies中带了过期验证，
	所以需要用浏览器登录网站，获取Request Headers 替换掉下面的。 
'''
import re
import lxml.etree
from urllib import request
import ssl
from io import BytesIO
import gzip


def ungzip(data):
	from io import BytesIO
	import gzip
	byteBuffer = BytesIO(data)
	f = gzip.GzipFile(fileobj=byteBuffer)
	return str(f.read(),'utf-8')
def groupingForList(objList):
	listOne = []
	listTwo = []
	listThree = []
	returnList = [listOne,listTwo,listThree]
	index = -1
	for k in objList:
		if k == '图书':
			index+=1
		else:
			pass
		returnList[index].append(k)
	return returnList

def dealWithPath(zg_hrsr_ladder):
	rankList = []
	for path in zg_hrsr_ladder:
		patt = r'\[.*?\]'
		m = re.search(patt, str(path))
		result = re.sub(r'\[|\]', '', m.group())
		alist = result.split(',')
		astr = '->'.join(alist)
		rankList.append(astr)
	return rankList

def classified(zg_hrsr_rank, zg_hrsr_ladder, zg_hrsr_point):
	
	dicOne = {}
	dicTwo = {}
	dicThree = {}
	rankList = [dicOne,dicTwo,dicThree]
	index = 0
	cursor = 0
	for rank in zip(zg_hrsr_rank,zg_hrsr_ladder,zg_hrsr_point):
		patt = r'\'|\"|\[|\]'
		m = re.sub(patt, '', str(list(rank)))
		alist = m.split(',')
		for obj in alist:
			if index == 0:
				rankList[cursor]['rank'] = obj
			elif index == 1:
				rankList[cursor]['path'] = obj
			else:
				rankList[cursor]['result'] = obj
			index += 1
		index = 0
		cursor += 1
	return rankList
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://amazon.cn/dp/0132678209'
headers = {
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Cookie':'x-wl-uid=1nj41uTwkerBbfo12HqVYzJeCHD0vIvGGMClSUJjjP6gp6hEy24tPW6PPlkqnPXIO1EHJJeRx4FU=; session-token="xxkCtWF9lS11VN67rB3WLRVRjekkrSqJMjvHmE27S4qsWu2/ipUNbg5dG1ZJDMxf9HEVOk9br8N+eEO9cLOIdzTHwic6CPXKZl3k/C3HbOD3qqbXQMZpSH4gT5mlNBiQeJH/2MS9mgZChemeT+9nKAwfzbHbH4Y7byEvCuq5k87M0/cUkqz4LvGQUYbC73hwha84iIYVVmNzloinX+N3tGX7Y4Ry+yQUWoiy9sPnl6lzsM8InwneAg=="; ubid-acbcn=461-1436015-1375517; session-id-time=2082729601l; session-id=462-5769959-9488111; csm-hit=1CDTHFPZ11QZH61X4FGZ+s-RV4YNDZ04X8PEYY32520|1494574494409'
}
res = request.Request(url,headers=headers)
f = request.urlopen(res)
html = ungzip(f.read())
tree = lxml.etree.HTML(html)
totalRank = re.sub(r'\n| |\(', '', tree.xpath('//li[@id="SalesRank"]/text()')[1])
rankOne = []
rankTwo = []
rankThree = []
zg_hrsr_rank = tree.xpath('//ul[@class="zg_hrsr"]//span[@class="zg_hrsr_rank"]/text()')
zg_hrsr_ladder = groupingForList(tree.xpath('//ul[@class="zg_hrsr"]//span[@class="zg_hrsr_ladder"]/a/text()'))
zg_hrsr_point = tree.xpath('//ul[@class="zg_hrsr"]//span[@class="zg_hrsr_ladder"]/b/a/text()')
rankList = classified(zg_hrsr_rank, dealWithPath(zg_hrsr_ladder), zg_hrsr_point)
print(rankList)
