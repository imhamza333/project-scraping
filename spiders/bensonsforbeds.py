import scrapy
from ..items import Bensonsforbeds


class Bensons_Spider(scrapy.Spider):
    name = 'bensonsforbeds'
    start_urls = [
        # 'https://www.bensonsforbeds.co.uk/products/simply-bensons-lyndon-options-divan-bed-set/?sku=756320032'
        # 'https://www.bensonsforbeds.co.uk/products/simply-bensons-zander-memory-support-divan-bed-set/?sku=766420061'
        # 'https://www.bensonsforbeds.co.uk/products/super-comfort-luxury-latex-pillow/?sku=DUN000021'
        # 'https://www.bensonsforbeds.co.uk/products/hotel-luxury-fitted-sheet/?sku=COM135100'
        # 'https://www.bensonsforbeds.co.uk/products/kuban-usb-charging-upholstered-bedside-table/?sku=STK451101'
        # 'https://www.bensonsforbeds.co.uk/products/sensaform-maya-headboard/?sku=438520061'
        # 'https://www.bensonsforbeds.co.uk/products/silentnight-marina-headboard/?sku=556120021'
        # 'https://www.bensonsforbeds.co.uk/products/slumberland-rollo-hybrid-duo-rolled-mattress/?sku=759620001'
        # 'https://www.bensonsforbeds.co.uk/products/igel-advance-2500-plush-top-mattress/?sku=755120089'
        'https://www.bensonsforbeds.co.uk/products/simply-bensons-zander-memory-support-divan-bed-set/?sku=766420061'
        # 'https://www.bensonsforbeds.co.uk/products/edgemont-ottoman-wooden-bed-frame/?sku=AST135200'
        # 'https://www.bensonsforbeds.co.uk/products/slumberland-amari-ortho-comfort-divan-bed-set/'
        # 'https://www.bensonsforbeds.co.uk/products/slumberland-amari-ortho-comfort-mattress/?sku=STK766005'
    ]

    def parse(self, response):
        item = Bensonsforbeds()

        title = response.css('.productView-title.main-heading ::text').get()
        item['title'] = title

        description = response.css('#tab-description p ::text').getall()
        item['description'] = description

        img = response.css(".productView-images div img::attr(src)").get()
        item['img'] = img

        lst = []
        for i in response.css("[data-option-title]"):
            title = i.css("div ::attr(data-option-title)").getall()
            value = i.css(".form-option-variant ::text").getall() or i.css(
                ".form-option-variant ::attr(title)").getall()
            dict_data = dict(title=title, value=value)

            lst.append(dict_data)

        item['variants'] = lst

        price = response.css("[itemprop='offers'] .price ::text").get()
        old_price = response.css("[itemprop='offers'] .price--non-sale ::text").get().strip()
        new_price = response.css('.productView-price div span.price::text').get()

        if old_price and new_price:
            item['old_price'] = old_price
            item['new_price'] = new_price
        else:
            item['price'] = price

        # size_name = response.css("[data-option-title='Size'] span ::text").getall()
        # item['size_name'] = size_name

        # color_name = response.css("[class^='productView-options'] span::attr(title)").getall()
        # item['color_name'] = color_name

        # rating = response.css("[data-option-title='Firmness Rating'] span ::text").getall()
        # if rating:
        #     item['rating'] = rating

        # storage = response.css("[data-option-title='Storage'] span ::text").getall()
        # if storage:
        #     item['storage'] = storage

        yield item
