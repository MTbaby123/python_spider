# -*- coding:utf-8 -*-
import bs4
import urllib
from bs4 import BeautifulSoup
import urllib2
import requests
from itertools import permutations


# 网址:http://www.66ip.cn/index.html
#这里看出每一页的网址由index下标表示，即index是几就代表第几页


#我这里只爬取五个,你随意啊
def main():
    #先定义一个空列表，用于存放爬取到的ip
    iplist = []
    for i in range(1,5):
        #构造url
        s = ".html"
        url = "http://www.66ip.cn/"
        
        #调用网页请求函数
        cur_url = url + str(i) + s
        html_doc = gethtml(cur_url)
        
        # 重复是因为这里重复读取本地文件内容
        #html_doc = gethtml_fromfile()
        
        #使用beautifulsoup来解析网页
        sp = bs4.BeautifulSoup(html_doc,'html.parser',from_encoding="utf-8")
        trs = sp.find_all("tr")
        
        for tr in trs:
            # tr是每一行
            for i,e in enumerate(tr.children):
                # unicode转成utf-8字符串
                #ip_val = a.string.encode('utf-8').strip()
                #调用判断有效ip函数
                if i == 0:
                    if not is_invalid_ip4(e):
                        continue
#                         iplist.append(ip_val)
                    IP = e
                elif i == 1:
                    port = e
                break
            print "%s:%s"%(IP,port)

                    #这里发现ip在tr的第一列，所以我们每次取到第一个数据后跳出
        print '-'*32#我是分隔符
            
def is_invalid_ip4(ip):
    ip = ip.strip()
    # ip4格式：a.b.c.d
    its = [v for v in ip.split('.')]
    
    # .分数不对
    if len(its) != 4:
        return False
    
    # 值不是数字
    for v in its:
        if not v.isdigit():
            return False
    
    return True
            
def gethtml_fromfile():
    tx = ''
    with open(r'F:\eclipse-cpp-workspace\LearnPython\html_agent.html','rb') as fd:
        tx = fd.read()
    return tx

#构造网页请求函数
def gethtml(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers = {"User-Agent":user_agent}
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

if __name__ == "__main__":
    main()
























