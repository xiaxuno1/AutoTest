# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: BeginningPython
# FN: function
# Author: xiaxu
# DATA: 2020/4/22
# Description:用于定义方法
# ---------------------------------------------------
from datetime import datetime,date,timedelta
from selenium import webdriver
import logging
import xlrd,xlwt


driver = webdriver.Firefox()
def id(element):
    return driver.find_element_by_id(element)
def css(element):
    return driver.find_element_by_css_selector(element)
def js(element):
    return driver.execute_script("document.getElementById("+"'"+element+"'"+").removeAttribute('readonly')")
def class_name(element):
    return driver.find_element_by_class_name(element)
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))))
def open_browse():
    return driver
def get_url(url):
    driver.get(url)
def xpath(element):
    return driver.find_element_by_xpath(element)
#预处理测试存放的数据
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    test_data = []
    for i in range(sheet.ncols):
        data = []
       # for j in range(sheet.nrows-1):
        test_data.append(sheet.col_values(i)) #读取一列,以列表的方式返回
       # test_data.append(data)
    return test_data
#日志的输出设置
def log(str):
    #基础设置：水准INFO;
    logging.basicConfig(level=logging.INFO,\
                        format = '%(asctime)s %(filename)s %(levelname)s %(message)s',\
                        datefmt="%a, %d %b %Y %H:%M:%S",\
                        filename='xiecheng-autotest-log-selenium.log',\
                        filemode='a')
    console = logging.StreamHandler()#初始化stream输出位置，如果为空，则使用标注流输出
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')#初始化formatters
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)


#测试excel读取用例
if __name__ == '__main__':
    print(read_excel("testdate.xlsx",0))
