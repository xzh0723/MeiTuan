美团美食店铺爬虫
==========

项目目录
--------

│  config.py
│  creat_token.py
│  demo.py
│  get_uuid.py
│  mongodb.py
│  parse.py
│  README.md
│
└─view
        db.pinglun.png.png
        db_dianpu.png.png
        pacharm_pinglun.png.png

环境依赖
---------
pyhon3.7.2

抓取流程
--------
  美团选定城市店铺首页开始，遍历抓取每页店铺列表，进而获取店铺id构造店铺评论详情API，抓取店铺所有评论。

    max_page = input('请输入你要查询的最大页码：')
    for page in range(1, int(max_page) + 1):
        fetch(page)
        
项目难点
---------
  测试期间发现美团的反爬措施有：
        
>>常规链接404（店铺详情页链接404页面）

>>_token参数

>>验证码（常规四字中英文混合）

>>cookies

破解反爬关键在于_token参数的构造，另外还有cookies的时效性问题，测试发现不登陆翻页获取的cookies时效性大约为爬取5页左右的店铺就会失效，需要不停切换。

反反爬
--------
_token参数的构造：
>>解密：
>>>>由现成_token参数结尾的'='猜测进行了base64加密，于是进行base64解密，得到bytes类型字符串，进行zlib解压后得出_token的加密生成字典，其中有两个比较重要的变化参数为ts和cts，其中ts为13位时间戳，cts则为ts+100*1000。还有一个sign参数，形式与_token参数一致，再对sign参数进行一次同样的解密，得到一个字符串，其中的uuid在首页源码中可以正则匹配出来。

>>加密：
>>>>由上可知_token参数的构造过程，进行了两次zlib压缩和base64编码加密。第一次加密对象位sign参数。第二次加密就是生成_token的字典，构造好字典后再进行一次上述加密即为_token。

解释说明
--------
未实现cookies切换，爬取失效后需自行更换cookies。（可以构建cookie池或者selenium翻页获取cookies保存到本地使用）。

运行
--------
  命令行切换至根目录：

>>> python demo.py

抓取结果
---------
 ![image](https://github.com/xzh0723/meituan/blob/master/view/db_dianpu.png.png)
 ![image](https://github.com/xzh0723/meituan/blob/master/view/db.pinglun.png.png)
 ![image](https://github.com/xzh0723/meituan/blob/master/view/pacharm_pinglun.png.png)

公告
=========
  本代码仅作学习交流，切勿用于商业用途，否则后果自负。若涉及点评网侵权，请邮箱联系，会尽快处理。
