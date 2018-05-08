#coding:utf-8
import urllib2
import random
import re
import socket



user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]

count = 0

def Get_proxy_ip(widx=1):                
    headers = {
            'Host': 'www.xicidaili.com',
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Accept': r'application/json, text/javascript, */*; q=0.01',
            'Referer': r'http://www.xicidaili.com/',
            }
    widx = 1
    while widx>0:
        try:
            widx += 1
            rurl = r'http://www.xicidaili.com/nn/%d'%(widx) 
            req = urllib2.Request(rurl, headers=headers)
            response = urllib2.urlopen(req)
            html = response.read().decode('utf-8')
            ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+',html)
            port_list = re.findall(r'<td>\d+</td>',html)
            for i in range(len(ip_list)):
                ip = ip_list[i]
                port = re.sub(r'<td>|</td>', '', port_list[i])
                proxy = '%s:%s' %(ip,port)
                if not Connect(ip, port):
                    print 'try hard for request a new available agent...'
                    continue
                #proxy_list.append(proxy)
                yield proxy
        except:
            pass

def Connect(ip,port):
    #print '%-16s %-8s : '%(ip,port),
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        sk.connect((ip,int(port)))
        return True
    except Exception:
        return False
    sk.close()
    

def Proxy_read(proxy_ip,user_agent_list):
    #proxy_ip = '110.73.13.4:8123'
    print (u'cur agent: %s'%proxy_ip)
    user_agent = random.choice(user_agent_list)
    headers = {
            'Host': 's9-im-notify.csdn.net',
            'Origin':'http://blog.csdn.net',
            'User-Agent': user_agent,
            'Accept': r'application/json, text/javascript, */*; q=0.01',
            'Referer': r'http://blog.csdn.net/xiaohusaier' # %(random.randint(1000000,999999999))
            #'Referer': r'http://blog.csdn.net/mtbaby/article/details/75645602',
            }

    proxy_support = urllib2.ProxyHandler({'http':proxy_ip})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    
    burl = r'http://blog.csdn.net/mtbaby/article/details/75645602'
    req = urllib2.Request(burl,headers=headers)
    try:
        urllib2.urlopen(req, timeout=3).read().decode('utf-8')
    except:
        #print ('fail')
        return False
    else:
        global count
        count +=1
        print('OK!总计成功%s次！'%count)
        return True

if __name__ == '__main__':
    for aip in Get_proxy_ip():
        Proxy_read(aip, user_agent_list)