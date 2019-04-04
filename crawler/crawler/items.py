# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BooklogItem(scrapy.Item):
    # ブクログ状の管理ID
    book_id = Field()
    # タイトル
    title = Field()
    # 著者
    authors = Field()
    # 本の画像
    image = Field()
    # 拡大画像？
    image_2x = Field()
    # 登録日
    create_on = Field()
    # 出版社
    publisher = Field()
    # 出版日
    release_date = Field()
    # 値段
    price = Field()
    # ページ数
    pages = Field()
    # URL
    url = Field()



