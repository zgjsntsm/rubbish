#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:wefinger

import requests
import pymysql
import json
import time

def text():
    url = "https://api.yum6.cn/yan.php?format=json"

    response = requests.get(url)
    response.encoding = 'utf-8'
    req_json = response.json()
    print(req_json['text'])
    yan_text = req_json['text'].replace("'","\\\'")
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
while 1:
    map = text()
    if map == '0':
        print('第%s条写入成功' %str(i))
    else:
        print('第%s条已存在' %str(i))
    # time.sleep(1)
    i=i+1