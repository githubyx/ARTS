# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp4BaItem(scrapy.Item):
    # define the fields for your item here like:
    id=scrapy.Field()
    url=scrapy.Field()
    name=scrapy.Field()
    path=scrapy.Field()
    type=scrapy.Field()
    code=scrapy.Field()
    bt_720p=scrapy.Field()
    cl_720p=scrapy.Field()
    mv_type=scrapy.Field()
    pass

class Mp4BaInfoItem(scrapy.Item):
    # define the fields for your item here like:
    id=scrapy.Field()
    name=scrapy.Field()
    bj=scrapy.Field()
    zy=scrapy.Field()
    lx=scrapy.Field()
    dq=scrapy.Field()
    yy=scrapy.Field()
    sysj=scrapy.Field()
    xkSjc=scrapy.Field()
    pc=scrapy.Field()
    pf=scrapy.Field()
    jj=scrapy.Field()
    pass
