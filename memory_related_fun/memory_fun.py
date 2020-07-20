# -*- coding: utf-8 -*-
# 文件名：memory_fun
# 创建日期：2020-7-20
__author__ = r'国信证券大连分公司'

from config import psutil as psu


# 获取内存使用情况
def get_memory():
    mem = psu.virtual_memory()
    print(mem)
    total = round(float(mem.total)/(1024**3),2) # 1024的3次方
    avalibale = round(float(mem.available/(1024**3)),2)
    used = round(float(mem.used/(1024**3)),2)

    print("总共有{}G, 可用{}G, 已用{}G".format(total,avalibale, used))


# 获取内存使用百分率,默认超过60就会发生警告
def get_memory_alert(mem_base=60):
    mem = psu.virtual_memory()
    if float(mem.percent) > float(mem_base):
        print("内存大于基线值预警: {}%".format(mem.percent))
    else:
        print("内存使用率正常：{}%".format(mem.percent))



# get_memory
get_memory()
get_memory_alert()