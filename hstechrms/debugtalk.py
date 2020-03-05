import time
import random
import string

import mockLogin
import timeFormat
from selenium import webdriver # 从selenium导入webdriver

#初始化
def init():
    get_cookie()
    get_csrf()

#获取token
def get_csrf():
    global csrf
    csrf = mockLogin.getTokenValue(driver)
    print('token:'+csrf)
    
#获取cookie
def get_cookie():
    global driver
    driver = webdriver.Chrome()
    mockLogin.getCookie(driver)

    cookie=driver.get_cookies()[0]
    # 获取cookie
    #print(cookie['domain'],cookie['name'],cookie['value'])
    global cookie_session
    cookie_session=cookie['value']
    print('session:'+cookie_session)
    return cookie['value']

def get_cookie_session():
    return cookie_session

def get_token():
    return csrf

#生成随机字符串后缀
def appendRandomStr(originalStr):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return originalStr + ran_str

#获取当前时间
def getTime():
    return timeFormat.getTime()

#获取指定日期时间
def getNextWeek():
    return timeFormat.getNextWeek()

# #获得全局唯一的随机字符串(多次调用该方法,返回同一个)
# def getStaticRandomStr():

init()
