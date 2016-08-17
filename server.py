# coding:utf-8

from bottle import route, run, static_file, error, template, request, get, HTTPResponse
import json
import threading

import fetch

tweetGetter = None

@route("/")
def html_index():
    return template("index")


@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')


@route('/css/<filename>')
def css_static(filename):
    return static_file(filename, root='./css')


@route('/guuzen.json')
def guuzen_send():
    body = json.dumps({'texts': tweetGetter.guuzen_list})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

if __name__ == '__main__':
    import os
    os.system('python mecab-python-0.996/setup.py build')
    os.system('python mecab-python-0.996/setup.py install')

    tweetGetter = fetch.TweetGetter()
    th_me = threading.Thread(target=tweetGetter.fetch_guuzen, name="th_me")
    th_me.start()


    if os.environ.get('CONSUMER_KEY'):
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True, reloader=False)

