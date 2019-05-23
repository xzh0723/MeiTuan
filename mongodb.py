import pymongo
from config import *

class MongoDB():

    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client.meituan

    def save(self, item):
        if item.get('comment'):
            collection = 'comment'
        else:
            collection = 'store'
        try:
            if self.db[collection].insert(dict(item)):
                print('成功插入数据库')
        except Exception as e:
            print('插入数据库失败：', e.args)

if __name__ == '__main__':
    pass