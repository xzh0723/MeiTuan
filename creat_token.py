import base64
import zlib
from datetime import datetime
import json
from get_uuid import get_uuid
from config import *

class CreatToken():
    def __init__(self, page):
        self.page = page
        self.url = originUrl + 'pn{}/'.format(self.page)

    def get_sign(self):
        uuid = get_uuid()
        sign = f"areaId=0&cateId=17&cityName={cityName}&dinnerCountAttrId=&optimusCode=1&originUrl={self.url}&page={self.page}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid={uuid}"
        sign_ = zlib.compress(bytes(json.dumps(sign, ensure_ascii=False), encoding='utf-8'))
        sign_ = str(base64.b64encode(sign_), encoding='utf-8')
        # print(sign_)
        return sign_

    def get_token(self):
        sign = self.get_sign()
        ts = int(datetime.now().timestamp() * 1000)
        # print(ts)
        data = {
            'rId': 100900,
            'ver': '1.0.6',
            'ts': ts,
            'cts': ts + 100 * 1000,
            'brVD': [1326, 538],
            'brR': [[1326, 538], [1326, 538], 24, 24],
            'bI': ['https://chs.meituan.com/meishi/c17/pn3/', 'https://chs.meituan.com/meishi/c17/pn2/'],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'aM': '',
            'sign': sign
        }
        token_decode = zlib.compress(
            bytes(json.dumps(data, separators=(',', ':'), ensure_ascii=False), encoding="utf8"))
        token = str(base64.b64encode(token_decode), encoding="utf8")
        # print(token)
        return token

if __name__ =='__main__':
    pass

