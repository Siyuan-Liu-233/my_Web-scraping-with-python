import urllib.request as ur
import time

from bs4 import BeautifulSoup
# header1={

# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400'
# }
# res = ur.Request("https://en.wikipedia.org/wiki/Kevin_Bacon",headers=header1)

# html=ur.urlopen(res)
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):		
# 	if 'href' in link.attrs:		#如果属性值有href xxx.attrs是个字典
# 		print(link.attrs['href'])

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
			href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)