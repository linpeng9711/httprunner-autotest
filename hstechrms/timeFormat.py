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

#获取当前周的星期一与星期天的日期
# def get_current_week():
#     monday, sunday = datetime.date.today(), datetime.date.today()
#     one_day = datetime.timedelta(days=1)
#     while monday.weekday() != 0:
#         monday -= one_day
#     while sunday.weekday() != 6:
#         sunday += one_day
#     # 返回当前的星期一和星期天的日期
#     return monday, sunday



