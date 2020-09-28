import scrapy
from fin_news.items import FinNewsItem
class FinNewsSpider(scrapy.Spider):
    name = 'Latest_News'

    start_urls = [
        'https://finance.yahoo.com/quote/PD/news?p=PD'
    ]

    def parse(self, response):
        for news in response.xpath(".//*[@id='latestQuoteNewsStream-0-Stream']/ul/li"):
            item = FinNewsItem()
            item['title'] = news.xpath(".//div/div/div/h3//text()").getall()
            item['link'] = news.xpath(".//div/div/div/h3/a/@href").getall()
            yield item

#.//*[@id='latestQuoteNewsStream-0-Stream']/ul/li/div/div/div/h3//text() - title xpath from shell
#.//*[@id='latestQuoteNewsStream-0-Stream']/ul/li/div/div/div/h3/a/@href - link xpath from shell