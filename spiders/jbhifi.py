import scrapy
from ..items import Jbhifi


class JbhifiSpider(scrapy.Spider):
    name = 'jbhifi'
    start_urls = [
        'https://www.jbhifi.com.au/products/nintendo-switch-new-pokmon-snap'
        #'https://www.jbhifi.com.au/products/vinyl-muse-origin-of-symmetry-xx-anniversary-remixx-vinyl-lp'
        # 'https://www.jbhifi.com.au/products/cd-bts-butter-cd'
        # 'https://www.jbhifi.com.au/products/garmin-fenix-6x-pro-sports-watch-black'
        # 'https://www.jbhifi.com.au/products/google-nest-mini-coral-red'
        # 'https://www.jbhifi.com.au/products/eufy-wire-free-hd-security-cam-with-home-base-kit-4-cameras'
        # 'https://www.jbhifi.com.au/products/segway-ninebot-kickscooter-e22-folding-electric-scooter'
        # 'https://www.jbhifi.com.au/products/dell-g5-special-edition-15-6-full-hd-120hz-gaming-laptop-512gb-ryzen-9'
        # 'https://www.jbhifi.com.au/products/samsung-galaxy-buds-live-mystic-black'
        # 'https://www.jbhifi.com.au/products/fitbit-versa-3-black-black-aluminium'
        # 'https://www.jbhifi.com.au/products/garmin-fenix-6x-pro-sports-watch-black'
    ]

    def parse(self, response):
        item = Jbhifi()

        title = response.css('h1[itemprop="name"]::text').get()
        item['title'] = title

        description = response.css('.descriptions p ::text').getall()
        if description:
            item['description'] = description
        else:
            None

        img = response.css(".gallery-image img::attr(data-src)").getall()
        item['img'] = img

        price = response.css('.price::text').get()
        new_price = response.css('.sale::text').get()
        old_price = response.css('.savings s::text').get()

        if old_price:
            item['old_price'] = old_price
            item['new_price'] = new_price
        else:
            item['price'] = price

        yield item
