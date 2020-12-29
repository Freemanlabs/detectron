import scrapy
import re
from bs4 import BeautifulSoup


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    # allowed_domains = ['example.com']
    autothrottle_enabled = True

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        "FEEDS": {"json/search_result.json": {"format": "json"}},
    }

    def __init__(self, urls):
        self.start_urls = urls

    def start_requests(self):
        print("Scraping urls...")
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.body.get_text()
        # if re.search("\n", text):
        #     text = re.sub("\n", "", text)

        yield {"text": text}
