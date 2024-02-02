import scrapy
from time import sleep

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
QuotesSpider = None
            
url = "https://twitter.com/elonmusk"
tweet_class_string = 'css-175oi2r r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l'
text_class_string = 'css-175oi2r r-18u37iz r-1udh08x r-i023vh r-1qhn6m8 r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21'
class MyTwitterSpider(scrapy.Spider):
    name = 'tweets'
    start_urls = [ url ]
    
    def parse(self, body):
        
        
        for tweet in body.css(f'div.{tweet_class_string}'):
            yield {
                "text" : tweet.css(f"article.{text_class_string}").get()
            }
            
        # next_page = body.css('id.next-page')
        # if next_page is not None:
        #     yield body.follow(next_page, self.parse)