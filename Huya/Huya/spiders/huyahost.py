# -*- coding: utf-8 -*-
import scrapy
import json
from Huya.items import HuyaItem

#Scrapy中的数据流由执行引擎控制，其过程如下：

#1.引擎从Spiders中获取到的最初的要爬取的请求(Requests)。
#2.引擎安排请求(Requests)到调度器中，并向调度器请求下一个要爬取的请求(Requests)。
#3.调度器返回下一个要爬取的请求(Request)给请求。
#4.引擎从上步中得到的请求(Requests)通过下载器中间件(Downloader Middlewares)发送给下载器(Downloader),这个过程中下载器中间件(Downloader Middlerwares)中的process_request()函数就会被调用。
#5.一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(Downloader Middlewares)中的process_response()函数，最后返回给引擎
#6.引擎从下载器中得到上步中的Response并通过Spider中间件(Spider Middewares)发送给Spider处理，这个过程中Spider中间件(Spider Middlewares)中的process_spider_input()函数会被调用到。
#7.Spider处理Response并通过Spider中间件(Spider Middlewares)返回爬取到的Item及(跟进的)新的Request给引擎，这个过程中Spider中间件(Spider Middlewares)的process_spider_output()函数会被调用到。
#8.引擎将上步中Spider处理的及其爬取到的Item给Item管道(Piplline),将Spider处理的Requests发送给调度器，并向调度器请求可能存在的下一个要爬取的请求(Requests)
#9.(从第二步)重复知道调度器中没有更多的请求(Requests)。


class HuyaHostSpider(scrapy.Spider):
    name = 'huyahost'
    allowed_domains = ['https://www.huya.com']
    page = 1
    url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page="
    url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2633&tagAll=0&page="

    start_urls = [url+str(page)]

    def parse(self, response):
        print(response.url)
        text = json.loads(response.text)
        # print(text)

        for live_item in text["data"]["datas"]:
            if self.page < 4:
                self.page += 1
            new_next_url = self.url + str(self.page)
            yield scrapy.Request(new_next_url, callback=self.parse)
            # 主播的昵称nick
            nick = live_item["nick"]
            # 直播的链接 privateHost
            privateHost = live_item["privateHost"]
            # 主播的图片保存的路径 avatar180
            avatar180 = live_item["avatar180"]
            print(nick)
            print(privateHost)
            print(avatar180)
            item = HuyaItem()
            item["nick"] = nick
            item["privateHost"] = privateHost
            item["avatar180"] = avatar180
            yield item