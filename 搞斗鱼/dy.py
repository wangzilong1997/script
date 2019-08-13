from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import sys
import os

#获取临时路径
land = os.getcwd()

print(land)

#向用户添加临时路径
sys.path.append(land)

#输入一个正在抽奖的直播间
print("输入一个正在抽奖的直播间")

begin = input("从这开始:")


browser = webdriver.Chrome(executable_path='chromedriver.exe')

#隐性等待
browser.get(begin)
time.sleep(2)
print("浏览器最大化")
browser.maximize_window() 
time.sleep(8)
"""
browser.find_element_by_class_name("LotteryDrawEnter-enter").click()

time.sleep(2)
"""
print("完成")
browser.find_element_by_xpath('//*[@id="js-player-dialog"]/div/div[11]/div[1]/div/div/div[2]/div/div[5]/div[2]').click()

print("点击完成")
"""
time.sleep(20)
print("睡眠完成")
browser.find_element_by_xpath('//*[@id="loginbox"]/div[2]/div[1]/div[1]').click()


js='window.open("https://www.douyu.com/member/oauth/signin/qq?biz_type=1&amp;ref_url=https%3A%2F%2Fwww.douyu.com%2Ftopic%2Fwdhd%3Frid%3D4352605&amp;room_id=0&amp;cate_id=0&amp;tag_id=0&amp;child_id=0&amp;vid=0&amp;fac=&amp;type=login");'
browser.execute_script(js)

"""
time.sleep(20)
browser.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/div[2]/a[1]').click()
