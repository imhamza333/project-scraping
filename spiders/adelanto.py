import scrapy
from ..items import Adelanto


class Adelanto_spider(scrapy.Spider):
    name = 'adelanto'
    start_urls = [
        'https://www.agourahillscity.org/'
    ]

    def parse(self, response):
        item = Adelanto()

        lst = []
        for respons in response.css('.event-item'):
            date = respons.css('.event-item .datebox div ::text').getall(),
            title = respons.css('.event-item .box_item_title ::text').getall()
            timing = respons.css('.event-item .box_item_summary ::text').getall()
            dict_data = dict(date=date, title=title, timing=timing)

            lst.append(dict_data)

        item['data'] = lst
        yield item






        # item['list_of_dict_one'] = a_dict
        # for data in response.css('.event-item'):
        #     item['data'] = {
        #         'date': data.css('.event-item .datebox div ::text').getall(),
        #         'title': data.css('.event-item .box_item_title ::text').getall(),
        #         'timing': data.css('.event-item .box_item_summary ::text').getall(),
        #     }
        # yield item

        # date = response.css('.event-item .datebox div ::text').getall()
        # item['date'] = date
        #
        # title = response.css('.event-item .box_item_title ::text').getall()
        # item['title'] = title
        #
        # timing = response.css('.event-item .box_item_summary ::text').getall()
        # item['timing'] = timing
        #
        # yield item
