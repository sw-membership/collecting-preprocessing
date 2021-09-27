# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: ekonlpy
#     language: python
#     name: ekonlpy_env
# ---

# ## pygoogle news

# 구글 뉴스에서 특정 키워드로 검색을 하면 관련 뉴스 url을 모두 얻을 수 있다. 
# 검색언어, 검색지역(국가), 기간을 설정할 수 있다. 
# 검색 키워드는 '종목명+stock'으로 했다. 

# !pip install pygoogle news --upgrade

# +
from pygooglenews import GoogleNews

gn = GoogleNews(lang = 'en', country = 'US')

s = gn.search('samsung electronics stock', when = '1m')

print(s['feed'].title)
# "boeing -airbus" - Google News

# -

s.keys()

s.values()

print(s['entries'])


