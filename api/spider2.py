#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:wefinger

import requests
import pymysql
import json
import time

def text(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    req_json = response.text
    print(req_json)
    yan_text = req_json.replace("'","\\\'")
    yan_text = yan_text.replace('"','\\\"')
    db = pymysql.connect("mysql.sunmiao.top", "yan", "sm80231314", charset="utf8")
    cursor = db.cursor()
    sql_select = "SELECT * FROM yan.text \
                  WHERE text = '%s'" %yan_text
    cursor.execute(sql_select)
    results = cursor.fetchall()

    if len(results):
        return '1'
    else:
        sql = "INSERT INTO `yan`.`text`(`text`) VALUES ('%s');" %yan_text
        cursor.execute(sql)
        db.commit()
        return '0'

i = 1
url1 = "https://v1.hitokoto.cn/?encode=text&charset=utf-8"
url2 = "http://yinshi.api.shkong.cc/mixture/full"
while 1:
    # map = text(url1)
    # if map == '0':
    #     print('第%s条写入成功' %str(i))
    # else:
    #     print('第%s条已存在' %str(i))

    map = text(url2)
    if map == '0':
        print('第%s条写入成功' %str(i))
    else:
        print('第%s条已存在' %str(i))
    i=i+1
