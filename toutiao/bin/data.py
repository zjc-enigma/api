#coding=utf-8
import os
import sys
sys.path.append('..')
import re


titles_path = '../data/toutiao.txt'
rule_path = '../data/rule.conf'


def find_title_tag(title, rule_list):

    """
    Keyword Arguments:
    title     -- toutiao title (utf8)
    rule_list -- rule tag -> regex list (unicode dict list)

    return -- tag(utf8)

    """
    for rule in rule_list:

        tag = rule.keys()[0]
        regex_list = rule[tag]

        for regex in regex_list:

            if re.search(re.escape(regex), title.decode('utf8')):
                return tag.encode('utf8')

    return "未知体"



def all_titles_classify(title_path, rule_path):
    """
    Keyword Arguments:
    title_path -- all titles data file path ; all titles string(utf8)
    rule_path  -- all classify rule file path ; all rule string(utf8)

    return -- classified list, key is rule tag(utf8) ; value is titles(utf8)

    """

    res_dict = {}
    rule_list = []

    for line in open(rule_path):

        line = line.decode('utf8')
        line = line.strip()
        line = line.split('\t')

        if len(line) != 3:
            print ("invalid line in rule file")
            continue

        tag = line[1]
        regex_list = line[2].split(',')

        rule_list.append({tag:regex_list})

    for line in open(titles_path):

        line = line.strip()
        line = line.split('\t')
        title = line[0]
        tag = find_title_tag(title, rule_list)

        if tag not in res_dict:
            res_dict[tag] = [title]

        else:
            res_dict[tag].append(title)

    return res_dict


res_dict = all_titles_classify(titles_path, rule_path)
