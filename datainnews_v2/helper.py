from datainnews_v2.variables import data_level1, data_level2, \
    data_level3, data_level_indicator, filter_list
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from newspaper import Article
from urllib.parse import urlparse
import pandas as pd
import twint

stop_words = set(stopwords.words('english'))


def get_new_articles(newspaper_username, since, until):
    c = twint.Config()
    c.Username = newspaper_username
    c.Pandas = True
    c.Hide_output = True
    c.Since = since
    c.Until = until
    twint.run.Search(c)
    df = twint.storage.panda.Tweets_df
    try:
        df = df[['id', 'created_at', "urls"]]
        df['urls'] = df.urls.apply(primary_url)
        df = df[df.urls != 404]
        df = df[df.urls.apply(filter_url)]
        df['created_at'] = (pd.to_datetime(
            df['created_at'], unit='ms').dt.tz_localize(
                'utc').dt.tz_convert('Asia/Kathmandu'))
        return df
    except Exception as e:
        print(str(e))
        return pd.DataFrame(columns=['id', 'created_at', "urls"])


def filter_url(url):
    return ((urlparse(url).netloc) == "www.nepalitimes.com")


def clean_text(raw):
    text = BeautifulSoup(raw, 'lxml').text
    word_tokens = word_tokenize(text.lower().rstrip())
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    return ' '.join(filtered_sentence)


def article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return clean_text(article.text)
    except Exception as e:
        print(str(e))
        return 404


def primary_url(urls):
    if len(urls) == 0:
        return 404
    return urls[0]


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
