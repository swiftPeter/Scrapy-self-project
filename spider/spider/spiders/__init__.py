# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class URLSpider(scrapy.Spider):
    name = "lianjia"
    start_urls = [
        'https://sh.lianjia.com/chengjiao/pg1/'
    ]

    cookies = {
        'lianjia_ssid': '2f4bd56b-b0c7-487d-ae1c-6a8d8ce4fc3f',
        'lianjia_token': '2.0014e06cc077eaf29b054d45f15040f5ac',
        'lianjia_token_secure': '2.0014e06cc077eaf29b054d45f15040f5ac',
        'lianjia_uuid': '9bc9e2e0-0236-4101-a9b2-579eed11bf2a',
        'login_ucid': '2000000110097335'
    }

    def start_requests(self):
        for page in range(1, 100):
            yield scrapy.Request(f'https://sh.lianjia.com/chengjiao/pg{page}/', cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        self.logger.info('item page %s', response.url)
        for lianjia in response.css('ul.listContent li'):
            yield {
                'House picture': lianjia.css('::attr(href)').get(),
                'House name': lianjia.css('div.title ::text').get(),
                'House info': lianjia.css('div.houseInfo::text').get(),
                'Deal date': lianjia.css('div.dealDate  ::text').get(),
                'TotalPrice': lianjia.css('div.totalPrice span.number::text').get(),
                'Position information': lianjia.css('div.positionInfo::text').get(),
                'Unit price': lianjia.css('div.unitPrice span.number::text').get(),
                'Listed price': lianjia.css('div.dealCycleeInfo span.dealCycleTxt ::text').get(),
                'Deal cycle': lianjia.css('div.dealCycleeInfo ::text').getall()[1]
            }

            # next_page = response.css('li.next a::attr(href)').get()
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)
