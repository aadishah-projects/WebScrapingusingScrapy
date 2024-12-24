import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com/"]

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"

        # Save the content as files
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        a = response.css(".product_pod")
        
        for item in a:
            title = item.css("h3>a::text").get()
            image = item.css(".image_container img")
            rating = item.css(".star-rating").attrib["class"]
            price = item.css(".price_color::text").get()
            stock = item.css(".availability")
            print(image.attrib['src'])
            print(title)
            print(rating.split(" ")[-1])
            print(price)
            print(stock)