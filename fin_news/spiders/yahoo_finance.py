import scrapy

class FinNewsSpider(scrapy.Spider):
    name = 'Latest_News'

    start_urls = [
        'https://finance.yahoo.com/quote/PD/news?p=PD'
    ]

    def parse(self, response):
        for news in response.xpath("//*[@id='latestQuoteNewsStream-0-Stream']/ul/li"):
            yield {
                'title': news.xpath(".//*[@id='latestQuoteNewsStream-0-Stream']/ul/li[4]/div/div/div[2]/h3/a/text()").get(),
                'link': news.xpath(".//*[@id='latestQuoteNewsStream-0-Stream']/ul/li[4]/div/div/div[2]/h3/a/@href").get(),
            }


