from config import psutil as psu
import time
# 获取网络信息
# while(True):
#     time.sleep(3)
print("使用psutil.net_io_counters()获取总的网络IO信息:",psu.net_io_counters())

# 使用 psutil.net_io_counters(pernic=True)获取网卡的IO信息
print(psu.net_io_counters(pernic=True))

# 使用 psutil.net_if_addrs() 获取网络接口信息
print("使用 psutil.net_if_addrs() 获取网络接口信息",psu.net_if_addrs())