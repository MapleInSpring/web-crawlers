# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KubepartnersSpider(CrawlSpider):
    name = 'kubepartners'
    allowed_domains = ['https://kubernetes.io/partners/#kcsp']
    start_urls = ['http://https://kubernetes.io/partners/#kcsp/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # get all the partners
        return i
