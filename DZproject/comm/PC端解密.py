import requests
from lxml import etree
import re


# 获取css页面的详情信息，用正则匹配得到css的定位数据
def css_info(info):
    # css 页面   这个网址是会变化的，修改为自己获取到的
    # css_html = requests.get(
    #     'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/d9206ecf873d5b175823e9ba260803a0.css').text
    # mty2pe{background:-180.0px -1664.0px;}
    with open('./comm/css.txt', 'r', encoding='utf8', errors='ignore')as f:
        html = f.read()
    # 正则，这里有个坑，刚开始使用+拼接，不能匹配
    str_css = r'%s{background:-(\d+).0px -(\d+).0px' % info
    css_re = re.compile(str_css)
    info_css = css_re.findall(html)
    # print(css_html)
    # print(str_css)
    # print(info_css)
    # print(info_css)
    return info_css


def get_ug_chinese(class_name):
    with open('./comm/cd.html', 'r', encoding='utf8', errors='ignore')as f:
        html = f.read()
    # res = requests.get(
    #     'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/71a40e6197eef62c892ef85f422dc118.svg')
    # html = '<body>' + res.content.decode('utf8') + '</body>'
    a = re.findall('textLength="378">(.*?)</textPath>', html)[0]
    b = re.findall('textLength="392">(.*?)</textPath>', html)[0]
    c = re.findall('textLength="476">(.*?)</textPath>', html)[0]
    d = re.findall('textLength="588">(.*?)</textPath>', html)[0]
    e = re.findall('textLength="504">(.*?)</textPath>', html)[0]
    f = re.findall('textLength="462">(.*?)</textPath>', html)[0]
    g = re.findall('textLength="420">(.*?)</textPath>', html)[0]
    h = re.findall('textLength="224">(.*?)</textPath>', html)[0]
    # print(h)
    # i = re.findall('textLength="112">(.*?)</textPath>', html)[0]
    # print(a)
    x, y = css_info(class_name)[0]
    x, y = int(x), int(y)
    # print('坐标', x, y)
    if y <= 31:
        chinese = a[x // 14]
        # print('文字：', a[xx // 12])
    elif y <= 62:
        chinese = b[x // 14]
        # print('文字：', b[xx // 12])
    elif y <= 109:
        chinese = c[x // 14]
        # print('文字：', c[xx // 12])
    elif y <= 142:
        chinese = d[x // 14]
        # print('文字：', d[xx // 12])
    elif y <= 182:
        chinese = e[x // 14]
        # print('文字：', e[xx // 12])
    elif y <= 230:
        chinese = f[x // 14]
        # print('文字：', f[xx // 12])
    elif y <= 265:
        chinese = g[x // 14]
        # print('文字：', g[xx // 12])
    else:
        chinese = h[x // 14]
        # print('文字：', h[xx // 12])
    # print(chinese)
    return chinese


def get_kphChinese(class_name):
    with open('./comm/kph.html', 'r', encoding='utf8', errors='ignore')as f:
        html = f.read()
    # res = requests.get(
    #     'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1bf11c9be33e47ff876a99d1d9e38395.svg')
    # html = '<body>' + res.content.decode('utf8') + '</body>'
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
    xx, yy = css_info(class_name)[0]
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
    return chinese


def get_yxChinese(class_name):
    with open('./comm/xy.html', 'r', encoding='utf8', errors='ignore')as f:
        html = f.read()
    a = re.findall('y="36">(.*?)</text>', html)[0]
    b = re.findall('y="80">(.*?)</text>', html)[0]
    c = re.findall('y="125">(.*?)</text>', html)[0]
    d = re.findall('y="168">(.*?)</text>', html)[0]
    e = re.findall('y="218">(.*?)</text>', html)[0]
    f = re.findall('y="264">(.*?)</text>', html)[0]
    g = re.findall('y="312">(.*?)</text>', html)[0]
    h = re.findall('y="354">(.*?)</text>', html)[0]
    i = re.findall('y="394">(.*?)</text>', html)[0]
    j = re.findall('y="427">(.*?)</text>', html)[0]
    k = re.findall('y="468">(.*?)</text>', html)[0]
    l = re.findall('y="512">(.*?)</text>', html)[0]
    m = re.findall('y="559">(.*?)</text>', html)[0]
    n = re.findall('y="609">(.*?)</text>', html)[0]
    o = re.findall('y="647">(.*?)</text>', html)[0]
    p = re.findall('y="695">(.*?)</text>', html)[0]
    q = re.findall('y="728">(.*?)</text>', html)[0]
    r = re.findall('y="762">(.*?)</text>', html)[0]
    s = re.findall('y="805">(.*?)</text>', html)[0]
    t = re.findall('y="849">(.*?)</text>', html)[0]
    u = re.findall('y="884">(.*?)</text>', html)[0]

    xx, yy = css_info(class_name)[0]
    xx, yy = int(xx), int(yy)
    # print('坐标', x, y)
    if yy <= 36:
        chinese = a[xx // 12]
        # print('文字：', a[xx // 12])
    elif yy <= 80:
        chinese = b[xx // 12]
        # print('文字：', b[xx // 12])
    elif yy <= 125:
        chinese = c[xx // 12]
        # print('文字：', c[xx // 12])
    elif yy <= 168:
        chinese = d[xx // 12]
        # print('文字：', d[xx // 12])
    elif yy <= 218:
        chinese = e[xx // 12]
        # print('文字：', e[xx // 12])
    elif yy <= 264:
        chinese = f[xx // 12]
        # print('文字：', f[xx // 12])
    elif yy <= 312:
        chinese = g[xx // 12]
        # print('文字：', g[xx // 12])
    elif yy <= 354:
        chinese = h[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 394:
        chinese = i[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 427:
        chinese = j[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 468:
        chinese = k[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 512:
        chinese = l[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 559:
        chinese = m[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 609:
        chinese = n[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 647:
        chinese = o[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 695:
        chinese = p[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 728:
        chinese = q[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 762:
        chinese = r[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 805:
        chinese = s[xx // 12]
        # print('文字：', h[xx // 12])
    elif yy <= 849:
        chinese = t[xx // 12]
        # print('文字：', h[xx // 12])
    else:
        chinese = u[xx // 12]
        # print('文字：', h[xx // 12])
    # print(chinese)
    return chinese


def get_open_time(class_name):
    with open('./comm/open.html', 'r', encoding='utf8', errors='ignore')as f:
        html = f.read()
    a = re.findall('y="36">(.*?)</text>', html)[0]
    b = re.findall('y="73">(.*?)</text>', html)[0]
    c = re.findall('y="109">(.*?)</text>', html)[0]
    x, y = css_info(class_name)[0]
    x, y = int(x), int(y)
    # print('坐标', x, y)
    if y <= 36:
        chinese = a[x // 12]

    elif y <= 73:
        chinese = b[x // 12]

    else:
        chinese = c[x // 12]

    # print(chinese)
    return chinese


num_dict = {
    'ec2d': '0',
    'e4ff': '2',
    'f70d': '3',
    'e6ec': '4',
    'f404': '5',
    'e65d': '6',
    'e284': '7',
    'f810': '8',
    'e27b': '9'
}

week_dict = {
    'xe60b': '周',
    'xf009': '一',
    'xf865': '日',

}


def get_num(n):
    for k in num_dict:
        if n == k:
            return num_dict[k]
    return n


# 将列表的数字转换为链接在一起的正常数字
def get_detail_num(num_list):
    data_list = []
    for i in eval(str(num_list).replace(r'\u', '')):
        if i != ' ':
            data = get_num(str(i))
            data_list.append(data)
            # print(phone)

    my_data = str(data_list).replace("['", '').replace("']", '').replace("', '", '').replace(r'\xa0', ' ')
    return my_data

# get_ug_chinese()
# get_kphChinese()
# print(get_num('e4ff'))
# get_open_time('ggtgx')
# get_yxChinese('yxdfw')
