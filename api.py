#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:wefinger

import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/api/')
def get_hito():
    conn = sqlite3.connect('HITODB.db')
    hito = conn.execute(
        'select * from hitokoto order by random() limit 1').fetchone()
    hitokoto = "{} ——「{}」".format(hito[1], hito[2])
    return 'function hitokoto() { ' + 'document.write(\'{}\');'.format(
        hitokoto) + '}'
@app.route('/api/json/')
def get_json():
    conn = sqlite3.connect('HITODB.db')
    hito = conn.execute(
        'select * from hitokoto order by random() limit 1').fetchone()
    hitokoto = {}
    hitokoto['id'] = hito[0]
    hitokoto['hito'] = hito[1]
    hitokoto['source'] = hito[2]
    return jsonify(hitokoto)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)