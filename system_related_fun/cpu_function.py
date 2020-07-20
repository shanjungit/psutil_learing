# -*- coding: utf-8 -*-
# 文件名：cpu_function
# 创建日期：2020-7-17
__author__ = r'国信证券大连分公司'

import psutil as psu
from config import psutil as pps
# 返回一个包含CPU使用时长的元组(单位:秒) percpu=True 就调用 per_cputimes 显示每一个cpu的使用时间
cpu_times_list = psu.cpu_times(percpu=True)

for ctl in cpu_times_list:
    print("####CPU 使用情况 监控 ####")
    print(ctl)
    print("User: 花费在用户进程上的时间 ",ctl.user)
    print("system: 花费在系统进程用的时间 ",ctl.system)
    print("idle: 空闲的时间 ",ctl.idle)
    print("interrupt(Windows): 硬件终端时间 ",ctl.interrupt)
    print("dpt(Windows): 延迟调用(学操作系统吧~) ",ctl.dpc)


# 查看每一个CPU使用率， interval 指查询使用率间隔， percup指是否查询每一个cpu, 返回的第一个数值就是第一个cpu

def cpu_monitor(interval=5,percup=True, alert_num=20):
    while(True):
        cpu_percent_list = psu.cpu_percent(interval=interval,percpu=percup)
        print(cpu_percent_list)
        for index, item in enumerate(cpu_percent_list):
            print("第{}号cpu,使用率是{}%".format(index,float(item)))
            if float(item) > alert_num:
                print("警报，{}号CPU,超过了警戒值{}%".format(index,float(item)))



# 查看机器CPU数量， logagic = True 标识逻辑线程也显示
print("CPU数量-包括逻辑线程:{}".format(psu.cpu_count(logical=True)))
print("CPU数量-不包括逻辑线程:{}".format(psu.cpu_count(logical=False)))

# psutil.cpu_stats() 返回一个CPU状态的元组
# ctx_switched 自启动以来的上下文切换（自愿 + 非自愿）的数量
# interrupts: 中断
# soft_interrupts： 自启动以来软件中断的数量。始终设置为在 Windows 和 SunOS 上
# syscalls: 系统调用
def get_cpu_stats():
    print(psu.cpu_stats())

print(psu.cpu_freq(percpu=True))

# cpu_monitor(alert_num=10)

# get_cpu_stats()