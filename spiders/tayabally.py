import scrapy
from ..items import TayabItem


class HypeSpider(scrapy.Spider):
    name = 'tayaballay'
    page_number = 2
    start_urls = [
        'https://www.tayabally.com/category/hunting-shooting-wear?page=1'
    ]

    def parse(self, response):
        item = TayabItem()

        title = response.css(".name::text").get()
        item['title'] = title
        description = response.css("#description div::text").get()
        item['description'] = description
        description_one = response.css(".description-container.m-t-20::text").get()
        item['description_one'] = description_one
        price = response.css(".price-box span::text").get()
        item['price'] = price

        response.css("#main-image img::attr(data-src)").getall()

        yield item

        next_page = 'https://www.tayabally.com/category/hunting-shooting-wear?page=' + str(HypeSpider.page_number)
        if HypeSpider.page_number <= 4:
            HypeSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
