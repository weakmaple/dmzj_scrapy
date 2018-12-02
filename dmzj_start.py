from scrapy import cmdline
import sys
if __name__ == '__main__':
    manhua_url = input("请输入网址：").strip()
    manhua_names = input("请输入漫画名：").strip()
    cmdline.execute(str("scrapy crawl dmzj_spider -a manhua_url=%s -a manhua_names=%s"%(manhua_url,manhua_names)).split())
    # cmdline.execute(str("scrapy crawl dmzj_spider -a manhua_url=%s -a manhua_names=%s"%(sys.argv[1],sys.argv[2])).split())