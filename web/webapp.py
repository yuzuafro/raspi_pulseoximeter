#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os, json
from bottle import route, run, debug, template, request, static_file, HTTPResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pulseoximeter

@route('/css/<file_path:path>')
def get_js(file_path):
    r = HTTPResponse(status=200)
    r.headers['Content-Type'] = 'text/css; charset=utf-8'
    r.body = static_file(file_path, root='./css')
    return r

@route('/js/<file_path:path>')
def get_js(file_path):
    r = HTTPResponse(status=200)
    r.headers['Content-Type'] = 'text/javascript; charset=utf-8'
    r.body = static_file(file_path, root='./js')
    return r

@route('/_spo2')
def spo2():
    return json.dumps({'result': 99})

@route('/_heartrate')
def heartrate():
    return json.dumps({'result': 70})

@route('/_measure')
def measure():
    """measure SpO2 and HeartRate"""
    measure = pulseoximeter.MAXREFDES117()
    hr, spo2 = measure.get()
    return json.dumps({'heartrate': hr, 'spo2': spo2})


@route('/')
def index():
    return template('index.tpl', request=request)


debug(True)
run(host='0.0.0.0',port=8080, reloader=True)

