import scrapy
from product_scraper.items import ProductScraperItem


class MySpider(scrapy.Spider):
    name = 'smi2'
    allowed_domains = ['smi2.ru']
    start_urls = [
        'https://smi2.ru',
    ]

    def parse(self, response):
        item = {}

        item['span'] = response.xpath('//span/text()').extract()

        yield item
