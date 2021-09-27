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

# ## sumy를 활용한 요약
# 이 프로그램은 두 가지 경우에 활용 가능합니다. 
# 1)url 내 텍스트 요약 2) 텍스트 파일 요약 
# 구글 뉴스와 (양이 많은)증권사 리포트는 sumy를 활용해 요약하려 합니다. 

# +
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "korean"
SENTENCES_COUNT = 10


if __name__ == "__main__":
    # 1. 텍스트 요약
    parser = PlaintextParser.from_file("리포트에서 추출한 텍스트 파일", Tokenizer(LANGUAGE))
    
    # 2. url 요약
    url = "요약하려는 구글 뉴스 url"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    
    
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
# -


