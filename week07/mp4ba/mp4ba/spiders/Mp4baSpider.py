import scrapy
import logging
from mp4ba.items import Mp4BaItem
class Mp4baSpider(scrapy.Spider):
    name = "mp4ba"
    allowed_domains = ["www.mp4ba.com"]
    start_urls = [
        "http://www.mp4ba.com/"
    ]

    def parse(self,response):
        top_selector=response.xpath('/html/body/section/div[1]/nav/ul/li/a/@href')
        # yield scrapy.Request(url=top_selector.extract()[3],callback=self.indexMp4ba)
        for top_url in top_selector.extract():
            yield scrapy.Request(url=top_url,callback=self.indexMp4ba)

    def indexMp4ba(self, response):
        nextpage_selector=response.xpath('//*[@id="page"]/a[@class="nextpage"]/@href')
        for nextpage_url in nextpage_selector.extract():
            yield scrapy.Request(nextpage_url,callback=self.indexMp4ba)

        item_selector=response.xpath('/html/body/section/div[4]/div[1]/div/div[2]/ul/li/a/@href')
        for item_url in item_selector.extract():  
            yield scrapy.Request(url=item_url,callback=self.detailMp4)


    def detailMp4(self,response):
        baiduYun_selector=response.xpath('//*[@id="fadecon"]/div[4]/ul/li')
        cl_720p_selector=response.xpath('//*[@id="fadecon"]/div[3]/ul/li/div/a[2]/@href')
        bt_720p_selector=response.xpath('//*[@id="fadecon"]/div[3]/ul/li/div/a[1]/@href')
        mv_type=response.xpath('/html/body/section/div[2]/a[3]/text()').extract_first()
        bt_720p=bt_720p_selector.extract_first()
        cl_720p=cl_720p_selector.extract_first()
        name=response.xpath('//*[@class="info_tit"]/text()').extract_first()
        for i in baiduYun_selector:
            item=Mp4BaItem()
            item["type"]=i.xpath('text()').extract()[0].replace(" ","").replace("\n","").replace("\t","").replace("\r","").replace("：","")
            item["path"]=i.xpath('div[@class="btn-group cloud"]/a/@href').extract_first()
            item["code"]=i.xpath('div[@class="btn-group cloud"]/p/text()').extract_first()
            item["cl_720p"]=cl_720p
            item["bt_720p"]=bt_720p
            item["name"]=name
            item["mv_type"]=mv_type
            item["url"]=response.url
            yield item
