import re
import requests
from config import *

def get_uuid():
    res = requests.get(originUrl, headers=HEADERS)
    uuid = re.search("uuid: '(.*?)',", res.text, re.S).group(1)
    # print(uuid)
    return uuid