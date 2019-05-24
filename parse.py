import time

def parse_store(item):
    store = {}
    field_map = {
        'title': 'title', 'address': 'address', 'frontImg': 'frontImg',
        'allCommentNum': 'allCommentNum', 'poiId': 'poiId', 'avgPrice': 'avgPrice', 'avgScore': 'avgScore'
    }
    for field, attr in field_map.items():
        store[field] = item[attr]
    return store

def parse_comment(item):
    comment = {}
    user = {}
    field_map = {
        'userName': 'userName', 'userId': 'userId', 'userUrl': 'userUrl', 'userLevel': 'userLevel'
    }
    for field, attr in field_map.items():
        user[field] = item[attr]
    comment['user'] = user
    field_map_ = {
        'comment': 'comment', 'menu': 'menu', 'merchantComment': 'merchantComment', 'readCnt': 'readCnt',
        'replyCnt': 'replyCnt', 'zanCnt': 'zanCnt', 'avgPrice': 'avgPrice',
    }
    for field, attr in field_map_.items():
        comment[field] = item[attr]
    # commentTime：13位时间戳转化为时间
    timestamp = float(int(item['commentTime']) / 1000)
    commentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    comment['commentTime'] = commentTime
    # dealEndtime: 10位时间戳转时间
    if item['dealEndtime']:
        timestamp = int(item['dealEndtime'])
        dealEndtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        comment['dealEndtime'] = dealEndtime
    return comment