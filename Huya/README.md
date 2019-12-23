---
## 项目目录结构
```
├── Huya   项目名
│   ├── __init__.py
│   ├── items.py                数据保存格式
│   ├── middlewares.py          存放自己定义的middleware
│   ├── pipelines.py            数据存储
│   ├── settings.py             设置文件
│   └── spiders                 存放具体某个网站的爬虫
│       ├── huyahost.py         爬虫文件，使用命令scrapy genspider huyahost www.huya.com生成
│       ├── __init__.py         
├── images
├── README.md
├── scrapy.cfg                     配置文件 
├── start.py                       启动文件 python start.py
└── 虎牙直播.json
```
---
## 环境

```
python 3.7
pip install scrapy
```
---
## 启动

```
python start.py
```
---
## 功能描述
1. 爬去虎牙直播的主播信息
2. 下载主播头像以主播昵称为图片名存储到images文件夹下


