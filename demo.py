# -*- coding:utf-8 -*-

"""
Updated at 14:20 at May 24,2019
@title: 美团店铺信息爬虫
@author: xzh0723
"""

import requests
import json
from mongodb import MongoDB
from config import *
from get_uuid import get_uuid
from parse import *
import math
from creat_token import CreatToken

def fetch(page):
    db = MongoDB()

    uuid = get_uuid()
    token = CreatToken(page).get_token()
    params = {
        'cityName': cityName,
        'cateId': type_,
        'areaId': '0',
        'sort': '',
        'dinnerCountAttrId': '',
        'page': page,
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
    items = result['data']['poiInfos']
    for item in items:
        # print(store)
        store = parse_store(item)
        # db.save(store)

        poiId = store['poiId']
        commentCount = store['allCommentNum']
        max_page = math.ceil(int(commentCount) / 10)
        comment_list = []
        for offset in range(max_page):
            params = {
                'uuid': get_uuid(),
                'id': poiId,
                'userId': '2490983615',
                'offset': offset * 10,
                'pageSize': '10',
            }

            resp = requests.get(comment_url, params=params, headers=HEADERS)
            # print(resp.text)
            result = json.loads(resp.text)
            items = result['data']['comments']
            for item in items:
                comment = parse_comment(item)
                print(comment)
                comment_list.append(comment)
        store['comment'] = comment_list
        print(store)
        db.save(store)

if __name__ == '__main__':
    max_page = input('请输入你要查询的最大页码：')
    for page in range(1, int(max_page) + 1):
        fetch(page)
