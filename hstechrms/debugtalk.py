import time
import random
import string
import mockLogin
import timeFormat
import os
from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.chrome.options import Options

#初始化
def init():
    mockLoginMethod = os.environ["mock_login_method"] #获取模拟登陆方式
    if mockLoginMethod == 'headless':
        print('使用headless模拟登陆')
        getCookByHeadlessChrome()
    elif mockLoginMethod == 'webdriver':
        print('使用webdriver模拟登陆')
        get_cookie()
    else:
        print('mock_login_method参数设置不正确,请进入.env文件修改')
        return
    get_csrf()
    generatorStaticRandomValue()

#产生两秒的运行间隔
def time_sleep():
    time.sleep(2)

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

#使用无头浏览器获得模拟登陆获得cookie
def getCookByHeadlessChrome():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
    mockLogin.getCookie(driver)
    cookie = driver.get_cookies()[0]
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

#获取一周后的时间
def getNextWeek():
    return timeFormat.getNextWeek()

#生成全局唯一的随机字符串(多次调用该方法,返回同一个)
def generatorStaticRandomValue():
    global srv
    srv = appendRandomStr("测试数据唯一值")

#获取UTC格式当天日期
def getUTCtime():
    return timeFormat.getUTCtime()

#获取明日UTC格式时间
def getUTCTomorrowTime():
    return timeFormat.getUTCTomorrowTime()

#获取当日与七日后日期,格式:2020-03-12 ~ 2020-03-19
def getTodayAndNextWeek():
    return timeFormat.getTodayAndNextWeek()

#获得全局唯一的随机字符串
def getSrv():
    return srv

#获得当前日期
def getDay():
    return timeFormat.getDay()

init()
