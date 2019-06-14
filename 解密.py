import re
import requests
import lxml.html
from lxml import etree
import ssl


# 获取css页面的详情信息，用正则匹配得到css的定位数据
def css_info(info):
    # css 页面   这个网址是会变化的，修改为自己获取到的
    css_html = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/d9206ecf873d5b175823e9ba260803a0.css').text
    # mty2pe{background:-180.0px -1664.0px;}
    # 正则，这里有个坑，刚开始使用+拼接，不能匹配
    str_css = r'%s{background:-(\d+).0px -(\d+).0px' % info
    css_re = re.compile(str_css)
    info_css = css_re.findall(css_html)
    # print(css_html)
    # print(str_css)
    # print(info_css)
    # print(info_css)
    return info_css


def get_num():
    # 这个链接为数字图片的链接
    res = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/71a40e6197eef62c892ef85f422dc118.svg')
    tree = lxml.html.fromstring(res.content)
    a = tree.xpath('//text[@y="32"]/text()')[0]
    b = tree.xpath('//text[@y="63"]/text()')[0]
    c = tree.xpath('//text[@y="98"]/text()')[0]
    d = tree.xpath('//text[@y="147"]/text()')[0]

    # x ,y 是得到的两个坐标点
    # 调用上面的函数
    x, y = css_info('cdlk7k')[0]
    x, y = int(x), int(y)

    print('坐标', x, y)
    # 这个14是根据css样式算出来的，后期出错很可能是这个改变了
    if y <= 32:
        print('数字：', a[x // 14])
    elif y <= 63:
        print('数字：', b[x // 14])
    elif y <= 98:
        print('数字：', c[x // 14])
    else:
        print('数字：', d[x // 14])


import re


def get_chinese():
    res = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/71a40e6197eef62c892ef85f422dc118.svg')
    # tree = lxml.html.fromstring(res.content)
    # print(res.content.decode('utf8'))
    html='<body>'+res.content.decode('utf8')+'</body>'
    # my_tree=etree.HTML(html.replace('<svg>','').replace('</svg>',''))
    #
    # tree=my_tree.xpath('//text[@lengthAdjust="spacing"]/text()')
    # print(tree)
    a=re.findall('textLength="336">(.*?)</textPath>',html)[0]
    b=re.findall('textLength="392">(.*?)</textPath>',html)[0]
    c=re.findall('textLength="308">(.*?)</textPath>',html)[0]
    d=re.findall('textLength="518">(.*?)</textPath>',html)[0]
    e=re.findall('textLength="378">(.*?)</textPath>',html)[0]
    f=re.findall('textLength="378">(.*?)</textPath>',html)[1]
    g=re.findall('textLength="434">(.*?)</textPath>',html)[0]
    h=re.findall('textLength="588">(.*?)</textPath>',html)[0]
    # print(h)
    i=re.findall('textLength="112">(.*?)</textPath>',html)[0]
    # print(a)
    x, y = css_info('cdlk7k')[0]
    x, y = int(x), int(y)
    # print('坐标', x, y)
    if y <= 308:
        print('文字：', c[x // 12])

    elif y <= 336:
        print('文字：', a[x // 12])

    elif y <= 378:
        print('文字：', e[x // 12])
    elif y <= 378:
        print('文字：', f[x // 12])
    elif y <= 392:
        print('文字：', b[x // 12])
    elif y <= 434:
        print('文字：', g[x // 12])
    elif y <= 518:
        print('文字：', d[x // 12])
    elif y <= 588:
        print('文字：', h[x // 12])
    else:
        print('数字：', i[x // 12])



get_chinese()
# get_num()

'''
    移动端 shop-detail
'''
