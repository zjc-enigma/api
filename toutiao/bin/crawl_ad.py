#coding=utf-8
import os
import sys
sys.path.append("/Users/Patrick/Git")
from utils import myutils
import requests
from pyquery import PyQuery as pq
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

base_url = 'http://m.toutiao.com/'
browser = webdriver.Chrome()
browser.get(base_url)
browser.refresh()

res = []

def get_ad_titles(res):

    doc = pq(browser.page_source)
    doc.xhtml_to_html()
    print doc('h3.dotdot.line3').text()
    all_ads = doc('span.ad_label.space')

    for item in all_ads.items():

        title = item.parent().parent()('h3').text()
        if title not in res:
            res.append(title)



def click_refresh_btn():

    browser.find_element_by_css_selector('.refresh_btn.btn').click()


def print_crawled_titles(res):

    for item in res:
        print item

if __name__=="__main__":

    click_refresh_btn()
    get_ad_titles(res)

    print_crawled_titles(res)
