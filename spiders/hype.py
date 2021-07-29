import scrapy

from ..items import HypeItem


# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


class HypeSpider(scrapy.Spider):
    name = 'hype'
    start_urls = [
         'https://www.hypedc.com/au/adidas-performance-ultraboost-20-core-black-core-black-signal-green-eg0711.html'
       # 'https://www.hypedc.com/au/adidas-ultra4d-5-0-core-black-cloud-white-carbon-g58158.html'
    ]

    # rules = (
    #
    #     Rule(LinkExtractor(restrict_css=('.nav-primary-category-list',))),
    #     Rule(LinkExtractor(restrict_css=('.category-products',)), callback=parse_item, follow=False),
    #     Rule(LinkExtractor(restrict_css=('.next',))),
    #
    #
    # )

    def parse(self, response):
        item = HypeItem()

        title = response.css(".product-name::text").get().strip()
        item['title'] = title

        img = response.css("#main-image img::attr(data-src)").getall()
        item['img'] = img

        description = []
        for i in response.css('.product-description[itemprop="description"] ::text').getall():
            description.append(i.strip())
        item['description'] = description

        size_cat = response.css("#size-selector-desktop-tabs a ::text").getall()
        item['size_cat'] = size_cat

        size = []
        for i in response.css('div[id^="size-selector-tab-desktop"] a::text').getall():
            size.append(i.strip())
        item['size'] = size

        new_price = response.css('#product_addtocart_form [itemprop="price"]::attr(content)').get()
        old_price = response.css('#product_addtocart_form .old-price .price::text').get('').strip()
        if old_price:
            item['old_price'] = old_price
            item['new_price'] = new_price
        else:
            item['price'] = new_price

        yield item

