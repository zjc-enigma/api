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
import time
from data import title_tag



class SearchToutiao(object):

    def __init__(self, keywords, count=20, offset=0):
        self.keywords = keywords
        self.count = count
        self.offset = offset
        self.search_res_list = []
        self.tagged_res_dict = {}

    def search_keyword(self):

        base_api = "http://toutiao.com/search_content/?offset={offset}&format=json&keyword={keywords}&autoload=true&count={count}"

        api_url = base_api.format(offset=self.offset,
                                  keywords=self.keywords,
                                  count=self.count)

        headers = myutils.get_test_header()
        ret = requests.get(api_url, headers=headers)

        ret_json = json.loads(ret.text)

        res_list = ret_json['data']

        return res_list

    def get_search_res(self):

        res_list = self.search_keyword()

        for item in res_list:
            title = item['title']
            url = item['url']

            self.search_res_list.append({"title": title,
                                         "url": url})



        for search_res in self.search_res_list:
            print search_res['title']

        return self.search_res_list

    def get_tagged_res(self):

        res_list = self.search_keyword()

        for item in res_list:

            title = item['title']
            url = item['url']
            tag = title_tag.find_title_tag(title)

            if tag not in self.tagged_res_dict:
                self.tagged_res_dict[tag] = [{"title": title, "url": url}]

            else:
                self.tagged_res_dict[tag].append({"title": title, "url": url})


        return self.tagged_res_dict
