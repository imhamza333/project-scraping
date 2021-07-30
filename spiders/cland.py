import scrapy

from ..items import ClandItem


class CroquetteLandSpider(scrapy.Spider):
    name = 'cland'
    start_urls = [
       # 'https://www.croquetteland.com/fr/royal-canin-care-nutrition-medium-sterilised.html'
       #  'https://www.croquetteland.com/fr/felichef-bio-chat-eminces-en-sauce-saumon.html'
         'https://www.croquetteland.com/fr/purina-dentalife-chien-moyen.html'
        # 'https://www.croquetteland.com/fr/hill-s-prescription-diet-feline-c-d-urinary-stress-metabolic.html'
        # 'https://www.croquetteland.com/fr/purina-dentalife-chien-moyen.html'

    ]

    def parse(self, response):
        item = ClandItem()

        title = response.css('.page-title span::text').get()
        item['title'] = title

        brand_name = response.css('.logo-produit .logo::text').get()
        item['brand_name'] = brand_name

        img = response.css('div.product.media img::attr(src)').getall()
        item['img'] = img

        description = response.css('#description ::text').getall()
        item['description'] = [line.strip() for line in description if line.strip()]

        a_dict = []
        for i in response.css("div.product-items"):
            size_name = i.css('.weight ::text').get(),
            price_per_unit = i.css('.weightprice ::text').get().strip()
            new_price = i.css('.price::attr(gtm-product-price)').get()
            old_price = i.css('.fullprice::attr(gtm-product-price)').get()
            if new_price:
                x = dict(size_name=size_name, price_per_unit=price_per_unit, new_price=new_price,
                         old_price=old_price)
            else:
                x = dict(size_name=size_name, price_per_unit=price_per_unit, price=old_price)

            a_dict.append(x)

        item['list_of_dict_one'] = a_dict
        yield item
