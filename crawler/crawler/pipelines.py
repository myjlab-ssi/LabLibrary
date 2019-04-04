# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from crawler import settings

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLPipeline(object):
    connection = None
    def open_spider(self, spider):
        
        self.connection = pymysql.connect(
            host=spider.settings.get("MYSQL_HOST"),
            user=spider.settings.get("MYSQL_USER"),
            password=spider.settings.get("MYSQL_PASSWORD"),
            db=spider.settings.get("MYSQL_DB_NAME"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
    def close_spider(self, spider):
        if self.connection:
            self.connection.close()
            self.connection = None

    def process_item(self, item, process):
        if item.get("price") == "":
            item["price"] = None
        with self.connection.cursor() as cursor:
            #TODO[marutaku] Insertの処理をよりシンプルにしたい
            sql = "INSERT INTO `books` (book_id, title, authors, image, image_2x, create_on, publisher, release_date, price, pages, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
            cursor.execute(sql, (item["book_id"], item["title"], item["authors"], item["image"], item["image_2x"], item["create_on"], item["publisher"], item["release_date"], item["price"], item["pages"], item["url"]))
        self.connection.commit()
        return item
        