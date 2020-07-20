# -*- coding: utf-8 -*-
# 文件名：window
# 创建日期：2020-7-20
import psutil
import platform
import re


def get_cpu_used(upu_base, interval=1):
    percent = psutil.cpu_percent(int(interval))
    if float(percent) > float(upu_base):
        print("CPU 使用率大于基线值预警: {}%".format(percent))
    else:
        print("CPU使用率正常：{}%".format(percent))


def get_mem_used(mem_base):
    mem = psutil.virtual_memory()
    if float(mem.percent) > float(mem_base):
        print("内存大于基线值预警: {}%".format(mem.percent))
    else:
        print("内存使用率正常：{}%".format(mem.percent))


def get_net_stats():
    tot_before = psutil.net_io_counters()
    status_before = psutil.net_if_stats()
    #print(psutil.net_if_stats())
    print("获取网络接口状态信息:",status_before)
    #print(status_before)


def check_process(process_names):
    res = ''
    names = set([i.strip().lower() for i in process_names.split() if i.strip()])
    all_process = set([p.name().lower() for p in psutil.process_iter()])
    diff_set = names - all_process
    #print(diff_set)
    if diff_set:
        for d in diff_set:
            res += '{} not running\n'.format(d)
    res = res or 'Normal, running'
    print("进程检查: ", res)



if __name__ == '__main__':
    upu_base =20  #CPU 基线值
    mem_base = 20  #内存基线值
    process_names =  'dwm.exe'# 进程名称
    get_cpu_used(upu_base, interval=5)
    get_mem_used(mem_base)
    check_process(process_names)
    get_net_stats()

