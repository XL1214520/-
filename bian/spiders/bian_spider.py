# -*- coding: utf-8 -*-
import scrapy
from bian.items import BianItem


class BianSpiderSpider(scrapy.Spider):
    name = 'bian_spider'
    allowed_domains = ['netbian.com']
    start_urls = ['http://www.netbian.com/']

    def parse(self, response):
        img_urls = response.xpath("//div[@class='list']//li")
        next_url = response.xpath('//div[@class="page"]/a[11]/@href').extract_first()
        print(next_url)
        for img in img_urls:
            img_url = img.xpath("./a/@href").extract_first()
            yield scrapy.Request(url=response.urljoin(img_url),callback=self.img_url)
            break
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.next_url)

    # 下一页
    def next_url(self,response):
        img_urls = response.xpath("//div[@class='list']//li")
        next_url = response.xpath('//div[@class="page"]/a[8]/@href').extract_first()
        for img in img_urls:
            img_url = img.xpath("./a/@href").extract_first()
            yield scrapy.Request(url=response.urljoin(img_url),callback=self.img_url)
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.next_url)

    # 获取下载图片的网址
    def img_url(self,response):
        download_url = response.xpath("//div[@class='pic-down']/a/@href").extract_first()
        yield scrapy.Request(url=response.urljoin(download_url),callback=self.img_downlolds)

    # 获取图片名字，地址
    def img_downlolds(self,response):
        item = BianItem()
        item['img_name'] = response.xpath('//td[@align="left"]/a/@title').extract_first()
        item['img_download'] = response.xpath("//td[@align='left']/a/img/@src").extract_first()
        item["classification_title"] = response.xpath('//*[@id="main"]/div[2]/a[2]/text()').extract_first()
        yield item