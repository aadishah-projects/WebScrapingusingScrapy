import scrapy
from pathlib import Path
from pymongo import MongoClient
import datetime



client = MongoClient("mongodb+srv://adityakshah66:GJU7ErWveUkQYfI0@cluster0.8blwv.mongodb.net/")
db = client.scrapy

def InsertToDb(page,title,imagesrc, rating, price):
    posts = db[page] #Database name
    doc = {
        "title": title,
        "imagesrc": imagesrc,
        "rating": rating,
        "price" : price,
        "date": datetime.datetime.now(tz=datetime.timezone.utc)
    }
    post_id  = posts.insert_one(doc).inserted_id
    return post_id

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
            image = image.attrib['src']
            rating = item.css(".star-rating").attrib["class"]
            rating = rating.split(" ")[-1]
            price = item.css(".price_color::text").get()
            stock = item.css(".availability")
            # print(image.attrib['src'])
            # print(title)
            # print(rating.split(" ")[-1])
            # print(price)
            # print(stock)
            InsertToDb(page,title,image, rating, price)