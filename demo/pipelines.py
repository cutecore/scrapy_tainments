# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import logging

import requests


class DemoPipeline:

    def process_item(self, item, spider):
        self.download(item['cover'],"1_")
        self.download(item['shoot'],"2_")
        self.download(item['video'],"3_")
        # M3U8 可以使用 https://github.com/nilaoda/N_m3u8DL-CLI 进行批量下载
       


    def download(self, url, path):
        proxies = {
        "http": "http://127.0.0.1:10809",
        "https": "http://127.0.0.1:10809"
        }  
        
        file_name = "c:/intel/blue/" + path + url.split('/')[-1]
        response = requests.get(url,proxies=proxies)
        with open(file_name,"wb") as code:
            code.write(response.content)
    
    
