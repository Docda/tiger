import requests
from lxml import etree
import re


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


def get_cd_chinese():
    res = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/71a40e6197eef62c892ef85f422dc118.svg')
    html = '<body>' + res.content.decode('utf8') + '</body>'
    a = re.findall('textLength="336">(.*?)</textPath>', html)[0]
    b = re.findall('textLength="392">(.*?)</textPath>', html)[0]
    c = re.findall('textLength="308">(.*?)</textPath>', html)[0]
    d = re.findall('textLength="518">(.*?)</textPath>', html)[0]
    e = re.findall('textLength="378">(.*?)</textPath>', html)[0]
    f = re.findall('textLength="378">(.*?)</textPath>', html)[1]
    g = re.findall('textLength="434">(.*?)</textPath>', html)[0]
    h = re.findall('textLength="588">(.*?)</textPath>', html)[0]
    # print(h)
    i = re.findall('textLength="112">(.*?)</textPath>', html)[0]
    # print(a)
    x, y = css_info('cdl8rn')[0]
    x, y = int(x), int(y)
    # print('坐标', x, y)
    if y <= 46:
        chinese = a[x // 14]
        # print('文字：', a[xx // 12])
    elif y <= 89:
        chinese = b[x // 14]
        # print('文字：', b[xx // 12])
    elif y <= 134:
        chinese = c[x // 14]
        # print('文字：', c[xx // 12])
    elif y <= 179:
        chinese = d[x // 14]
        # print('文字：', d[xx // 12])
    elif y <= 227:
        chinese = e[x // 14]
        # print('文字：', e[xx // 12])
    elif y <= 259:
        chinese = f[x // 14]
        # print('文字：', f[xx // 12])
    elif y <= 306:
        chinese = g[x // 14]
        # print('文字：', g[xx // 12])
    elif y <= 245:
        chinese = h[x // 14]
        # print('文字：', h[xx // 12])
    else:
        chinese = i[x // 14]
        # print('数字：', i[xx // 12])
    print(chinese)


import lxml.html


def get_kphChinese():
    res = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1bf11c9be33e47ff876a99d1d9e38395.svg')
    html = '<body>' + res.content.decode('utf8') + '</body>'
    a = re.findall('textLength="492">(.*?)</textPath>', html)[0]
    b = re.findall('textLength="432">(.*?)</textPath>', html)[0]
    c = re.findall('textLength="480">(.*?)</textPath>', html)[0]
    d = re.findall('textLength="576">(.*?)</textPath>', html)[0]
    e = re.findall('textLength="432">(.*?)</textPath>', html)[1]
    f = re.findall('textLength="516">(.*?)</textPath>', html)[0]
    g = re.findall('textLength="456">(.*?)</textPath>', html)[0]
    h = re.findall('textLength="564">(.*?)</textPath>', html)[0]
    i = re.findall('textLength="324">(.*?)</textPath>', html)[0]
    j = re.findall('textLength="588">(.*?)</textPath>', html)[0]
    k = re.findall('textLength="492">(.*?)</textPath>', html)[1]
    l = re.findall('textLength="300">(.*?)</textPath>', html)[0]
    m = re.findall('textLength="312">(.*?)</textPath>', html)[0]
    n = re.findall('textLength="492">(.*?)</textPath>', html)[2]
    o = re.findall('textLength="432">(.*?)</textPath>', html)[2]
    p = re.findall('textLength="384">(.*?)</textPath>', html)[0]
    q = re.findall('textLength="432">(.*?)</textPath>', html)[3]
    r = re.findall('textLength="564">(.*?)</textPath>', html)[1]
    s = re.findall('textLength="420">(.*?)</textPath>', html)[0]
    t = re.findall('textLength="516">(.*?)</textPath>', html)[1]
    u = re.findall('textLength="588">(.*?)</textPath>', html)[1]
    v = re.findall('textLength="528">(.*?)</textPath>', html)[0]
    w = re.findall('textLength="372">(.*?)</textPath>', html)[0]
    x = re.findall('textLength="564">(.*?)</textPath>', html)[2]
    y = re.findall('textLength="324">(.*?)</textPath>', html)[1]
    z = re.findall('textLength="372">(.*?)</textPath>', html)[1]
    aa = re.findall('textLength="24">(.*?)</textPath>', html)[0]
    # print(a, b, c, d, e, f, g, h, j, k, l, n, m, o, p, q, r, s, t, u, v, w, x, y, z, aa)
    xx, yy = css_info('kphyjb')[0]
    xx, yy = int(xx), int(yy)
    # print('坐标', x, y)
    if yy <= 38:
        chinese = a[xx // 12]
        # print('文字：', a[xx // 12])
    elif yy <= 69:
        chinese = b[xx // 12]
        # print('文字：', b[xx // 12])
    elif yy <= 102:
        chinese = c[xx // 12]
        # print('文字：', c[xx // 12])
    elif yy <= 140:
        chinese = d[xx // 12]
        # print('文字：', d[xx // 12])
    elif yy <= 177:
        chinese = e[xx // 12]
        # print('文字：', e[xx // 12])
    elif yy <= 225:
        chinese = f[xx // 12]
        # print('文字：', f[xx // 12])
    elif yy <= 257:
        chinese = g[xx // 12]
        # print('文字：', g[xx // 12])
    elif yy <= 297:
        chinese = h[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 341:
        chinese = i[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 385:
        chinese = j[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 429:
        chinese = k[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 479:
        chinese = l[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 520:
        chinese = m[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 557:
        chinese = n[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 590:
        chinese = o[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 621:
        chinese = p[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 659:
        chinese = q[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 692:
        chinese = r[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 725:
        chinese = s[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 756:
        chinese = t[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 794:
        chinese = u[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 843:
        chinese = v[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 885:
        chinese = w[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 926:
        chinese = x[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 970:
        chinese = z[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 1010:
        chinese = y[xx // 12]
        # print('文字：', h[xx // 12])
    else:
        chinese = aa[xx // 12]
        # print('数字：', i[xx // 12])
    print(chinese)


get_cd_chinese()
# get_kphChinese()
