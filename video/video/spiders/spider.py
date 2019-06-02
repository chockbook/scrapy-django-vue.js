import requests
import json
import re
import os
import time
import scrapy
from scrapy import Request
from video.items import VideoItem

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',

        }

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    #sorry
    allowed_domains = ['xinpianchang.com', 'openapi-vtom.vmovier.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/id-76/sort-like?from=tabCutting']
    cookies = {
            'Authorization':'918B0156535E57304535E541B3535E584E2535E5A0C49EE9F3C3;',
    }
    
    def parse(self,response):

        url = "https://www.xinpianchang.com/a%s?from=ArticleList"
        post_list = response.xpath('//ul[@class="video-list"]/li')
        for post in post_list:
            # 视频ID
            pid = post.xpath('./@data-articleid').extract_first()
            #
            request = Request(url % pid, callback=self.parse_post)
            print(pid)
            yield request

    def parse_post(self,response):
        
        post = VideoItem()
        post['title'] = response.xpath(
            '//div[@class="title-wrap"]/h3/text()').extract_first()
        # 分类信息
        cates = response.xpath('//span[contains(@class, "cate")]/a/text()').extract()
        post['video_type'] = '-'.join([cate.strip() for cate in cates])

        # 提取视频的vid,这个是请求视频源文件地址的关键参数
        vid, = re.findall(r'vid: \"(\w+)\",', response.text)
        # 请求视频信息接口，把vid参数代入进去
        video_url = "https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource,resource_origin?"
        request = Request(video_url % vid, callback=self.parse_video)
        request.meta['post'] = post
        yield request

    def parse_video(self,response):
        """解析视频接口"""
        post = response.meta['post']
        resp = json.loads(response.text)
        # 视频源文件地址
        #post['video'] = resp['data']['resource']['progressive'][2]['url']
        post['video'] = resp['data']['resource']['default']['url']
        # 视频预览图地址
        post['cover'] = resp['data']['video']['cover']
        #视频请求
        vid_request = requests.get(url=post['video'],headers=headers).content
        vid_name = post['video'].split('/')[-1]
        #图片请求
        pic_request = requests.get(url=post['cover'],headers=headers).content
        pic_name = post['cover'].split('/')[-1]
        #进入django下的media目录
        media_path = r"F:\python\manhua\cvweb\media"
        os.chdir(media_path)
        #建立以下载时间为名的目录
        today = time.strftime('%Y%m%d',time.localtime(time.time()))
        if not os.path.exists(today):
            os.makedirs(today)
        os.chdir(today)
        #下载视频
        with open(vid_name, "wb") as f:
            print("downling-PIC---" + vid_name )
            f.write(vid_request)
            f.close()
            print("Done!")
        #下载图片
        with open(pic_name, "wb") as f:
            print("downling-PIC---" + pic_name )
            f.write(pic_request)
            f.close()
            print("Done!")

        #返回视频和图片的本地路径到数据库，django后面用到
        video_path = str(today) + '/' + vid_name
        post['video_path'] = video_path
        cover_path = str(today) + '/' + pic_name
        post['cover_path'] = cover_path


        yield post





