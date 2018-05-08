#coding:utf-8
import redis
import sqlite3
from film_spider import SqlExec
#1.mid去redis查
#2.如果没有，取数据库数据
#3.写redis
#4.返回查询数据

def RedisMviQuery(mid):
    #定义空字典来存储查询结果
    mvi_dict = {}
    key_name = 'film_info_'+str(mid)
    
    # **1.mid去redis查**
    r = redis.Redis(host = 'localhost', port = 6379, db = 0)
    if r.exists(key_name):
        return r.hgetall(key_name)
    else:
        print "没有查询到，将连接数据库查询，并返回查询结果"
    # **2.取数据库数据**
    #连接数据库
    cx = sqlite3.connect('PaChong.db')
    #sql查询，将查询结果返回到query_result列表
    sql2 = "select * from film where id=%d"%(mid)
    #调用数据库执行函数
    cu = SqlExec(cx,sql2)
    query_result = []
    if cu:
        row = cu.fetchone()
    query_result = row
    if not query_result:
        print "无查询结果"
        return mvi_dict

    mvi_key = ["ID","name","director","url", "edit", "star", "type", 
       "region", "language", "date", "length", 
       "othername", "IMDblink","brief","douban","postlink","IMDB","summery"]
    
    for i,m in enumerate(mvi_key):
        mvi_dict[m] = query_result[i]
    
    # **3.把查询到的结果储存到redis**
    for k,v in mvi_dict.items():
        r.hset(key_name,k,v)

    # **4.返回**
    return mvi_dict

if __name__ == "__main__":
    mvi = RedisMviQuery(3)
    for k,v in mvi.items():
        print k,':',v























