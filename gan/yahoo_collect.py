# -*- coding: utf-8 -*-

################################
# yahoo画像サイトからスクレイピング
################################

import os
import sys
import traceback
from mimetypes import guess_extension
from time import time, sleep
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup

MY_EMAIL_ADDR = ''


class Fetcher:
    def __init__(self, ua=''):
        self.ua = ua

    def fetch_img_direct(self, url):
        """
        yahoo画像検索画面に表示されている画像のbyte情報を抽出します。
        引数:
            url: yahoo画像検索画面のurlです。

        返り値:
            img_b_content: ウェブサイトリソースのbyteコードのリストです。
            mime: CONTENT_TYPEにより指定されている拡張子です。
        """
        req = Request(url, headers={'User-Agent': self.ua})
        try:
            with urlopen(req, timeout=3) as p:
                page_b_content = p.read()
                structured_page = BeautifulSoup(
                    page_b_content.decode('UTF-8'), 'html.parser')
                img_link_elems = structured_page.find_all('img')
                img_urls = [e.get('src') for e in img_link_elems if e.get(
                    'src').startswith('http')]
                img_urls = list(set(img_urls))  # なぜset化しているのかは不明
        except:
            sys.stderr.write('Error in fetching {}\n'.format(url))
            sys.stderr.write(traceback.format_exc())
            return None, None

        img_b_content = []
        mime = []
        for i, img_url in enumerate(img_urls):
            req1 = Request(img_url, headers={'User-Agent': self.ua})
            try:
                with urlopen(req1, timeout=3) as p:
                    img_b_content.append(p.read())
                    mime.append(p.getheader('Content-Type'))
            except:
                sys.stderr.write('Error in fetching {}\n'.format(img_url))
                sys.stderr.write(traceback.format_exc())
                continue

        return img_b_content, mime


fetcher = Fetcher(MY_EMAIL_ADDR)


def url_brancher(word):
    """
    yahoo画像検索画面のurlを、検索条件の組み合わせの数だけ取得します。

    引数:
        word : 検索語です。

    返り値:
        urllist : yahoo画像検索画面のurlのリストです。
    """
    constant = "https://search.yahoo.co.jp/image/search?p={}&n=60".format(
        quote(word))

    values = [
        ["", "small"],
        ["", "red"],
        ["", "face"]
    ]
    """
    values = [\
    ["", "small", "medium", "large", "wallpaper", "widewallpaper"],\
    ["", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink", "white", "gray", "black", "brown"],\
    ["", "face", "photo", "clipart", "lineart"]\
    ]
    """
    urllist = []

    for i in range(len(values[0])):
        for j in range(len(values[1])):
            for k in range(len(values[2])):
                urllist.append(constant + "&dim={}".format(values[0][i]) + "&imc={}".format(
                    values[1][j]) + "&ctype={}".format(values[2][k]))
    return urllist


def main(word):
    """
    Fetchにより取得された情報をもとに画像ファイルを保存します。

    引数:
    word: 検索語です。

    返り値:
    """
    data_dir = 'building/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    yahoo_url_list = url_brancher(word)

    for i, yahoo_url in enumerate(yahoo_url_list):
        sleep(1)
        img, mime = fetcher.fetch_img_direct(yahoo_url)
        if not mime or not img:
            print('Error in fetching {}\n'.format(yahoo_url))
            continue

        for j, img_url in enumerate(img):
            ext = guess_extension(mime[j].split(';')[0])
            if ext in ('.jpe', '.jpeg'):
                ext = '.jpg'
            if not ext:
                print('Error in fetching {}\n'.format(img_url))
                continue

            result_file = os.path.join(data_dir, str(i) + str(j) + ext)
            with open(result_file, mode='wb') as f:
                f.write(img_url)
            print('fetched', str(i) + str(j) + ext)


if __name__ == '__main__':
    word = input("検索ワードを入力してください : ")
    main(word)
