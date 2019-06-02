# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from comic.items import ComicItem,ChapterItem,PageItem
import pymysql 
import os
import requests

class ComicPipeline(object):

    def __init__(self):
        self.conn = None
        self.cur = None
    def open_spider(self, spider):
        #数据库连接
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='xpc_videos',
            user='root',
            password='chock2333',
            charset='utf8mb4',
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    #将漫画，章节，页数分别写进数据库
    def process_item(self, item, spider):
        
        if isinstance(item,ComicItem):
            comic_values = (
            item['title'],
            str(item['author']),
            str(item['state']),
            str(item['intro']),
            item['cover']

        )
            sql = 'INSERT INTO comic VALUES (NULL,%s,%s,%s,%s,%s)'  #id自增，设为null
            self.cur.execute(sql, comic_values)
            self.conn.commit()

        elif isinstance(item,ChapterItem):
            chapter_values = (
            item['chapter'],
            item['comci_chapter'],
            
        )
            sql = 'INSERT INTO chapter VALUES (NULL,%s,now(),%s)'  #创建时间,使用now（）
            self.cur.execute(sql, chapter_values)
            self.conn.commit()
        elif isinstance(item,PageItem):
            #下载图片
            #F:\python\manhua\cvweb\media\comic
            host_path = "F:\python\manhua\cvweb\media\comic\\"
            #机械依存系少女的麻烦日常 3话
            chapter_page = item['chapter_page']
            p = chapter_page.split()
            #漫画目录
            co = p[0]
            #章节
            ch = p[1]           
            #http://n9.1whour.com/newkuku/2019/05/03/对老师oo是不行的哦_第01话/000264K.jpg
            img_name = item['page_url'].split('/')[-1]

            dir_path = host_path + co + '\\' + ch
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            
            os.chdir(dir_path)

            #下载
            res = requests.get(url=item['page_url'])
            with open(img_name,'wb') as f:
                f.write(res.content)
                f.close()
            
            #图片本地路径
            page_path = "comic/%s/%s/%s" % (co,ch,img_name) 
            item['page_path'] = page_path


            #写进数据库
            page_values = (
            item['page_path'],
            str(item['page']),
            item['chapter_page']
   
            
        )
            sql = 'INSERT INTO page VALUES (NULL,%s,%s,%s)'
            self.cur.execute(sql, page_values)
            self.conn.commit()
            '''
            res = dict(item)
            aa = res['chapter_page']
            bb = str(res['page']) #int->字符串
            cc = res['page_url']
            file_name = "aa.txt"
            with open(file_name,"a+",encoding='utf-8') as f:
                f.write(aa + "\n")
                f.write(bb + "\n")
                f.write(cc + "\n")
                f.close()
                '''
        return item




'''
class ComicPipeline(object):
    def process_item(self, item, spider):
        return item

class ComicPipeline(object):
    def process_item(self, item, spider):
        return item
'''