# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
# from scrapy.pipelines.images import ImagesPipeline
# from bmw import settings

class BmwPipeline:
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"images") #获取到BMW路径并拼接
        if not os.path.exists(self.path):  #判断语句，如果不存在image文件夹，就生成一个
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category=item["category"]
        urls=item["urls"]

        category_path=os.path.join(self.path,category)
        if not os.path.exists(category_path):   #如果不存在category分类的文件夹就创建一个
            os.mkdir(category_path)

        for url in urls:
            image_name=url.split("__")[-1]
            request.urlretrieve(url,os.path.join(category_path,image_name))

        return item

# class BMWImagesPipeline(ImagesPipeline):
#     def get_media_requests(self,item,info):
#         request_objs=super(BMWImagesPipeline,self).get_media_requests(item,info)
#         for request_obj in request_objs:
#             request_obj.item=item
#         return request_objs

#     def file_path(self,request,response=None,info=None):
#         path=super(BMWImagesPipeline,self).file_path(request,response,info)
#         category=request.item.get("category")
        
#         images_store=settings.IMAGES_STORE
#         category_path=os.path.join(images_store,category)
        
#         if not os.path.exists(category_path):
#             os.mkdir(category_path)
#         image_name=path.replace("full/","") #拿到照片名
#         image_path=os.path.join(category_path,image_name)
        
#         return image_path