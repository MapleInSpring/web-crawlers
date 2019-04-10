# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class KubepartnersSpider(CrawlSpider):
    name = 'kubepartners'

    def start_requests(self):
        urls = [
            'https://kubernetes.io/partners/#kcsp',
            'https://landscape.cncf.io/category=kubernetes-certified-service-provider&format=card-mode&grouping=category&embed=yes'
            ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # get all the partners
        divs = response.xpath('//div').getall()
        div_number = len(divs)
        self.logger.info('total number of divs {0}'.format(div_number))

        # debug with shell
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        self.logger.info('hello world')
        return i
