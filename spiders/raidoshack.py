import scrapy
from ..items import Raidoshack


class Raidoshack_spider(scrapy.Spider):
    name = 'raidoshack'
    start_urls = [
        'https://www.radioshack.com/collections/forehead-thermometers/products/non-contact-infrared-thermometer'
        # 'https://www.radioshack.com/collections/power-banks/products/ks501-blk-keysmart-ultimate-charger-portable-multi-device-power-bank-65w-pd'
        # 'https://www.radioshack.com/collections/power-banks/products/flibank-boost-2900-mah-purple'
        # 'https://www.radioshack.com/collections/cleaners-and-chemicals/products/precision-electronics-cleaner'
        # 'https://www.radioshack.com/collections/cleaners-and-chemicals/products/deoxit-d5s-6-spray-contact-cleaner-and-rejuvenator'
        # 'https://www.radioshack.com/collections/electronics/products/lexon-mino-l-bluetooth-speaker-with-passive-bass-system'
        # 'https://www.radioshack.com/collections/electronics/products/auvio-wireless-stereo-headphones'
        # 'https://www.radioshack.com/collections/electronics/products/auvio-wireless-stereo-headphones'
        # 'https://www.radioshack.com/collections/electronics/products/radioshack-am-fm-digital-headset-radio'
        # 'https://www.radioshack.com/collections/earbuds-and-in-ear-headphones/products/kanex-goplay-wireless-sport-headphones-black'
        # 'https://www.radioshack.com/collections/earbuds-and-in-ear-headphones/products/trend-tech-fun-buds-pro-fashion-stereo-bluetooth-tws-earbuds-with-built-in-mic-and-charging-case'
        # 'https://www.radioshack.com/collections/earbuds-and-in-ear-headphones/products/trend-tech-fun-buds-pro-fashion-stereo-bluetooth-tws-earbuds-with-built-in-mic-and-charging-case'
        # 'https://www.radioshack.com/collections/drones-rc-toys/products/dumpin-moto'
        # 'https://www.radioshack.com/collections/hot-products/products/radioshack-am-fm-digital-headset-radio'
    ]

    def parse(self, response):
        item = Raidoshack()

        title = response.css('.product_title::text').get()
        item['title'] = title

        description = response.css('[id$="pr_description"] p::text').getall()
        item['description'] = description

        img = response.css("[data-mdtype='image'].img_ptw ::attr(data-src)").getall()
        if img:
            item['img'] = img

        color_name = response.css("[data-opname='color'] li ::text").getall()
        if color_name:
            item['color_name'] = color_name

        old_price = response.css('.price_range del::text').get()
        new_price = response.css('.price_range ins::text').get()
        price = response.css('.price_range::text').get()

        if old_price and new_price:
            item['old_price'] = old_price
            item['new_price'] = new_price
        else:
            item['price'] = price

        yield item
