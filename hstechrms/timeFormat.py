import time
import datetime

#获取当前时间
def getTime():
    formatStr = '%Y-%m-%d %H:%M:%S'
    return time.strftime(formatStr,time.localtime(time.time()))

#获取当天日期
def getDay():
    formatStr = '%Y-%m-%d'
    return time.strftime(formatStr,time.localtime(time.time()))

#获取指定时间
def getNextWeek():
    #获取当前时间
    today = datetime.datetime.now()
    #计算偏移量
    offset = datetime.timedelta(days=+7)
    return (today + offset).strftime('%Y-%m-%d %H:%M:%S')

#获取UTC格式的时间
def getUTCtime():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

#获取当日与七日后日期,格式:2020-03-12 ~ 2020-03-19
def getTodayAndNextWeek():
	formatStr = '%Y-%m-%d'
	today = datetime.datetime.now()
	offset = datetime.timedelta(days=+7)
	return time.strftime(formatStr,time.localtime(time.time())) + ' ~ ' + (today + offset).strftime(formatStr)


#获取明日UTC格式时间
def getUTCTomorrowTime():
	today = datetime.datetime.utcnow()
	tomorrow = today + datetime.timedelta(days=1)
	return tomorrow.strftime("%Y-%m-%dT%H:%M:%S.000Z")

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
