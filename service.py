#!/usr/bin/env python
from flask import request, Flask, url_for, jsonify, make_response
from urlparse import urlparse
import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

db_connect = sqlite3.connect(os.path.join(BASE_DIR,'service.db'),isolation_level = None)
conn = db_connect.cursor()

app = Flask(__name__)

@app.route('/track/api/v1.0/domains/<path:arg1>', methods=['POST'])
def api_log(arg1):
    url = urlparse(arg1).hostname
    if url != "":
        query = conn.execute('with new (domain,cnt) as (values( ?,1)) insert or replace into counter select new.domain,new.cnt+ifnull(c.cnt,0) fro
m new left outer join counter c on new.domain = c.domain',(url,))
        return jsonify({'logged': url})
    else:
        return jsonify({'Logged': None})

@app.route('/track/api/v1.0/domains/clear', methods=['DELETE'])
def api_clear():
    query = conn.execute("delete from counter")
    data = dict(query.fetchall())
    return jsonify({'erased': 'all counters are cleared'})

@app.route('/track/api/v1.0/domains/top3')
def api_get():
    query = conn.execute("select * from counter order by cnt desc limit 3")
    data = dict(query.fetchall())
    return jsonify({'domains': data})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

if __name__ == '__main__':
    app.run()
