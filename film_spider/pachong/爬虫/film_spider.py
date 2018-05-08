#coding:utf-8
import bs4
import urllib
from bs4 import BeautifulSoup
import urllib2
import sqlite3
import redis


print '连接数据库……'
cx = sqlite3.connect('PaChong.db')
#在该数据库下创建表

cx.execute ('''CREATE TABLE film(
   id INTEGER PRIMARY KEY   AUTOINCREMENT,
   name             str      null,
   url             str      null,
   director         str      null,
   edit             str      null,
   star             str      null,
   type             str      null,
   region             str      null,
   language             str      null,
   date             str      null,
   length            str      null,
   othername             str      null,
   IMDblink             str      null,
   brief             str      null,
   douban             str      null,
   postlink             str      null,
   IMDB             str      null,
   summery             str      null
);''')
print "Table created successfully";
print "数据库连接完成"


#main函数
def main():
    for num in xrange(12525,22200):
        cur_url = 'http://www.bd-film.com/gq/'
        num = str(num)
        h = ".htm"
        cur_url = cur_url + num + h
        mvi = {}
        #调用解析函数
        mvi = GetBdfilmInfo(cur_url)

        # 这里加一个判断，判断是否获取网页成功
        if not mvi.has_key('director'):
            print 'Page get failed:',num
            continue

        # 格式化数据，防止插入数据库sql有问题
        for k,v in mvi.items():
            if v:
                mvi[k] = v.replace("'","")
            else:
                mvi[k] = ''

        #这里拼接sql语句 
        filed_sql = []
        value_sql = []
        for k,v in mvi.items():
            filed_sql.append(k)
            value_sql.append(v)
        
        sql = 'insert into film(' + ','.join(filed_sql) + ') '
        sql += "values('" + "','".join(value_sql) + "');"
        #调用数据库函数
        if SqlExec(cx, sql):
            print "数据插入完毕",num
        else:
            print sql



#数据库执行函数
def SqlExec(conn,sql):
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception,e:
        print 'exec sql error[%s]'%(sql)
        print Exception,e
        cur = None
    return cur

#访问网页
def getHtml(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent":user_agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html
#爬取信息并存储数据
def GetBdfilmInfo(cur_url):
    # 先定义一个字典存储电影信息
    film_info = {}
    try:
        html_doc = getHtml(cur_url)
        sp = bs4.BeautifulSoup(html_doc,'html.parser',from_encoding="utf-8")

        # 当前url,这里把当前的url当做下载链接来处理
        film_info['url'] = cur_url

        # 标题处理
        film_info['name'] = ''
        title = sp.find('h3')
        if title:
            film_info['name'] = title.string

        # 豆瓣评分
        film_info['douban'] = ''
        db = sp.find('a',class_='list-douban')
        if db:
            film_info['douban'] = db.string


        # IMDB评分
        film_info['IMDB'] = ''
        imdb = sp.find('a',class_='list-imdb')
        if imdb:
            film_info['IMDB'] = imdb.string


        # 摘要
        film_info["summery"] = ''
        abst = sp.find('strong')
        if abst:
            einfo = ''
            for i,e in enumerate(abst.next_elements):
                if i>=2:
                    break
                einfo += e
            film_info['summery'] = einfo
    
    #下载链接，由于该电影网站对下载链接做了反爬虫机制，所以我们这里暂不处理
    #     down_div = sp.find("div",id = "bs-docs-download")
    #       
    #     film_info['urls'] = []
    #     down_list = []
    #     durls = down_div.find_all('a')
    #     for u in durls:
    #         down_list.append(str(u))
    #         continue
    #         for n in u.children:
    #             down_list.append(n)
    #     film_info['urls'] = down_list

        # 海报
        film_info['postlink'] = ''
        poster_url = sp.find('div',id = 'wx_pic')
        if poster_url:
            for img in poster_url.children:
                film_info['postlink'] = img.attrs["src"]

        #剧情介绍
        film_info['brief'] = ''
        jq = sp.find_all("div",style = "margin-bottom: 10px;")
        for x in jq:
            film_info['brief'] = x.get_text()

        # 电影信息
        mvinfo = []
        information = sp.find_all("div",attrs={'class':"span7",'sytle':"font-size:12px"})
        for b in information:
            for v in b.children:
                t = v.string
                if t:
                    mvinfo.append(''.join(t))
        spv = []
        cv = ''
        for v in mvinfo:
            if v.find(':')>=0:
                if cv:
                    spv.append(cv)
                cv = v
            else:
                cv += v
        spv.append(cv)

        # 字典名映射转换
        # 英文
        mvh = ["director", "edit", "star", "type", 
           "region", "language", "date", "length", 
           "othername", "IMDblink"]
        # 中文
        mvhcn = ["导演","编剧","主演","类型","制片国家/地区","语言","上映日期",
                 "片长","又名","imdb链接"]
        # 列表打包成字典,此时mvd是一个字典
        mvd =  dict(zip(mvhcn, mvh))
        # 先把抓取的数据整理成字典
        spvdict = {}
        for element in spv:
            its = [v.strip() for v in element.split(':')]
            if len(its) != 2:
                continue
            nm = its[0].lower()#统一成小写
            if type(nm).__name__=='unicode':
                nm = nm.encode('utf-8')
            vu = its[1]
            spvdict[nm] = vu    
    
        #将字典的key与数据库中的字段对应,这里用mvh列表存储
        for i,element in enumerate(mvh):
            if spvdict.has_key(mvhcn[i]):
                film_info[mvh[i]] = spvdict[mvhcn[i]]
            else:
                film_info[mvh[i]] = ''
    except:#处理网页不存在的情况
        pass
    return film_info


if __name__ == '__main__':
    main()












