import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def get_XY(addr):
    url = 'https://apis.map.qq.com/jsapi?qt=geoc&addr={}&key=TMZBZ-S72K6-66ISB-ES3XG-CVJC6-HKFZG&output=jsonp&pf=jsapi&ref=jsapi'.format(
        addr)
    try:
        res = requests.get(url, headers=headers)
        # print(res.text)
        if res.status_code == 200:
            json_data = json.loads(res.text)

            if 'pointx' in json_data['detail']:
                # print(json_data['detail'])
                # print(1111111111,json.loads(json_data['detail']))
                city = json_data['detail']['city']
                pointx = json_data['detail']['pointx']
                pointy = json_data['detail']['pointy']
                print(pointx, pointy, city)
                return pointx, pointy, city
            else:
                return '', '', ''
        else:
            return '', '', ''
    except Exception as e:
        print('获取经纬度失败', e)
        return '', '', ''

get_XY('上海市太仓路181弄上海新天地北里15单元2-3层')