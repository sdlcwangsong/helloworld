# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import urllib
import time,json
import os
print("workd")
print("helo")
print("")
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.find_element_by_css_selector("#u1 .lb").click()
time.sleep(1)
browser.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("usernmae")
browser.find_element_by_id("TANGRAM__PSP_8__password").send_keys("password")
browser.find_element_by_id("TANGRAM__PSP_8__submit").click()
browser.find_element_by_id("TANGRAM__PSP_8__verifyCode").send_keys(input("输入验证码: "))
browser.find_element_by_id("TANGRAM__PSP_8__submit").click()
time.sleep(1)
browser.get("http://tieba.baidu.com/f?kw=%E5%BF%83%E6%83%85")
time.sleep(1)
browser.find_element_by_xpath(".//*[@id='tb_rich_poster']/div[3]/div[1]/div[2]/input").send_keys(Keys.TAB)
time.sleep(3)
browser.quit()
