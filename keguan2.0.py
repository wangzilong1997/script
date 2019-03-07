from selenium import webdriver
from selenium.webdriver.support.select import Select
import urllib
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import win32con
import win32api
import sys
import os
#获取临时路径
land = os.getcwd()
print(1111)
print(land)
#向用户添加临时路径
sys.path
sys.path.append(land)

browser=webdriver.Chrome(executable_path='chromedriver.exe')

#隐性等待
browser.get('http://xdyc.echehua.com/login/index')
#登陆部分
try:
    browser.find_element_by_class_name('account-container')
    a = 1
    k = input("选择科目：科目二输入:2 科目三输入:3~~~~~~")
except:
    a = 2
    pass
if a == 1:
    while a == 1:
        print("存在元素(请输入用户正确信息)")

        x = input("用户名:")
        print(x)
        #username
        username = browser.find_element_by_id("username")
        username.clear()
        username.send_keys(x)
        time.sleep(1)
        #password
        y = input("密码：")
        print(y)
        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys(y)
        #验证码
        z = input("验证码：")
        print(z)
        verify = browser.find_element_by_id("verifycode")
        verify.clear()
        verify.send_keys(z)

        #自动点击登陆
        login = browser.find_element_by_class_name('btn-large')
        login.click()
        #验证是否登陆成功
        try:
            browser.find_element_by_class_name('account-container')
            a = 1
        except:
            a = 2
            pass
if a == 2:
    print("登陆成功")
    print(k)
    try:
        browser.find_element_by_id("exam")
        e = 1
    except:
        e = 2
        pass
if e == 1:
    while e == 1:
        # 自动选择科目
        Select(browser.find_element_by_id("exam")).select_by_value(k)
        print("选择科目完成")
        #time.sleep(1)
        # 自动选择教练
        browser.find_element_by_id("divselect").click()
        browser.find_element_by_id("teacherlist").click()
        print("选择教练完成")

        #time.sleep(1)
        # 点击模拟登陆
        browser.find_element_by_class_name('btn-large').click()
        print("登陆点击完成")

        time.sleep(1)
        try:
            browser.find_element_by_id("exam")
            browser.find_element_by_xpath("/html/body/div[4]/div/form/div/button").click()
            print("关闭弹出框成功")
            e = 1
        except:
            e = 2


if e == 2:
    print("完成教练选择进入选课页面")
    # 查询剩余课程
    left = browser.find_elements_by_class_name('btn-primary')
    size = len(left)
    print(size)
    print(left)
    # 选课部分
    c = 1
    d = 1
    while True:
        left = browser.find_elements_by_class_name('btn-primary')
        size = len(left)
        if size > 1:
            print("还有课")
            left[0].click()
            d = d + 1
            if d > 2:
                break
            continue
        elif size == 1:
            print("还有个鸡儿课:", c)
            browser.refresh()
            time.sleep(1)
            c = c + 1
        continue
