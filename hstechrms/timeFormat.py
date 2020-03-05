import time
import datetime

#获取当前时间
def getTime():
    formatStr = '%Y-%m-%d %H:%M:%S'
    return time.strftime(formatStr,time.localtime(time.time()))

#获取指定时间
def getNextWeek():
    #获取当前时间
    today = datetime.datetime.now()
    #计算偏移量
    offset = datetime.timedelta(days=+7)
    return (today + offset).strftime('%Y-%m-%d %H:%M:%S')

