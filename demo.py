import requests
from mongodb import MongoDB
from config import *
from get_uuid import get_uuid
from parse import *
import math
from creat_token import CreatToken
from multiprocessing import Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor

def fetch(page):
    db = MongoDB()

    uuid = get_uuid()
    token = CreatToken(page).get_token()
    params = {
        'cityName': '长沙',
        'cateId': '17',
        'areaId': '0',
        'sort': '',
        'dinnerCountAttrId': '',
        'page': '1',
        'userId': '',
        'uuid': uuid,
        'platform': '1',
        'partner': '126',
        'originUrl': originUrl + 'pn{}/'.format(page),
        'riskLevel': '1',
        'optimusCode': '1',
        '_token': token
    }

    res = requests.get(base_url, params=params, headers=HEADERS)
    result = json.loads(res.text)
    stores = result['data']['poiInfos']
    for store in stores:
        print(store)
        db.save(store)

        poiId = store['poiId']
        commentCount = store['allCommentNum']
        max_page = math.ceil(int(commentCount) / 10)
        for offset in range(max_page):
            params = {
                'uuid': get_uuid(),
                #    'platform': '1',
                #    'partner': '126',
                #    'originUrl': 'https://www.meituan.com/meishi/163284684/',
                #    'riskLevel': '1',
                #    'optimusCode': '1',
                'id': poiId,
                'userId': '2490983615',
                'offset': offset * 10,
                'pageSize': '10',
                #    'sortType': '1'
            }

            resp = requests.get(comment_url, params=params, headers=HEADERS)
            print(resp.text)
            result = json.loads(resp.text)
            comments = result['data']['comments']
            for comment in comments:
                print(comment)
                db.save(comment)

MAX_WORKER_NUM = cpu_count()

if __name__ == '__main__':
    #pool = Pool(MAX_WORKER_NUM)
    # pool = ProcessPoolExecutor()
    for page in range(1, 2):
        fetch(page)
    #    pool.apply_async(fetch, args=(page, ))
    #pool.close()
    #pool.join()