#coding:utf-8
import bobo
@bobo.query('/')
def hello(name="World"):
    s = '''
    <!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title> 欢迎来到BD影视剧场~~</title>
<style type="text/css">
span{
color:red;
}
</style>
</head>
<body>
<img src="//www.baidu.com/img/bd_logo1.png" width="258" height="200" />
<h1>Welcome to mtbaby's Movie site</h1>
<form method="post" action="bs4demo.py" style = "color:red">
      <input type='text' border = '3px' name='wd' id='kw' length='200px' autocomplete="off"> 
      <p><input type="submit" value="搜索"  name="submit" /></p>
</form>  

<table summery = "电影表格"  width='100%' border="3px" cellspacing="0px" bordercolor="#6699ff">
    <caption>电影表格</caption>
    <tr>
        <th>电影名</th>
        <th>下载链接</th>
        <th>导演</th>
        <th>编剧</th>
        <th>主演</th>
        <th>类型</th>
        <th>地区</th>
        <th>语言</th>
        <th>上映日期</th>
        <th>片长</th>
        <th>又名</th>
        <th>IMDB链接</th>
        <th>简介</th>
        <th>豆瓣评分</th>
        <th>海报链接</th>
        <th>IMDB评分</th>
        <th>摘要</th>
    </tr>
    <tr>
        <td>2016韩国纪录片《卢武铉：双城记》HD720P.韩语中字</td>
        <td><a href="http://www.bd-film.com/gq/23000.htm" title = "点击进行下载"/>下载地址</td>
        <td>Jeon In-hwan</td>
        <td>Jeon In-hwan</td>
        <td>卢武铉</td>
        <td>纪录片</td>
        <td>韩国</td>
        <td>韩语</td>
        <td>2016-10-26(韩国)</td>
        <td>90分钟</td>
        <td>武铉：双城记 / Moo-hyun, the Story of Two Cities</td>
        <td></td>
        <td>剧情简介　　影片记录了卢武铉前总统一心希望建设没有岭南、湖南之分的社会，
        并为之努力的身影以及后代人们跟随他的脚步共同建设家园。</td>
        <td>0</td>
        <td><img src="http://p1.bqimg.com/10086/078645d0cf440828.jpg" title = "电影介绍"/></td>
        <td>IMDB评分</td>
        <td>摘要： 2.08G HD720P 都说韩国总统是个高危职业，不是被杀就是自杀，
        而这部纪录片从卢武铉来展现韩国存在的问题，韩国上映反响强烈，有兴趣可以看看~</td>
    </tr>
    



</body>
</html>

    '''
    return s