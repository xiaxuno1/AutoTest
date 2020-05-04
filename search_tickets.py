# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: BeginningPython
# FN: search_tickets.py
# Author: xiaxu
# DATA: 2020/4/22
# Description:此文件用于业务代码
# ---------------------------------------------------
from selenium import webdriver
import time
from datetime import datetime,date,timedelta
from selenium.webdriver.common.action_chains import ActionChains
from function import *


'''
:param 
from_station:出发站
to_station:到达站
n：表示当天后的第几天
'''

def search_tickets(from_city, to_city,depart_date):
    # driver = open_browse()  #unittest中使用setup初始化
    driver.implicitly_wait(10)
    url = 'https://trains.ctrip.com/TrainBooking/SearchTrain.aspx'
    get_url(url)
    time.sleep(1)
    id("departCityName").send_keys(from_city)
    time.sleep(1)
    id("arriveCityName").send_keys(to_city)
    time.sleep(1)  #与上面一样，这里执行过快都会出现无法填充的错误，可以通过设置
    # 移除JS的readonly属性方可赋值
    js("departDate")
    id("departDate").clear()
    id("departDate").send_keys(depart_date)
    driver.maximize_window()
    ActionChains(driver).move_by_offset(0,0).click().perform()#为了解决弹出窗口导致无法定位的问题
    class_name("searchbtn").click()
def booking_ticket(num):
    return xpath("//strong[text() = %s]/../../../div[6]/a[1]" % num).click() #车次和作为等级设定功能未实现


