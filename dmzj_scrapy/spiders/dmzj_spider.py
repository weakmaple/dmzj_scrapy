# -*- coding: utf-8 -*-
import scrapy
import re
import json
from dmzj_scrapy.items import DmzjScrapyItem
class DmzjSpiderSpider(scrapy.Spider):
    name = 'dmzj_spider'
    allowed_domains = ['m.dmzj.com']
    start_urls = ['http://m.dmzj.com/']

    def __init__(self,manhua_url=None, manhua_names=None,  *args, **kwargs):
        self.url = manhua_url
        self.manhua_name = manhua_names
        # print("="*40)
        # print(manhua_url)
        # print(manhua_names)
        # print("=" * 40)

    def start_requests(self):
        yield scrapy.http.Request(url=self.url, callback=self.first_url_parse)

    #将pc端网址装化为app端网址
    def first_url_parse(self,response):
        url = 'https://m.dmzj.com/info/%s.html'
        manhua_id_1 = response.xpath('//head/script/text()').get()
        manhua_id = re.search(r'.*?g_current_id = "(.*?)";.*',manhua_id_1).group(1)
        main_url = url % manhua_id
        # print(main_url)
        yield scrapy.http.Request(url=main_url, callback=self.parse_total)

    # 获得漫画的目录
    def parse_total(self,response):

        catalog = response.xpath('//body/script[@type="text/javascript"]/text()').getall()[1]
        catalog = re.sub(r'},{"title":.*?,"data":\[(.*?)\]', '', catalog)
        catalog_list = json.loads(re.search(r'"data":(.*?)}]\);.*',catalog).group(1))
        data_list = []
        for ls in catalog_list:
            #detail_url是每一话的地址
            detail_url = 'https://m.dmzj.com/view/%s/%s.html' % (ls['comic_id'],ls['id'])
            yield scrapy.http.Request(url=detail_url,callback=self.parse_detail)

    # 获得该话所有图片的url，再将这里的链接交给piplines处理
    def parse_detail(self,response):
        title = response.xpath('//a[@class="BarTit"]/text()').get()
        pic_urls = response.xpath('//body/script[@type="text/javascript"]/text()').getall()[1]
        pic_urls = json.loads(re.search(r'.*?"page_url":(.*?),"chapter_type".*', pic_urls).group(1))
        item = DmzjScrapyItem(pic_urls=pic_urls,title=title,big_title=self.manhua_name)
        yield item


