# -*- coding: utf-8 -*-
import scrapy
import json
import random
import re
from comm.PC端解密 import get_num, get_detail_num, get_ug_chinese, get_kphChinese, get_open_time, get_yxChinese


class DzspiderSpider(scrapy.Spider):
    name = 'dzSpider'
    allowed_domains = []
    start_urls = ['http://m.dianping.com/']

    headers = {'Host': 'www.dianping.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; switchcityflashtoast=1; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; m_flash2=1; source=m_browser_test_22; visitflag=0; pvhistory=6L+U5ZuePjo8L3NzbmV3P2tleXdvcmQ9JUU0JUI4JThBJUU2JUI1JUI3JUU3JUJFJThFJUU5JUEzJTlGJl89MTU2MDMyNDg2MzMyMSZjYWxsYmFjaz1aZXB0bzE1NjAzMjQ4NTEwNTY+OjwxNTYwMzI0ODYxNzU0XV9b; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1%7Cshopdish%3AA%3A1%7Cdishlist%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; msource=default; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1%7Cdishlist%3AA%3A1; _lxsdk_s=16b4f73d72e-9c-857-368%7C%7C527'}

    headers2 = {'Host': 'www.dianping.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; switchcityflashtoast=1; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; m_flash2=1; source=m_browser_test_22; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1; visitflag=0; pvhistory=6L+U5ZuePjo8L3NzbmV3P2tleXdvcmQ9JUU0JUI4JThBJUU2JUI1JUI3JUU3JUJFJThFJUU5JUEzJTlGJl89MTU2MDMyNDg2MzMyMSZjYWxsYmFjaz1aZXB0bzE1NjAzMjQ4NTEwNTY+OjwxNTYwMzI0ODYxNzU0XV9b; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1%7Cshopdish%3AA%3A1%7Cdishlist%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16b4b0732eb-a97-347-553%7C1458064701%7C9'}

    def start_requests(self):
        # 抓取全部数据50页
        # for i in range(1, 51):
        for i in range(1, 2):
            url = 'http://www.dianping.com/search/keyword/1/0_%E4%B8%8A%E6%B5%B7%E7%BE%8E%E9%A3%9F/p{}'.format(str(i))
            yield scrapy.Request(url, headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        shop_list = response.xpath('//div[@id="shop-all-list"]/ul/li')
        for sh in shop_list:
            shop_name = sh.xpath('./div[2]/div[1]/a/@title').get()
            shop_url = sh.xpath('./div[2]/div[1]/a/@href').get()
            shop_id = re.findall('shop/(\d+)', shop_url)[0]
            # print(shop_name, shop_url, shop_id)
            # yield shop_name, shop_url, shop_id
            request = scrapy.Request(shop_url, headers=self.headers2, callback=self.parse_item)
            request.meta['shop_name'] = shop_name
            request.meta['shop_url'] = shop_url
            request.meta['shop_id'] = shop_id
            yield request

    def parse_item(self, response):
        shop_name = response.meta['shop_name']
        shop_url = response.meta['shop_url']
        shop_id = response.meta['shop_id']
        if response.status == 200:
            try:
                # 电话
                phone_tree_list = response.xpath(
                    '//p[contains(@class,"expand-info") and contains(@class,"tel")]/text() | //p[contains(@class,"expand-info") and contains(@class,"tel")]//d/text()').extract()
                phoneNum = get_detail_num(phone_tree_list)
                # 星数
                start = response.xpath('//div[@class="brief-info"]/span[1]/@title')[0]
                start = str(start).replace("""<Selector xpath='//div[@class="brief-info"]/span[1]/@title' data='""",
                                           '').replace("'>", '')
                # 评论数
                comment_num_list = response.xpath(
                    '//span[@id="reviewCount"]/text() | //span[@id="reviewCount"]/d/text()').extract()
                commentNum = get_detail_num(comment_num_list)
                # 人均
                avgPriceTitle = response.xpath(
                    '//span[@id="avgPriceTitle"]/text() | //span[@id="avgPriceTitle"]/d/text()').extract()
                price = get_detail_num(avgPriceTitle)
                # 口味
                taste_num_list = response.xpath(
                    '//span[@id="comment_score"]/span[1]/text() | //span[@id="comment_score"]/span[1]/d/text()').extract()
                taste = get_detail_num(taste_num_list)
                # 环境
                environment_list = response.xpath(
                    '//span[@id="comment_score"]/span[2]/text() | //span[@id="comment_score"]/span[2]/d/text()').extract()
                environment = get_detail_num(environment_list)
                # 服务
                service_list = response.xpath(
                    '//span[@id="comment_score"]/span[3]/text() | //span[@id="comment_score"]/span[3]/d/text()').extract()
                service = get_detail_num(service_list)
                # 地址
                address_list = response.xpath(
                    '//span[@id="address"]/text() | //span[@id="address"]/e/@class | //span[@id="address"]/d/text()').extract()
                # print(address_list)
                add = []
                for j in address_list:
                    # 地址文字和营业时间文字是不一样的，而且每天会变
                    if 'ug' in j:
                        address = get_ug_chinese(j)
                        add.append(address)
                        # print(address)
                    else:
                        address = get_num(str(j).replace(r'\u', ''))
                        add.append(address)
                        # print(address)
                # 地址
                add = get_detail_num(add)
                # 类别
                breadcrumb = response.xpath('//div[@class="breadcrumb"]//a/text()').get().replace("['", '').replace(
                    "']",
                    '').replace(
                    "', '", '>')
                # 营业时间
                open_time_list = response.xpath(
                    '//p[contains(@class,"info") and contains(@class,"info-indent")]/span[2]/text() | //p[contains(@class,"info") and contains(@class,"info-indent")]/span[2]/svgmtsi/@class').extract()
                time_list = []
                for n in open_time_list[6:]:
                    if 'gg' in n:
                        o_time = get_open_time(n)
                        time_list.append(o_time)
                    else:
                        time_list.append(n)

                open_time = str(time_list).replace("['", '').replace("']", '').replace("', '", '')
                # recommend_dict = get_recommend(shop_id) # todo 1
                # print(open_time)
                # print(phoneNum, start, commentNum, price, taste, environment, service, breadcrumb, add)
                my_data = {
                    "店名": shop_name,
                    "链接": shop_url,
                    'ID': shop_id,
                    '地址': add,
                    '电话': phoneNum,
                    '评价': {
                        '口味': taste.replace('口味:', ''),
                        '环境': environment.replace('环境:', ''),
                        '服务': service.replace('服务:', '')
                    },
                    '评论数': commentNum,
                    '营业时间': open_time.replace('shopdesc', ''),  # 这个可以根据时间类名进行修改
                    # '推荐菜': recommend_dict, # todo 下一步在获取
                    '人均价格': price,
                    # '经度': pointy,
                    # '维度': pointx,
                    # '城市': city,
                    '类别': breadcrumb,
                    '星级': start
                }
                # print(my_data)

                # 获取 推荐菜
                url = 'http://www.dianping.com/ajax/json/shopDynamic/shopTabs?shopId={}&cityId=1&shopName=%E4%B8%80%E5%BF%83%E7%89%9B%E7%83%A7%E8%82%89%E6%94%BE%E9%A2%98%E4%B8%93%E9%97%A8%E5%BA%97&power=5&mainCategoryId=224&shopType=10&shopCityId=1&_token=eJxV0Utv4jAQAOD%2F4mst4sd47HBb0pa2u4AKaQRFHHgGRJOmJG2A1f73naQBqaf5POMZ2%2FJfdnhcsbYUQoDk7Gt9YG0mW6KFjLMip4pBqiD41gJytvyRc9r4nC0O0S1rTxEFtwpnVWJI66k0GrlDmPGGiqiAV4EtHmkL2xZF1va8sixbq908zXZp3Fq%2BJ16%2Bfc88qcCgttqnqzBqScKqBYzgaDXlwBiSqoUkWckqjuZbVAVXy5GgkqNeELUkx3oyOHUVkOxV9RRHkxVcpRoZ378Kmg6DrjnDKHuRvNzAiIvgu9dqDlJXD9tXD6M4b2JxWffoM2hrvotT0vrpGI5yyD82w14eRi8noXvnh%2F7gz91b%2F3xyQTCMX5N5HJmndXpfJPOPbZSazhJKf9QZBEF3P0myZNE1%2BSialIE79v2xOk2wm3mfi1RvBpsCnXcXhcb2shsJn8nX%2Ff54MxoLuXQ6fFkdAtznu9tIFp1fwXMQxuffY%2FbvP%2BPjkG8%3D&uuid=e164282b-987f-c262-4b6e-83441815f9b7.1551490015&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2F124563739'.format(
                    shop_id)
                headers3 = {'Host': 'www.dianping.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache', 'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'X-Requested-With': 'XMLHttpRequest',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                            'Referer': 'http://www.dianping.com/shop/{}'.format(str(shop_id)),
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                            'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; switchcityflashtoast=1; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; m_flash2=1; source=m_browser_test_22; visitflag=0; pvhistory=6L+U5ZuePjo8L3NzbmV3P2tleXdvcmQ9JUU0JUI4JThBJUU2JUI1JUI3JUU3JUJFJThFJUU5JUEzJTlGJl89MTU2MDMyNDg2MzMyMSZjYWxsYmFjaz1aZXB0bzE1NjAzMjQ4NTEwNTY+OjwxNTYwMzI0ODYxNzU0XV9b; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1%7Cshopdish%3AA%3A1%7Cdishlist%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; msource=default; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1%7Cdishlist%3AA%3A1; _lxsdk_s=16b4f73d72e-9c-857-368%7C%7C442'}
                yield scrapy.Request(url, meta={'my_data': my_data}, headers=headers3, callback=self.get_recommend)

            except Exception as e:
                print('需要更换cookie', e)
        else:
            print('需要更换cookie')

    # 获取推荐菜信息
    def get_recommend(self, response):
        my_data = response.meta['my_data']
        if response.status == 200:
            try:
                allDishes = json.loads(response.text)['allDishes']
                d_dict = {}
                for d in allDishes:
                    m_list = []
                    dishTagName = d['dishTagName']
                    finalPrice = d['finalPrice']
                    d_class = re.findall('class="(.*?)">', dishTagName)
                    for m in d_class:
                        m_name = get_yxChinese(m)
                        m_list.append(m_name)
                    d_dict[str(m_list).replace("['", '').replace("']", '').replace("', '", '')] = finalPrice
                # print(d_dict)
                my_data['推荐菜'] = d_dict
                # 获取全部内容
                print('全部的菜谱内容：', my_data)

            except Exception as e:
                return '暂无推荐菜'
        else:
            return '暂无推荐菜'
