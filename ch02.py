from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
# nameList = set(bsObj.findAll("span", {"class":"green"}))
# for name in nameList:
#     print(name.get_text())


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(sibling)
# #############################################################
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
# #allText = bsObj.findAll(id="text")
# #print(allText[0].get_text())
# print(bsObj.text)

# ################################################################
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")

# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)