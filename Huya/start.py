from scrapy import cmdline

'''
from scrapy import cmdline
# 方式一：注意execute的参数类型为一个列表
cmdline.execute('scrapy crawl spidername'.split())
# 方式二:注意execute的参数类型为一个列表
cmdline.execute(['scrapy', 'crawl', 'spidername'])
'''
# cmdline.execute("scrapy crawl huyahost".split())
cmdline.execute("scrapy crawl atguigu".split())