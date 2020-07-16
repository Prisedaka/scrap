import scrapy
from product_scraper.items import ProductScraperItem


class MySpider(scrapy.Spider):
    name = 'severotek'
    allowed_domains = ['severotek.ru']
    start_urls = [
        'http://severotek.ru',
    ]

    def parse(self, response):
        item = {}

        item['h1'] = response.xpath('//h1/text()').extract()
        item['h2'] = response.xpath('//h2/text()').extract()
        item['h3'] = response.xpath('//h3/text()').extract()
        item['h4'] = response.xpath('//h4/text()').extract()
        item['p'] = response.xpath('//p/text()').extract()
        yield item
