# coding:utf-8

import requests
from requests_oauthlib import OAuth1Session
from requests.exceptions import SSLError
import json, datetime, time, pytz, re
import csv
import os


def pp(obj):
    if isinstance(obj, list) or isinstance(obj, dict):
        orig = json.dumps(obj, indent=4)
        return eval("u'''%s'''" % orig).encode('utf-8')
    else:
        return obj


class TweetGetter:

    def __init__(self):
        self.KEYS = {}
        if os.path.exists('key.csv'):
            with open('key.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.KEYS[row[0]] = row[1]
        else:
            self.KEYS['consumer_key'] = os.environ.get('CONSUMER_KEY')
            self.KEYS['consumer_secret'] = os.environ.get('CONSUMER_SECRET')
            self.KEYS['access_token'] = os.environ.get('ACCESS_TOKEN_KEY')
            self.KEYS['access_secret'] = os.environ.get('ACCESS_TOKEN_SECRET')

        self.twitter = OAuth1Session(
            self.KEYS['consumer_key'],
            self.KEYS['consumer_secret'],
            self.KEYS['access_token'],
            self.KEYS['access_secret'])

        self.guuzen_list = []

    def fetch_guuzen(self):

        URL_NORM = re.compile(ur"(https?://[A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]+)")
        USERNAME_NORM = re.compile(ur"@[A-Za-z0-9_]+")
        HASHTAG_NORM = re.compile(ur"#\S+")

        import guuzen

        senryu = guuzen.Dodoitsu(pattern='senryu')
        tanka = guuzen.Dodoitsu(pattern='tanka')
        dodoitsu = guuzen.Dodoitsu(pattern='dodoitsu')

        num=0
        while True:
            url = "https://stream.twitter.com/1.1/statuses/sample.json"
            req = self.twitter.get(url, stream=True)

            if req.status_code == 200:
                print 'connection success'
                try:
                    for line in req.iter_lines():
                        try:
                            tweet = json.loads(line)
                        except Exception:
                            continue
                        if 'text' not in tweet:
                            continue
                        if tweet['user']['lang'] != 'ja':
                            continue
                        if 'retweeted_status' in tweet:
                            continue

                        num += 1

                        twt = tweet['text']

                        twt = URL_NORM.sub("", twt)
                        twt = USERNAME_NORM.sub("", twt)
                        twt = HASHTAG_NORM.sub("", twt)

                        # if num % 100 == 0:
                        #     print num

                        find_list = senryu.find_dodoitsu(twt.encode('utf-8'))
                        find_list.extend(tanka.find_dodoitsu(twt.encode('utf-8')))
                        find_list.extend(dodoitsu.find_dodoitsu(twt.encode('utf-8')))

                        if len(find_list) != 0:
                            self.guuzen_list.extend(find_list)
                            self.guuzen_list = self.guuzen_list[-min(10, len(self.guuzen_list)):]
                            for find in find_list:
                                print '/'.join(find)
                            # print "↑", tweet['user']['name'], twt.encode('utf-8')
                except requests.exceptions.ChunkedEncodingError:
                    print 'continue'
                    continue
            else:
                print 'connection miss'
                time.sleep(10)


# 文字列を日本時間2タイムゾーンを合わせた日付型で返す
def str_to_date_jp(str_date):
    dts = datetime.datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')
    return pytz.utc.localize(dts).astimezone(pytz.timezone('Asia/Tokyo'))


def box_str_to_date_jp(str_date):
    dts = datetime.datetime.strptime(str_date, '%Y %m月%d日 %H時%M分')
    return pytz.utc.localize(dts)


# 現在時刻をUNIX Timeで返す
def now_unix_time():
    return time.mktime(datetime.datetime.now().timetuple())


def str_to_unix_date_jp(str_date):
    dts = datetime.datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')
    dt = pytz.utc.localize(dts).astimezone(pytz.timezone('Asia/Tokyo'))
    return time.mktime(dt.timetuple())


def unix_time_to_datetime(int_date):
    return datetime.datetime.fromtimestamp(int_date)

