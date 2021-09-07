import scrapy


class Test_spider(scrapy.Spider):
    name = "test"
    start_urls = [
        # "https://www.cclonline.com/"
        "https://quotes.toscrape.com/"
        # "https://www.cheatsheet.com/"
    ]

    def parse(self, response):
        print(response.status)
