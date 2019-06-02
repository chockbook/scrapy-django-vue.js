# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #名字，作者，状态，简介，封面，URL
    title = Field()
    author = Field()
    state = Field()
    intro = Field()
    cover = Field()
    comic_url = Field()

class ChapterItem(scrapy.Item):
    #章节，所属漫画，URL
    chapter = Field()
    comci_chapter = Field()
    chapter_url = Field()

class PageItem(scrapy.Item):
    #页数，本地路径，所属章节，URL
    page = Field()
    page_path = Field()
    chapter_page = Field()
    page_url = Field()


