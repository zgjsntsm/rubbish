import requests
import json
import base64

long_url = "https://solusvm.sora.top/remote.php?_v=u2w2y2p2d4c4j5x2k5"

long_url_base64 = base64.b64encode(long_url.encode(encoding="utf-8")).decode()
print(long_url_base64)

url = "http://dwz.wailian.work/api.php"
data = {
    'from':'w',
    'url':long_url_base64,
    'site':'sina'
}
cookie = "PHPSESSID=1t20vre4u3vf00e927orbtnun4; __51cke__=; Hm_lvt_fd97a926d52ef868e2d6a33de0a25470=1524718861,1524721117; Hm_lpvt_fd97a926d52ef868e2d6a33de0a25470=1524721117; __tins__19242943=%7B%22sid%22%3A%201524721117341%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201524722917341%7D; __51laig__=2"
headers = {
    'Accept':"application/json, text/javascript, */*; q=0.01",
    'Accept-Encoding':"gzip, deflate",
    'Accept-Language':"zh-CN,zh;q=0.9",
    'Connection':"keep-alive",
    'Cookie':cookie,
    'Host':"dwz.wailian.work",
    'Referer':"http://dwz.wailian.work/",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'X-Requested-With':"XMLHttpRequest"
}

print(url)

response = requests.get(url,params=data,headers=headers)
response.encoding = 'utf-8'
req_json = response.json()
print(req_json)
req = {
    'result':req_json['result'],
    'short_url':req_json['data']['short_url'],
    'title':req_json['data']['title']
}

print(req)