import scrapy
import re
from scrapy.selector import Selector
from jokesText.items import JokestextItem

class JokeSpider(scrapy.Spider):
  name = "joke"
  allowed_domains = ["qiushibaike.com"]

  start_urls = [
     "http://www.qiushibaike.com/textnew/page/1"
  ]

  def parse(self, response):
    page = Selector(response)

    url = response.url
    print url
    divs = page.xpath('//div[@class="article block untagged mb15"]')

    for div in divs:
      item = JokestextItem()

      content_list= div.xpath('.//div[@class="content"]/text()').extract()

      text = ""
      for string in content_list:
        string = string.strip()
        if len(string) > 0:
          text = text + "<br>" + string

      text = text[4:len(text)]
      text = text.encode('utf-8')
      item['content'] = text 
      print item['content']
      yield item

    button = page.xpath('//ul[@class="pagination"]')
    url_list = button.xpath('.//a/@href')[-1]
    next_page_url = "http://www.qiushibaike.com" + url_list.extract()

    yield scrapy.Request(next_page_url, callback = self.parse)