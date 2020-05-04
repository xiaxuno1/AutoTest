# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: xiecheng_autotest
# FN: booking_tikects
# Author: xiaxu
# DATA: 2020/3/26
# Description:见项目实战
# ---------------------------------------------------
from selenium import webdriver
import ddt
import time
from function import id,css,js,class_name,date_n,driver,get_url,open_browse
from search_tickets import *
from selenium.webdriver.common.action_chains import ActionChains
import HTMLTestRunner
import unittest


# 车次搜索
# @ddt.ddt   # ddt类装饰器,使用装饰器执行时出错，具体原因未知
class BookingTickets(unittest.TestCase):
    def setup(self):
        self.driver = open_browse()

    # @ddt.data(['北京','上海','1'],['北京','成都','1'],['成都','广州','1'])   # ddt方法装饰器，用于测试时填充测试数据，可以是元组列表字典
    # @ddt.unpack
    def test_ctrip_tickets(self):
        #from_city = "成都"
        # to_city = "广州"
        # depart_date = date_n(2)
        # search_tickets(from_city,to_city,depart_date)
        log("Read excel file in this dir")
        test_data = self.test_data = read_excel("testdate.xlsx",0)
        # print(test_data)
        log("Begin to search tickets")
        # 使用ddt装饰器实现数据多次输入
        # search_tickets(from_city, to_city, depart_date)
        # 数据的使用方式需要优化
        search_tickets(test_data[0][1],test_data[1][2],date_n(int(test_data[2][2])))
        log("End to search tickets")
        # 车票预订页面,直接在z124硬座单击预订，可选项待后面补充,这样定位当车次不存在时可能会导致错误
        # https://blog.csdn.net/bangwu6488/article/details/101365369
        log("starting booking ticket")
        railway_number = "D1751"
        site_class = "二等座"
        css("div.railway_list:nth-child(4) > div:nth-child(6) > div:nth-child(1) > a:nth-child(1)").click()
        # driver.find_element_by_xpath("//div[@strong='D1751']")
        # booking_ticket(railway_number) 功能还未实现
        log("booking ticket success")
        #填写订单页面
        time.sleep(2)
        log("starting fill info")
        driver.find_element_by_css_selector(".input-name").send_keys("张三")

    def tearDown(self):
        self.driver = open_browse()
        self.driver.quit()


if __name__ == '__main__':
    start_time = time.perf_counter()
    suite = unittest.TestSuite()
    suite.addTest(BookingTickets('test_ctrip_tickets')) # 补充测试用例至测试套,注意这里的写法，之前就因为写成类引用函数导致输出报告为空
    file_name = "E:\\report_booking_tickets.html"
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report_Portal',
                                           description='Report_Description')  #设置输出报告的格式：标题，描述
    runner.run(suite)
    log("test report successs,browse quit now!")
    print("总共用时：{time}".format(time=time.perf_counter() - start_time))
    fp.close()
