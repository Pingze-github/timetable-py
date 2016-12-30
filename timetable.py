# coding=u8

import time as _time
import datetime
from threading import Thread


# 循环检查类
class Timer(Thread):
    def __init__(self,timetable):
        super(Timer,self).__init__()
        self.tb = timetable
        self.delay = 1
        #self.setDaemon(True)
    def run(self):
        while(True):
            time_date = datetime.datetime.now()
            time_now = {
                "second" : time_date.second
                ,"minute" : time_date.minute
                ,"hour" : time_date.hour
                ,"day" : time_date.day
                ,"month" : time_date.month
                ,"year" : time_date.year
                ,"microsecond" : time_date.microsecond
            }
            for task in self.tb.task_list: #造成计时间隔延长
                print time_now["hour"] , task["time"]["hour"] , time_now["minute"] , task["time"]["minute"] 
                if task["done"] == False:
                    time_task = task["time"]
                    flag_triggered = True
                    for key in time_task:    
                        if int(time_task[key]) != int(time_now[key]):
                            flag_triggered = False
                    if flag_triggered == True:
                        task["func"]()
                        task["done"] = True
            _time.sleep(self.delay) #延时防阻塞

#任务控制类
class Timetable(object):
    def __init__(self):
        self.task_list = []
        self.initTimer()
    def initTimer(self):
        self.timer = Timer(self);
        self.timer.start()
    def add(self,time,func):
        task = {
            "time":time
            ,"func":func
            ,"done":False
        }
        self.task_list.append(task);



def do():
    print "do do do"

timetable = Timetable()
time = {
    'hour':16
    ,'minute':28
    }
timetable.add(time,do)


