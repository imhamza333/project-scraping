import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        print(response.status)

