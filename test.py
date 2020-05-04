# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: xiecheng_autotes
# FN: test
# Author: xiaxu
# DATA: 2020/4/28
# Description:
# ---------------------------------------------------
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
driver.implicitly_wait(5)
# 需要页面响应成功后，才执行下一步
driver.get("https://www.baidu.com")
time.sleep(1)
# 显示等待，60s，轮询时间5s,untill后为条件，有隐式和显示时，以最大时间为准
print("定位！")
# WebDriverWait(driver,5).until(lambda d:driver.find_elements_by_id("kw"),message="定位元素超时！")
# print("查询")
driver.find_element_by_link_text("地图").click()
print("跳转至地图页面！")
WebDriverWait(driver,15,poll_frequency=5).until(lambda d:driver.find_element_by_id("search-button"),message="定位地图页面元素超时")
