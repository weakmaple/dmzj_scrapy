# -*- coding: utf-8 -*-

# from selenium import webdriver
# import scrapy
# import time
#
# class DmzjScrapyDownloaderMiddleware(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def process_request(self, request, spider):
#         self.driver.get(request.url)
#         time.sleep(2)
#         source = self.driver.page_source
#         # source = b'%s' % (source)
#         return scrapy.http.HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')