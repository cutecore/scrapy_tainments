import scrapy
import logging

import requests
from demo.items import DemoItem

class ExampleSpider(scrapy.Spider):
    name = 'example'

    start_urls = ["https://www.baidu.com"]

    
    def parse(self, response):
        for i in range(1, 27):
            _temp = 'https://www.aventertainments.com/subdept_products.aspx?Dept_ID=29&SubDept_ID=525&languageID=2&whichtitle=0&Rows=1&CountPage=%d'%(i)
            yield scrapy.Request(_temp, callback=self.parse_list_page, meta={'proxy': 'http://127.0.0.1:10809'})


    def parse_list_page(self, response):
        list = response.css('.single-slider-product__image a::attr(href)').extract()
        for item in list:
            yield scrapy.Request(item, callback=self.parse_item_page, meta={'proxy': 'http://127.0.0.1:10809'})

    
    def parse_item_page(self, response):
        item = DemoItem()
        a = response.css('#sscontainerppv123 img::attr(src)').extract()
        b = response.css('#PlayerCover img::attr(src)').extract()
        c = response.css("#player-1 #player1 source::attr(src)").extract() 
        item['url'] = response.url
        item['cover'] = a[0]
        item['shoot'] = b[0]
        item['video'] = c[0]
        yield item


   
 




