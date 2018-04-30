# -*- coding: utf-8 -*-

import json,pymysql
from flask import Flask,request,Response

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    format_type = request.values.get('type')

    db = pymysql.connect("mysql.sunmiao.top", "yan", "sm80231314", charset="utf8")
    cursor = db.cursor()
    sql_select = "SELECT * FROM yan.text WHERE id >= ((SELECT MAX(id) FROM yan.text)-(SELECT MIN(id) FROM yan.text)) * RAND() + (SELECT MIN(id) FROM yan.text) LIMIT 1"
    cursor.execute(sql_select)
    results = cursor.fetchall()

    print(results[0][1])

    if format_type=='js':
        req = 'function finger_yan(){document.write("%s");}' %results[0][1]
        return Response(req,mimetype='text/javascript')
    elif format_type=='text':
        req = results[0][1]
        return Response(req,mimetype='text/html')
    elif format_type=='json':
        req = {
            'text':results[0][1]
        }
        return Response(json.dumps(req,ensure_ascii=False), mimetype='application/json')
    else:
        req = {
            'text': results[0][1]
        }
        return Response(json.dumps(req, ensure_ascii=False), mimetype='application/json')

if __name__ == '__main__':
    app.run()
