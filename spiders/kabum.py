import scrapy
import json
from ..items import Kabum


class Kabum_Spider(scrapy.Spider):
    name = "kabum"
    start_urls = {
        "https://kabum.com.br/produto/129451/processador-amd-ryzen-5-5600x-cache-35mb-3-7ghz-4-6ghz-max-turbo-am4-100"
        "-100000065box "
        # "https://kabum.com.br/produto/135291/mem-ria-ram-crucial-ballistix-8gb-ddr4-2666-mhz-cl16-udimm"
        # "-preto-bl8g26c16u4b "
        # "https://kabum.com.br/produto/114929/tablet-samsung-galaxy-tab-s6-lite-4g-bluetooth-android-10-0-64gb-8mp"
        # "-tela-de-10-4-cinza-sm-p615nzavzto "

    }

    def parse(self, response):
        item = Kabum()

        json_string = response.xpath('//script[@type="application/ld+json"]//text()').get()
        json_string_one = response.xpath('//script[@type="application/json"]//text()').get()
        json_string_two = response.xpath('//script[@id="__NEXT_DATA__"]//text()').get()

        json_str = json.loads(json_string, strict=False)
        json_str_one = json.loads(json_string_one, strict=False)
        json_str_two = json.loads(json_string_two, strict=False)

        old_price = json_str_one["props"]["initialProps"]["pageProps"]["productData"]["priceDetails"]["price"]
        new_price = response.css("#blocoValores h4 ::text").get()
        breadcrumb = json_str_two["props"]["initialProps"]["pageProps"]["productData"]["category"]
        rating_value = json_str["aggregateRating"]["ratingValue"]
        total_review = json_str["aggregateRating"]["reviewCount"]
        img = response.css(".selectedImage img::attr(src)").get()
        product_id = json_str["sku"]
        title = json_str["name"]
        description = json_str["description"]

        item["total_review"] = total_review
        item["rating_Value"] = rating_value
        item['breadcrumb'] = breadcrumb
        item['old_price'] = old_price
        item['new_price'] = new_price
        item["description"] = description
        item["title"] = title
        item["item_id"] = product_id
        item['img'] = img

        return item
