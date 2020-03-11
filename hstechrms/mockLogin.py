# https://segmentfault.com/a/1190000015642808
import time 
import os
from selenium import webdriver # 从selenium导入webdriver


#driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

def getCookie(driver):
    base_path = os.environ["base_path"]
    driver.get(base_path+'/hstechrms/login')

    username = driver.find_element_by_id('username$text') #用户名
    password = driver.find_element_by_id('password$text') #密码
    submit = driver.find_element_by_id('login') #登录按钮
    
    #username.send_keys("ywczy03") #输入框输入
    username.send_keys(os.environ["login_username"]) #输入框输入
    password.send_keys(os.environ["login_password"]) #输入框输入
    #token = driver.find_element_by_xpath('//form[@id="loginForm"]/input').get_attribute('value')
    submit.click() #登录

    # driver.findElement(By.id("firstname-placeholder")).sendKeys(Keys.F5); 
    # driver.navigate().refresh()
    # time.sleep(5)

    cookie=driver.get_cookies()[0]

    # 获取cookie
    #print(cookie['domain'],cookie['name'],cookie['value'])
    return cookie['value']

#使用无头浏览器模拟点击登录
# def getCookByHeadlessChrome(driver):
#     base_path = os.environ["base_path"] #获取项目根目录
#     driver.get(base_path+'/hstechrms/login')
#     username = driver.find_element_by_id('username$text') #用户名
#     password = driver.find_element_by_id('password$text') #密码
#     submit = driver.find_element_by_id('login') #登录按钮
#     username.send_keys(os.environ["login_username"]) #输入框输入
#     password.send_keys(os.environ["login_password"]) #输入框输入
#     submit.click() #登录
#     cookie=driver.get_cookies()[0]
#     return cookie['value']

#登录后从index页定位meta元素,获取token值
def getTokenValue(driver):
    #driver.get('http://172.16.100.115:8080/hstechrms/index')
    token = driver.find_element_by_name('_csrf').get_attribute('content')
    return token