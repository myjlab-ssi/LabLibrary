# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
import json
from crawler.items import BooklogItem


class BooklogSpider(scrapy.Spider):
    name = 'booklog'
    allowed_domains = ['booklog.jp']
    start_urls = ['https://booklog.jp/users/myutaka3/all?category_id=all&status=all&sort=sort_desc&rank=all&page={}&json=true']

    def start_requests(self):
        page_counter = 84
        while True:
            next_url = self.start_urls[0].format(page_counter)
            page_counter += 1
            yield scrapy.Request(next_url, callback=self.parse)
    def parse(self, response):
        booklog_json = json.loads(response.text)
        self.logger.info(f"Get response object {response}")
        if len(booklog_json["books"]) == 0:
            # booksが0になったらクローリング終了
            raise CloseSpider("Crawling complete")
        for book in booklog_json["books"]:
            booklog_item = BooklogItem()
            booklog_item["book_id"] = book["book_id"]
            booklog_item["title"] = book["title"]
            booklog_item["image"] = book["image"]
            booklog_item["image_2x"] = book["image_2x"]
            booklog_item["create_on"] = book["create_on"]

            book_item = book["item"]
            booklog_item["url"] = book_item["url"]
            # 著者が複数人いる場合はカンマで区切る
            booklog_item["authors"] = book_item["author"]
            booklog_item["publisher"] = book_item["publisher"]
            booklog_item["release_date"] = book_item["release_date"]
            booklog_item["price"] = book_item["price"]
            booklog_item["pages"] = book_item["pages"]
            booklog_item["url"] = book_item["url"]
            yield booklog_item

        
