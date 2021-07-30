import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        items = QuoteItem()
        div_quote = response.css('div.quote')

        for quotes in div_quote:
            title = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tag = quotes.css('.tag::text').get()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = 'https://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        if QuoteSpider.page_number <= 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
