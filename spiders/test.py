import scrapy


class ProxiesDownloaderMiddleware(scrapy.Spider):
    name = "test"
    start_urls = [
        # "https://www.cclonline.com/"
        "https://quotes.toscrape.com/"
    ]

    def process_request(self, request):
        request.meta['proxy'] = "http://192.168.1.1:8050"

    def parse(self, response):
        print(response.status)
