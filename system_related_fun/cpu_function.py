# -*- coding: utf-8 -*-
# 文件名：cpu_function
# 创建日期：2020-7-17
__author__ = r'国信证券大连分公司'

import psutil as psu
from config import psutil as pps
# 返回一个包含CPU使用时长的元组(单位:秒) percpu=True 就调用 per_cputimes 显示每一个cpu的使用时间
cpu_times_list = psu.cpu_times(percpu=True)

for ctl in cpu_times_list:
    print("################")
    print(ctl)
    print("User: 花费在用户进程上的时间 ",ctl.user)
    print("system: 花费在系统进程用的时间 ",ctl.system)
    print("idle: 空闲的时间 ",ctl.idle)
    print("interrupt(Windows): 硬件终端时间 ",ctl.interrupt)
    print("dpt(Windows): 延迟调用(学操作系统吧~) ",ctl.dpc)