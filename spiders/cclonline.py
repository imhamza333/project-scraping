import scrapy
from ..items import Cclonline


class Cclonline_spider(scrapy.Spider):
    name = "cclonline"

    start_urls = [
        "https://www.cclonline.com/",
    ]

    # def start_requests(self):
    #     headers = {
    #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'accept-encoding': 'gzip, deflate, br',
    #         'accept-language': 'en-US,en;q=0.9,pl;q=0.8',
    #     }
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, meta={'proxy': 'https://51.79.166.87:8080'})


class ProxiesDownloaderMiddleware(object):

    def process_request(self, request):
        request.meta['proxy'] = 'https://51.79.166.87:8080'

    def parse(self, response, **kwargs):
        print(response.status)

    # allowed_domains = ['www.cclonline.com']
    # start_urls = ['https://www.cclonline.com/product/357751/MAG-X570S-TOMAHAWK-MAX-WIFI/Motherboards/MSI-MAG-X570S'
    #               '-TOMAHAWK-MAX-WIFI-Motherboard-ATX-AMD-Socket-AM4-X570-Chipset/MBD3124/']
    # handle_httpstatus_list = [403]
