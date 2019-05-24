HEADERS = {
    'Cookie': '_lxsdk_cuid=16acb846703c8-008366d74aeda5-7a1b34-100200-16acb846703c8; client-id=918956e6-105b-4ca5-8968-89e93fb32be0; _hc.v=1910edeb-2eb7-a3c5-41ff-2a64d0eaf25e.1558451373; mtcdn=K; iuuid=49894D73803B6C7A56246D5EA9CE5D36334A7B19F721BDD32DA94E4F042CA7EC; _lxsdk=49894D73803B6C7A56246D5EA9CE5D36334A7B19F721BDD32DA94E4F042CA7EC; webp=1; __utmz=74597006.1558621239.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); uuid=4c097d9a35874d9bb55b.1558633426.1.0.0; rvct=20%2C70%2C45; __utma=74597006.1501988102.1558621239.1558621239.1558633443.2; latlng=28.266892,113.070056,1558633442917; ci=70; cityname=%E9%95%BF%E6%B2%99; i_extend=H__a100001__b2; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; __mta=150257289.1558192631632.1558619209734.1558663121852.7; _lxsdk_s=16ae78fc7cc-688-efb-c45%7C%7C4',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Mobile Safari/537.36'
}

originUrl = 'https://chs.meituan.com/meishi/c17/'
base_url = 'https://chs.meituan.com/meishi/api/poi/getPoiList?'
comment_url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?'

cityName = input('请输入你要查询的城市：')

MONGO_URI = 'localhost'
MONGO_PORT = 27017
