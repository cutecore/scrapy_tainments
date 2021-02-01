# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DemoItem(scrapy.Item):
    cover = scrapy.Field()
    shoot = scrapy.Field()
    video = scrapy.Field()
    url = scrapy.Field()
    pass



