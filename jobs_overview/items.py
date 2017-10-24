# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsOverviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    education = scrapy.Field()
    required_year = scrapy.Field()
    apply_count = scrapy.Field()
    comp_name = scrapy.Field()
    industry = scrapy.Field()
    salary = scrapy.Field()
    appearDate = scrapy.Field()
    link = scrapy.Field()
    others = scrapy.Field()
    datetime = scrapy.Field()

