# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


'''
爬取的主要目标就是从非结构性的数据源提取结构性数据，例如网页。 Scrapy spider可以以python的dict来返回提取的数据.虽然dict很方便，并且用起来也熟悉，但是其缺少结构性，容易打错字段的名字或者返回不一致的数据，尤其在具有多个spider的大项目中。。

为了定义常用的输出数据，Scrapy提供了 Item 类。 Item 对象是种简单的容器，保存了爬取到得数据。 其提供了 类似于词典(dictionary-like) 的API以及用于声明可用字段的简单语法。

许多Scrapy组件使用了Item提供的额外信息: exporter根据Item声明的字段来导出数据、 序列化可以通过Item字段的元数据(metadata)来定义、 trackref 追踪Item实例来帮助寻找内存泄露 (see 使用 trackref 调试内存泄露) 等等。
'''

class HuyaItem(scrapy.Item):
    '''
    Field 对象指明了每个字段的元数据(metadata)。例如下面例子中 last_updated 中指明了该字段的序列化函数。
    您可以为每个字段指明任何类型的元数据。
    Field 对象对接受的值没有任何限制。也正是因为这个原因，文档也无法提供所有可用的元数据的键(key)参考列表。
    Field 对象中保存的每个键可以由多个组件使用，并且只有这些组件知道这个键的存在。您可以根据自己的需求，定义使用其他的 Field 键。
    设置 Field 对象的主要目的就是在一个地方定义好所有的元数据。 一般来说，那些依赖某个字段的组件肯定使用了特定的键(key)。
    您必须查看组件相关的文档，查看其用了哪些元数据键(metadata key)。
    '''
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主播的昵称nick
    nick = scrapy.Field()
    # 直播的链接 privateHost
    privateHost = scrapy.Field()
    # 主播的图片 avatar180
    avatar180 = scrapy.Field()
    # 主播的图片保存的路径 image_path
    image_path = scrapy.Field()

