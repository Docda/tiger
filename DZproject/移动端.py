# coding=utf8
import json
import random
import re
import time

from getXY import get_XY
import requests
from lxml import etree

s = requests.session()


# 商铺列表
def get_shop_list():
    # 2000为商铺数量的估计值，还可以更大
    for d_range in range(0, 2000, 20):
        url = 'https://m.dianping.com/isoapi/module'
        headers = {'Host': 'm.dianping.com', 'Connection': 'keep-alive', 'Content-Length': '240', 'Pragma': 'no-cache',
                   'Cache-Control': 'no-cache', 'Origin': 'https://m.dianping.com',
                   'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36',
                   'Content-Type': 'application/json', 'Accept': '*/*',
                   'Referer': 'https://m.dianping.com/shoplist/1/search?from=m_search&keyword=%E4%B8%8A%E6%B5%B7%E7%BE%8E%E9%A3%9F&from_suggest=history',
                   'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                   'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; logan_custom_report=; switchcityflashtoast=1; dp_pwa_v_=cede7d743c680cf24367c7011286d76f3df2fce5; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; _tr.s=b6ImXVNmoXRBvSOG; m_flash2=1; source=m_browser_test_22; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; msource=seouser; no_app_installed=yes; chwlsource=seouser; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/Xz0xNTYwMjM5MjA3MTM1JmNhbGxiYWNrPVplcHRvMTU2MDIzOTIwNTcwOT46PDE1NjAyMzkyMDc1ODVdX1s="; _lxsdk_s=16b4576d644-a5e-288-5b2%7C%7C3407; logan_session_token=dbf8g6rot5us4qvgci7n'
                   }
        d = r'''{"pageEnName":"shopList","moduleInfoList":[{"moduleName":"mapiSearch","query":{"search":{"start":{start},"categoryId":0,"parentCategoryId":0,"locateCityid":0,"limit":20,"sortId":0,"cityId":1,"keyword":"上海美食","regionId":0,"maptype":0}}}]}'''.replace(
            '{start}', str(d_range))
        res = s.post(url, headers=headers, data=d.encode('utf8'), verify=False)
        if res.status_code == 200:
            try:
                json_data = json.loads(res.text)
                list_data = json_data['data']['moduleInfoList'][0]['moduleData']['data']['listData']['list']
                # print(list_data)
                if len(list_data) != 0:
                    for data in list_data:
                        # print(data)
                        # dishtags = data['dishtags']
                        name = data['name']
                        branchName = data['branchName']
                        b_id = data['id']
                        shop_url = 'https://m.dianping.com/shop/' + b_id
                        priceText = data['priceText']
                        yield name, branchName, shop_url, priceText, b_id
                else:
                    break
            except Exception as e:
                print('解析数据出错了', e)
        time.sleep(random.randint(1, 4))


headers2 = {'Host': 'm.dianping.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; logan_custom_report=; switchcityflashtoast=1; dp_pwa_v_=cede7d743c680cf24367c7011286d76f3df2fce5; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; _tr.s=b6ImXVNmoXRBvSOG; m_flash2=1; source=m_browser_test_22; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; msource=seouser; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/Xz0xNTYwMjM5MjA3MTM1JmNhbGxiYWNrPVplcHRvMTU2MDIzOTIwNTcwOT46PDE1NjAyMzkyMDc1ODVdX1s="; logan_session_token=j3ig8n8ta3vl8k8hsoq3; _lxsdk_s=16b4576d644-a5e-288-5b2%7C%7C5023'}

num_dict = {
    'ee53': '0',
    '1': '1',
    'e3a3': '2',
    'f759': '3',
    'f831': '4',
    'e96b': '6',
    'e7d4': '7',
    'f8d6': '8',
    'eb25': '9'
}


def get_num(n):
    for k in num_dict:
        if k in n:
            return num_dict[k]
    return '5'


headers3 = {'Host': 'm.dianping.com', 'Connection': 'keep-alive', 'Content-Length': '165', 'Pragma': 'no-cache',
            'Cache-Control': 'no-cache', 'Origin': 'https://m.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36',
            'Content-Type': 'application/json', 'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': '_lxsdk_cuid=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _lxsdk=1693c02dd8354-0019ba09c9125b-1333063-144000-1693c02dd84c8; _hc.v=e164282b-987f-c262-4b6e-83441815f9b7.1551490015; _dp.ac.v=1f54f2e1-9002-4914-bb3b-4f5d23f80218; ctu=555955555c34dcc24494a3a9709b38bb01f90b399fe68847869eb50b49ff1a2d; ua=Docda; aburl=1; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1555916661; thirdtoken=24a1ac97-df43-4c37-bedd-0df6ed27262d; dper=0287947a83172e76c190728dc116e2b00bc83119da7575df75711d07173dc3cad8ce91a54ff091a96549b399f141a9de2b06af12921b18d439b340e38264d9100d815da48b82640df4208b538c9fb0430df987bd12ef53f3ad6c9cd837b41a2d; ll=7fd06e815b796be3df069dec7836c3df; uamo=18000241280; cy=1; cye=shanghai; logan_custom_report=; switchcityflashtoast=1; dp_pwa_v_=cede7d743c680cf24367c7011286d76f3df2fce5; cityid=1; PHOENIX_ID=0a49aa33-16b40e3abba-2812a8; _tr.u=x1lerlKvlCRYnkdp; m_flash2=1; source=m_browser_test_22; default_ab=shop%3AA%3A4%7Cindex%3AA%3A1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/Xz0xNTYwMzA3NzY4NTk5JmNhbGxiYWNrPVplcHRvMTU2MDMwNzc2NjM2Mj46PDE1NjAzMDc3NjczMjRdX1s="; msource=seouser; no_app_installed=yes; logan_session_token=w3qrm0oljijl6ob65l5q; seouser_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A2%7Cmap%3AA%3A1%7Cshopdish%3AA%3A1%7Cdishlist%3AA%3A1; _lxsdk_s=16b4a636571-6f8-bac-725%7C1458064701%7C168'}


# 获取推荐菜信息
def get_recommend(shopId):
    url = 'https://m.dianping.com/isoapi/module'
    d = r'''{"moduleInfoList":[{"moduleName":"list","query":{"type":"listLoadMore","shopId":"{shop_id}","page":1,"pagesize":20,"userIds":[1458064701]}}],"pageEnName":"dishlist"}'''.replace(
        '{shop_id}', shopId)
    res = s.post(url, data=d, headers=headers3, verify=False)
    # print(shopId,res.text)
    if res.status_code == 200:
        try:
            json_data = json.loads(res.text)
            rec_dict = {}
            for d in json_data['data']['moduleInfoList'][0]['moduleData']['data']['list']:
                dishName = d['dishName']
                pric = d['price']
                # print(dishName,pric)
                rec_dict[dishName] = pric
            return rec_dict
        except Exception as e:
            return '暂无推荐菜'
    else:
        return '暂无推荐菜'


# 获取店铺详细信息
def shop_detail(name, branchName, shop_url, priceText, b_id):
    res = s.get(shop_url, headers=headers2)
    html = res.text
    # print(html)
    try:
        my_tree = etree.HTML(res.text)
        # 地址
        address = re.findall('"address":(.*?),', html)[0].replace('"', '')
        pointx, pointy, city = get_XY('上海市' + address)
        # 电话
        phoneNum = re.findall('"phoneNum"(.*?)}', html)[0].replace(':"', '').replace('"', '')
        # 评论数
        comment = re.findall('下载APP查看全部(.*?)条点评', html)[0]
        # 营业时间
        businessHour = my_tree.xpath('//div[@class="businessHour"]/text()')[0].strip().replace('\n', ' ')
        # print(name)
        dp_dict = get_recommend(b_id)
        # 类别
        shop_crumbs = my_tree.xpath('//div[@class="shop-crumbs"]//a/text()')
        star_icon = my_tree.xpath('//div[@class="star_icon"]/span[1]/@class')
        if len(star_icon) != 0:
            star = re.findall('star_(\d+)', star_icon[0])[0]
        else:
            star = '暂无评价'
        taste_one = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[1]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[1]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[1]/text() | //div[@class="description_type"]/div[@class="description"]/span[1]/text()')
        taste_two = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[1]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[1]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[1]/text() | //div[@class="description_type"]/div[@class="description"]/span[1]/text()')
        environment_one = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[2]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[2]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[2]/text() | //div[@class="description_type"]/div[@class="description"]/span[2]/text()')
        environment_two = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[2]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[2]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[2]/text() | //div[@class="description_type"]/div[@class="description"]/span[2]/text()')
        service_one = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[3]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[3]/span[3]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[3]/text() | //div[@class="description_type"]/div[@class="description"]/span[3]/text()')
        service_two = my_tree.xpath(
            '//div[@class="description_type"]/div[@class="description"]/span[3]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[3]/span[4]/text() | //div[@class="Multi-description-type"]/div[@class="Multi-description"]/span[3]/text() | //div[@class="description_type"]/div[@class="description"]/span[3]/text()')

        if len(taste_one) != 0:
            # print(111111,taste_one[0],1111,type(taste_one[0]))
            taste_num_one = get_num(str(taste_one))
            taste_num_two = get_num(str(taste_two))
            environment_num_one = get_num(str(environment_one))
            environment_num_two = get_num(str(environment_two))
            service_num_one = get_num(str(service_one))
            service_num_two = get_num(str(service_two))

            # print(name, taste_num_one, taste_num_two, environment_num_one, environment_num_two, service_num_one,
            #       service_num_two)
            if taste_num_one == '1':
                taste_num_one = '9'
            if environment_num_one == '1':
                environment_num_one = '9'
            if service_num_one == '1':
                service_num_one = '9'
            # 口味
            taste = taste_num_one + '.' + taste_num_two
            # 环境
            environment = environment_num_one + '.' + environment_num_two
            # 服务
            service = service_num_one + '.' + service_num_two
            # print(name, taste, environment, service)
            my_data = {
                "店名": name + branchName,
                '地址': address,
                '电话': phoneNum,
                '评价': {
                    '口味': taste,
                    '环境': environment,
                    '服务': service
                },
                '评论数': comment,
                '营业时间': businessHour,
                '推荐菜': dp_dict,
                '人均价格': priceText,
                '经度': pointy,
                '维度': pointx,
                '城市': city,
                '类别': str(shop_crumbs).replace("['", '').replace("']", '').replace("', '", '>'),
                '星级': ('.').join(star)
            }

        else:
            my_data = {
                "店名": name + (branchName),
                '地址': address,
                '电话': phoneNum,
                '评价': '暂无评价',
                '评论数': comment,
                '营业时间': businessHour,
                '推荐菜': dp_dict,
                '人均价格': priceText,
                '经度': pointy,
                '维度': pointx,
                '城市': city,
                '类别': str(shop_crumbs).replace("['", '').replace("']", '').replace("', '", '>'),
                '星级': ('.').join(star)
            }
        print(my_data)
    except Exception as e:
        print('店铺详情页出错了', e)


if __name__ == '__main__':
    for name, branchName, shop_url, priceText, b_id in get_shop_list():
        shop_detail(name, branchName, shop_url, priceText, b_id)
    # get_recommend('96133168')
