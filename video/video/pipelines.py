# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import re

class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='######',
            port=3306,
            db='#####',
            user='root',
            password='######',
            charset='utf8mb4',
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        
        values = (
            item['title'],
            item['video_path'],
            'No',
            item['video_type'],
            item['cover_path']


        )
        sql = 'INSERT INTO xpc_video VALUES (NULL,%s,%s,%s,%s,now(),%s)'
        self.cur.execute(sql, values)
        self.conn.commit()
        return item

'''
class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        yield Request(url=item['cover'],meta={'name':item['title']})

    def item_completed(self, results, item, info):
        # 是一个元组，第一个元素是布尔值表示是否成功
        if not results[0][0]:
            raise DropItem('下载失败')
        return item

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 提取url前面名称作为图片名
        image_name = request.url.split('/')[-1]
        # 清洗Windows系统的文件夹非法字符，避免无法创建目录
        folder_strip = re.sub(r'[？\\*|“<>:/]', '', str(name))
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(folder_strip, image_name)
        return filename
'''

