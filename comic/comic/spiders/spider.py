# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from comic.items import ComicItem,ChapterItem,PageItem
from scrapy import Selector
import time
import requests
from lxml import etree



class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['comic.kukukkk.com','n9.1whour.com']
    start_urls = ['http://comic.kukukkk.com/comictype/3_2.htm']
    #图片也=页网址
    pagehost = 'http://n9.1whour.com/'
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Cookie': '2292_2223_120.85.181.191=1; Hm_lvt_5faade0d566fcec8b00f8d195be751aa=1558610847; 1934_2232_120.85.181.191=1; 2292_2264_120.85.181.191=1; Hm_lpvt_5faade0d566fcec8b00f8d195be751aa=1558611352',
                'Host': 'comic.kukukkk.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'

            }

    def parse(self, response):
        item = ComicItem()
        url = "http://comic.kukukkk.com%s"
        #获取页面内所有漫画
        post_list = response.xpath('//*[@id="comicmain"]/dd/a[2]')
        for post in post_list:
            item['title'] = post.xpath('text()').extract()[0]
            item['comic_url'] =post.xpath('@href').extract()[0]
            #uurl = 'http://comic.kukukkk.com' + item['comic_url']

            #.................算了,就这样吧
            co_request = requests.get(url=url % item['comic_url'],headers=self.headers)
            co_request.encoding='gb2312'
            text = co_request.text
            xhtml = etree.HTML(text)
            item['intro'] = xhtml.xpath('//*[@id="ComicInfo"]/text()')#简介,
            item['author'] = re.findall('作者：[^\s]+',text)#作者,
            item['state'] = re.findall('漫画状态：[^\s]+',text)#状态,
            item['cover'] = "comic_default.jpg"
            yield item
            #...................
            #把title传到下一个函数
            request = Request(url % item['comic_url'],meta={'comic':item['title']},callback=self.comic_parse)
            request.meta['item'] = item
            yield request

        

    def comic_parse(self,response):
        item = ChapterItem()
        #co_item = response.meta['item']
        
        #co_item['intro'] = response.xpath('//*[@id="ComicInfo"]/text()').extract()#简介,
        #co_item['author'] = re.findall('作者：[^\s]+',response.text)#作者,
        #co_item['state'] = re.findall('漫画状态：[^\s]+',response.text)#状态,
        #co_item['cover'] = "comic_default.jpg"
        
        chapter = response.xpath('//*[@id="comiclistn"]/dd/a[1]/text()').extract()#章节，
        chapter_url = response.xpath('//*[@id="comiclistn"]/dd/a[2]/@href').extract()#链接，
        for index in range(len(chapter)):
            i = 0  #页数
            item['comci_chapter'] = response.meta['comic']
            item['chapter'] = chapter[index]
            item['chapter_url'] = chapter_url[index]
            yield item
            request = Request(item['chapter_url'],meta={'ye':i,'chapter':item['chapter']},callback=self.page_parse)
            yield request
            
       # yield co_item

    def page_parse(self,response):
        hxs=Selector(response)
        item = PageItem()
        #页数自增+1      
        i = int(response.meta['ye']) + 1
        item['page'] = i
        item['chapter_page']= response.meta['chapter']

        try:
            #有些页面可能解释不出来
            img = hxs.xpath('//script/text()').extract()
            img_url = re.findall(r"newkuku[^\s]+.jpg",img[0])[0]
            item['page_url'] ="http://n9.1whour.com/" + img_url
        except Exception as d:
            item['page_url'] = "http://img.guu2.com/data/attachment/forum/threadcover/03/5d/16078.jpg"

        
        finally:
            
            try:

                # 获取下一页图片地址
                #不能超过最后一页
                next_img = response.xpath('//img[@src="/images/d.gif"]/../@href').extract()[0]
                next_page_url = "http://comic.kukukkk.com" + next_img
                #回调自身，获取下一页
                request = Request(next_page_url,meta={'ye':i,'chapter':item['chapter_page']},callback=self.page_parse)

                yield request

            except Exception as e:
                print("错误")
        

        yield item

        

        
        

