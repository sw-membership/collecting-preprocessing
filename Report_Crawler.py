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

# ## 한경컨센서스 증권사 리포트 크롤러
# selenium을 활용해 기업분석 리포트를 크롤링하는 프로그램입니다. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("http://consensus.hankyung.com/apps.analysis/analysis.list?skinType=business")

driver.find_element_by_name("sdate").click()

#기간 설정
driver.find_element_by_link_text('1년').click()

driver.find_element_by_css_selector('#f_search > div > div.hd_top > div.btn_r > a:nth-child(1) > img').click()

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/a[2]").click()

# ### 직접 설정 변경
# 크롬 '추가 콘텐츠 설정'에서 pdf클릭 시 파일이 바로 다운되게 설정을 변경합니다. 
#

# 크롤링할 각 페이지의 url에 붙을 url_basis
url_basis = driver.current_url[0:-1]

url_test = url_basis + "1"
for i in range(2) :
    input = "#contents > div.table_style01 > table > tbody > tr:nth-child(%d)> td:nth-child(9) > div > a > img" %(i+1)
    alt = driver.find_element_by_css_selector(input).get_attribute('alt')
    print(alt)
    num = 0
    while True:
        if (alt[num]=
    

n = 0 # n은 페이지 번호
stock_name_list = [] #종목명만 모을 리스트

# +
while True :    
    n = n + 1 
    temp = n    
    url = url_basis + str(temp)
    driver.get(url)    
    for i in range(20) :
        input = "#contents > div.table_style01 > table > tbody > tr:nth-child(%d)> td:nth-child(9) > div > a > img" %(i+1)
        # 클릭하여 pdf다운
        driver.find_element_by_css_selector(input).click()
        
        # 종목명만(stock_name)따로 추출(pdf파일명이 random숫자이기 때문)
        alt = driver.find_element_by_css_selector(input).get_attribute('alt')
        temp1= alt.find("2") + 8
        temp2 = alt[temp1 : ]
        stock_name = temp2[:-4]
        stock_name_list.append(stock_name)        
        
        time.sleep(1)        
    
    print("%d번째 페이지 완료"%n)    
    
    if (n == 3) :
        break
        
        
            
            
# -

driver.close()


