# -*- coding: utf-8 -*-

import json,pymysql
from flask import Flask,request,Response

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    # 获取参数
    format_type = request.values.get('type')

    # 查询数据库，返回随机语句
    sql_select = "SELECT * FROM yan.text WHERE id >= ((SELECT MAX(id) FROM yan.text)-(SELECT MIN(id) FROM yan.text)) * RAND() + (SELECT MIN(id) FROM yan.text) LIMIT 1"
    # db.ping(reconnect=True)
    cursor.execute(sql_select)
    results = cursor.fetchall()

    # 按需返回
    if format_type=='js':
        req = 'function finger_yan(){document.write("%s");}' %results[0][1]
        tongji()
        return Response(req,mimetype='text/javascript')
    elif format_type=='text':
        req = results[0][1]
        tongji()
        return Response(req,mimetype='text/html')

    elif format_type=='json':
        req = {
            'text':results[0][1]
        }
        tongji()
        return Response(json.dumps(req,ensure_ascii=False), mimetype='application/json')
        tongji()
    else:
        req = {
            'text': results[0][1]
        }
        tongji()
        return Response(json.dumps(req, ensure_ascii=False), mimetype='application/json')


@app.route('/num')
def num():
    sql_select_num = "SELECT * FROM yan.num WHERE yan.num.date = 'all';"
    cursor.execute(sql_select_num)
    results = cursor.fetchall()
    return str(results[0][1])

#统计函数
def tongji():
    global num
    num = num+1
    sql_update_num = "UPDATE `yan`.`num` SET `num` = {} WHERE `date` = 'all';".format(num)
    db.ping(reconnect=True)
    cursor.execute(sql_update_num)
    db.commit()

if __name__ == '__main__':
    # 建立数据库连接
    db = pymysql.connect("mysql.sunmiao.top", "yan", "sm80231314", charset="utf8")
    cursor = db.cursor()
    db.ping(reconnect=True)
    # 统计初始化
    sql_select_num = "SELECT * FROM yan.num WHERE yan.num.date = 'all';"
    cursor.execute(sql_select_num)
    results = cursor.fetchall()
    num = results[0][1]

    app.run(
            host = '0.0.0.0',
            port = 5000,
            threaded = True,
            debug = True
            )