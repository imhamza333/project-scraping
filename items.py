# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html
#
import scrapy


class HypeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    description = scrapy.Field()
    size_cat = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()


class ClandItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    description = scrapy.Field()
    size_name = scrapy.Field()
    price = scrapy.Field()
    list_of_dict_one = scrapy.Field()
    brand_name = scrapy.Field()


class TayabItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    description_one = scrapy.Field()


class QuoteItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class Jbhifi(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    new_price = scrapy.Field()


class Bensonsforbeds(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    description = scrapy.Field()
    size_name = scrapy.Field()
    price = scrapy.Field()
    color_name = scrapy.Field()
    rating = scrapy.Field()
    storage = scrapy.Field()
    variants = scrapy.Field()


class Raidoshack(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    description = scrapy.Field()
    img = scrapy.Field()
    color_name = scrapy.Field()


class Adelanto(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    timing = scrapy.Field()
    data = scrapy.Field()


class Kabum(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    description = scrapy.Field()
    img = scrapy.Field()
    color_name = scrapy.Field()
    aggregateRating = scrapy.Field()
    item_id = scrapy.Field()
    breadcrumb = scrapy.Field()
    rating_Value = scrapy.Field()
    total_review = scrapy.Field()