# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxes=response.xpath(r'//div[@class="uibox"]')[1:]    #[1:]表示为不要第一个元素
        for uibox in uiboxes:
            category=uibox.xpath(r'.//div[@class="uibox-title"]/a/text()').get()    #点表示在当前循环内的，点get表示只获取一份
            # print(category) #打印标题
            urls=uibox.xpath(r'.//ul/li/a/img/@src').getall() #获取图片链接，getall()提取所有
            # print(urls) #这样得到的链接是前面缺少https的
            ''' for url in urls:
                # url="https:"+url  #第1种方法在url前面加https:
                url=response.urljoin(url)   #第2种方法在url前面加https: 也就是说会自动添加
                print(url) '''
            urls=list(map(lambda url: response.urljoin(url),urls))  #第3种方法url前面加https:
            # print(urls)
            item=BmwItem(category=category,urls=urls)
            yield item
