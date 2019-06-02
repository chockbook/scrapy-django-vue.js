# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    video = Field()
    jianjie = Field()
    video_type = Field()
    date = Field()
    cover = Field()
    cover_path = Field()
    video_path = Field()

