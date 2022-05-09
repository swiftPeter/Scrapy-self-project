# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class URLSpider(scrapy.Spider):
    name = "Douban"
    start_urls = [
        'https://movie.douban.com/top250?start=0&filter='
    ]

    def parse(self, response):
        self.logger.info('item page %s', response.url)
        for movie in response.css('div.item'):
            yield {
                'Movie link': movie.css('div.pic a::attr(href)').get(),
                'Movie Picture': movie.css('::attr(src)').get(),
                'Movie Name': movie.css('span.title::text').get(),
                'Rate': movie.css('span.rating_num::text').get(),
                'Quote': movie.css('span.inq::text').get(),
            }

        next_page = response.css('span.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

