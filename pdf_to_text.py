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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## pdf 파일에서 텍스트 추출
# tika라이브러리를 활용해 pdf에서 텍스트를 추출할 수 있습니다.  

# !pip install tika

# +
from tika import parser

data = parser.from_file("미래에셋_삼성전자.pdf")
content = data["content"].strip()

with open("미래에셋_삼성전자_텍스트.txt", 'w', encoding='utf-8') as txt:
    print(content, file=txt)
