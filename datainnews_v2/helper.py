from datainnews_v2.helper import data_level1, data_level2, \
    data_level3, data_level_indicator, filter_list
import re


def level1_count(article):
    if article:
        article = str(article)
        keyword_list = []
        for word in data_level1:
            search_ = r"\b" + word.split()[0] + r"[a-zA-Z]*\s\b" \
                + word.split()[1] + r"[a-zA-Z]*"
            if re.search(search_, article):
                keyword_list.append(word)
        for word in data_level_indicator:
            if word in article:
                keyword_list.append(word)
        return keyword_list
    return []


def level2_count(article, valid):
    if valid == 1:
        article = str(article)
        keyword_list = []
        for word in data_level2:
            search_ = r"\b" + word + r"[a-zA-Z]*"
            if re.search(search_,  article):
                keyword_list.append(word)
        return keyword_list
    return []


def level3_count(article, valid):
    if valid == 1:
        article = str(article)
        keyword_list = []
        for word in data_level3:
            search_ = r"\b" + word + r"[a-zA-Z]*"
            if re.search(search_,   article):
                keyword_list.append(word)
        return keyword_list
    return []


def level_2_3_filter(article):
    article = str(article)
    for word in filter_list:
        if word in article:
            return 1
    return 0


def level_len(count_list):
    if type(count_list) == str:
        return (1 if len(count_list) > 2 else 0)
    return (1 if len(count_list) > 0 else 0)