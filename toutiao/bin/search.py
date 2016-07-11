#coding=utf-8
import os
from os.path import isfile, join
import sys
reload(sys)
sys.setdefaultencoding('UTF8')
sys.path.append("/Users/Patrick/Git")
from utils import myutils
import requests
from pyquery import PyQuery as pq
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


keywords = "uber"
count = 20
offset = 0
base_api = "http://toutiao.com/search_content/?offset={offset}&format=json&keyword={keywords}&autoload=true&count={count}"

api_url = base_api.format(offset=offset,
                          keywords=keywords,
                          count=count)

headers = myutils.get_test_header()
ret = requests.get(api_url, headers=headers)
#doc = pq(ret.text)
ret_json = json.loads(ret.text)

res_list = ret_json['data']


search_res_list = []
for item in res_list:
    title = item['title']
    url = item['url']

    search_res_list.append({"title": title,
                            "url": url})



for search_res in search_res_list:
    print search_res['title']
