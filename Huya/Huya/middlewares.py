# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
'''
 spider中间件是介入到Scrapy中的spider处理机制的钩子框架，可以插入自定义功能来处理发送给Spiders的response,以及spider产生的item和request。
1.激活Spider中间件(Spider Middlewares)
 要启用Spider中间件(Spider Middlewares)，可以将其加入到SPIDER_MIDDLEWARES设置中。该设置是一个字典，键为中间件的路径，值为中间件的顺序(order)。
 在setting.py
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware' : 543,
}
2.如果您想禁止内置的(在SPIDER_MIDDLEWARES_BASE中设置并默认启用的)中间件，您必须在项目的SPIDER_MIDDLEWARES设置中定义该中间件，并将其赋值为None，例如，如果您想要关闭off-site中间件：
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware': 543,
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': None,
}
'''


class HuyaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        '''
        ①创建一个TempSpiderMiddleware类的实例s；
        ②使用crawler实例的crawler.signals.connect方法将实例s的spider_opened方法与spider_opened信号绑定起来；
        ③返回实例s
        :param crawler:
        :return:
        '''
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        '''
        应该返回一个None或者抛出一个异常(exception)。
        如果其返回None，Scrapy将会继续处理该response，调用所有其他中间件直到spider处理该response。
        如果其抛出一个异常(exception),Scrapy将不会调用任何其他中间件的process_spider_input()方法，并调用request的errback。errback的输出将会以另一个方向被输入到中间链中，使用process_spider_output()方法来处理，当其抛出异常时则带调用process_spider_exception()
        :param response: (Response对象) - 被处理的response
        :param spider:(Spider对象) - 该response对应的spide
        :return:
        '''
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        '''
        当Spider处理Response返回结果时，process_spider_output会被调用
        process_spider_output方法必须返回包含Request或Item的可迭代对象
        :param response: 是Response对象，即生成该输出的Response。
        :param result: 包含Request或Item对象的可迭代对象，即Spider返回的结果
        :param spider: 是Spider对象，即其结果对应的Spider。
        :return:
        '''
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        '''
        当spider或(其它spider中间件的)process_spider_input()抛出异常时，该方法被调用
        process_spider_exception()必须要么返回None，要么返回一个包含Response或Item对象的可迭代对象(iterable)。
        通过其返回None，Scrapy将继续处理该异常，调用中间件链中的其它中间件的process_spider_exception()
        如果其返回一个可迭代对象，则中间件链的process_spider_output()方法被调用，其他的process_spider_exception()将不会被调用。
        :param response: (Response对象) - 异常被抛出时被处理的response
        :param exception: (Exception对象) - 被抛出的异常
        :param spider: (Spider对象) - 抛出异常的spider
        :return:
        '''
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        '''
        该方法以spider启动的request为参数被调用，执行的过程类似于process_spider_output()，只不过其没有相关联的response并且必须返回request(不是item)。
        其接受一个可迭代的对象(start_requests参数)且必须返回一个包含Request对象的可迭代对象。
        :param start_requests: (b包含Request的可迭代对象) - start requests
        :param spider: (Spider对象) - start request所属的spider
        :return:
        '''
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HuyaDownloaderMiddleware(object):
    '''
    Downloader Middleware的功能十分强大，修改User-Agent、处理重定向、设置代理、失败重试、设置Cookies等功能都需要借助它来实现
    '''
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        '''
        Reuqest在被Scrapy引擎调度给Downloader之前，process_request，方法就会被调用，也就是在Request从队列调出来到Downloader下载之前，我们都可以用process_request对其进行修改。
        方法的返回值必须是None，Request，Response之一，或者抛出异常IgnoreRequest

        返回None：
        Scrapy将会继续处理该Request，接着执行其他Downloader Middleware的process_request方法，其实就是修改Request的过程
        返回Response对象时：
        更低优先级的Downloader Middleware的process_request和process_exception方法都不会被调用，转而执行每个Downloader Middleware的process_response方法
        返回Request对象时：
        返回的Request对象会被重新添加到调度队列中，作为一个全新的Requet等待被调用
        抛出IgnoreRequest异常时：
        所有的Downloader Middleware的process_exception方法会被依次调用。如果没有一个方法处理异常，那么Request的errback方法会回调，如果该异常还没有被处理，就会被忽略
        :param request: 是Request对象，即被处理的Request。
        :param spider: 是Spdier对象，即此Request对应的Spider。
        :return:
        '''
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        '''
        Downloader 执行下载之后，会得到对应的Response。Scrapy引擎变回讲Response发送给spider进行解析，在发送之前，我们都可以用process_response方法来对Response进行修改处理。
        方法的返回值必须是Request，Response之一，或者抛出异常IgnoreRequest

        当返回Request时：
        更低优先级的Downloader Middleware的process_response方法不会被调用。Request会被添加进调度队列，等待被调度。
        返回Response时：
        每个Downloader Middleware的process_response方法会被继续调用，对该Response进行处理
        抛出异常IgnoreRequest时
        每个Request的errback方法会被回调，如果没有处理这个异常，就会被忽略
        :param request: 是Request对象，即此Response对应的Request。
        :param response: 是Response对象，即此被处理的Response。
        :param spider: 是Spider对象，即此Response对应的Spider。
        :return:
        '''
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        '''
        Downloader 或process_request 产生异常时，process_exception方法就会被调用
        方法返回值必须是None，Request，Response对象之一

        返回None：
        更低优先级的process_exception方法会被继续调用，直到所有的方法都被调用完毕
        返回Request时：
        更低优先级的process_exception方法不会被调用。新的Request直接被放入调度队列等候调用
        返回Response时：
        更低优先级的process_exception方法不会被调用，每个Downloader Middleware的process_response方法会被依次调用
        :param request: 是Request对象，即产生异常的Request。
        :param exception: 是Exception对象，即抛出的异常。
        :param spider: 是Spider对象，即Request对应的Spider。
        :return:
        '''
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        '''
        当spider开启时调用该函数，说明开始爬取数据并分配spider的资源
        :param spider: 开始爬取的spider对象
        :return:
        '''
        spider.logger.info('Spider opened: %s' % spider.name)
