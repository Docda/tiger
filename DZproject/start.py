# -*- coding:utf-8 -*-


import scrapy.cmdline

def main():

    scrapy.cmdline.execute(["scrapy", "crawl", "dzSpider"])



if __name__ == '__main__':
    main()