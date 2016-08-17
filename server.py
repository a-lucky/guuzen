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
    # ビルトインの開発用サーバーの起動
    # ここでは、debugとreloaderを有効にしている
    tweetGetter = fetch.TweetGetter()
    th_me = threading.Thread(target=tweetGetter.fetch_guuzen, name="th_me")
    th_me.start()
    run(host='localhost', port=8080, debug=True, reloader=False)

