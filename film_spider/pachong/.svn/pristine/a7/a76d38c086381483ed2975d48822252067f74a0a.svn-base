#-*- coding:utf-8-*-
import urllib
import requests
from bs4 import BeautifulSoup
import re
from HTMLParser import HTMLParser
#获取所要爬取的url地址
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html_doc = getHtml("http://www.bd-film.com/gq/index.htm")
print html_doc
soup = BeautifulSoup(html_doc,'html.parser', from_encoding ='utf-8')  
links = soup.find_all('a')
print soup.title.string
print soup.p.string
print 'links len:',len(links)
for link in links:
    print link.string













































