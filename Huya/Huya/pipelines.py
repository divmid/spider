# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

import scrapy

from scrapy.pipelines.images import ImagesPipeline

from Huya.settings import IMAGES_STORE


class HuyaImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        avatar180 = item['avatar180']
        yield scrapy.Request(avatar180)# 在setting配置图片保存路径

    def item_completed(self, results, item, info):
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        image_path = [x["path"] for ok, x in results if ok][0]
        print("image_path=======", image_path)
        print("IMAGES_STORE========", IMAGES_STORE)
        old_image_path = IMAGES_STORE+image_path
        print("old_image_path=======", old_image_path)
        new_image_path = IMAGES_STORE + item['nick'] + '.jpg'
        print("new_image_path=======", new_image_path)
        os.rename(old_image_path, new_image_path)

        item["image_path"] = new_image_path
        return item

class HuyaPipeline(object):

    def open_spider(self, spider):
        '''
        爬虫开启时只执行一次
        爬虫开启时，找到文件保存位置，并打开
        :param spider: Spider对象
        :return:
        '''
        print('open' * 80)
        self.file = open("虎牙直播.json", "w", encoding="utf-8")


    def close_spider(self, spider):
        '''
        爬虫结束时执行一次
        爬虫结束后将文件关闭，这种方式，若中间报错会使数据无法存储
        :param spider: Spider对象
        :return:
        '''
        print('close' * 80)
        self.file.close()


    def process_item(self, item, spider):
        '''
        每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理
        :param item: 爬取到的一项数据（Item或字典）
        :param spider: Spider对象
        :return:
        '''
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    # @classmethod
    # def from_crawler(cls):
    #     '''
    #     创建Item Pipeline对象时回调该类方法。通常，在该方法中通过crawler.settings读取配置，根据配置创建Item Pipeline对象。
    #     :return:
    #     '''
    #     return cls()