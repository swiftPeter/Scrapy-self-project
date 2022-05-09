# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class URLSpider(scrapy.Spider):
    name = "URL"
    start_urls = [
        'https://ourcloudnetwork.com/ms-220-study-guide-troubleshooting-microsoft-exchange-online/'
    ]

    def parse(self, response):
        for quote in response.css('div.elementor-element-52ef7ed'):
            yield {
                'text': quote.css('li::text').getall(),
                'url': quote.css('a::attr(href)').getall()
                # 'tags': quote.css('div.tags a.tag::text').getall(),
            }
