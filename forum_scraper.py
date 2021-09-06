#!/usr/bin/env python
"""forum_scraper.py this is a script to download and archive the first 10 pages of a 4 chan board"""
import scrapy
from scrapy.crawler import CrawlerProcess
import datetime as dt

class ThreadSpider(scrapy.Spider):
    """A spider Implementing the Scrapy Library
    generating asynchronous responses handled by the
    parse functino saving the data of each web page"""
    name = 'threads'
    def start_requests(self): 
        """method to initiate the requests for each page"""
        board_name = input('Please enter which board you want to archive!:\n')
        urls = [
            f'https://boards.4channel.org/{board_name}/{i}'
            for i in range(2,11)
        ]
        urls.append('https://boards.4channel.org/{board_name}/')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """saves the files"""
        page = response.url.split('/')[-1]
        board_name = response.url.split('/')[-2]
        date_time = dt.datetime.now().strftime('%d_%b_%Y_%H_%M')
        file_name = f'{board_name}_{page}_{date_time}.html'
        with open(file_name,'wb') as f:
            f.write(response.body)
def main():
    process = CrawlerProcess()
    process.crawl(ThreadSpider)
    process.start()


if __name__=='__main__':
    main()