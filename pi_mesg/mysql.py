#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:wefinger

import pymysql

conn = pymysql.connect(
    host='mysql.sunmiao.top',
    port=3306,
    user='root',
    passwd='sm80231314',
    charset='utf8'
)
cursor = conn.cursor()

cursor.execute("INSERT INTO `pi_info`.`ds18b20`(`time`,`temp`) VALUES (NOW(),'23.6')")
conn.commit()