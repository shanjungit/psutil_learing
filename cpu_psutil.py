from config import psutil as psu
import time

# 使用psutil.cpu_times()获取CPU的完整信息
print("使用psutil.cpu_times()获取CPU的完整信息: ",psutil.cpu_times())

# 使用psutil.cpu_count()获取CPU的逻辑个数
print("使用psutil.cpu_count()获取CPU的逻辑个数：",psutil.cpu_count())

# psutil.cpu_count(logical=False)获取CPU的物理个数；默认logical值为True；
print("psutil.cpu_count(logical=False)获取CPU的物理个数；默认logical值为True；", psutil.cpu_count(logical=False))

# psutil获取系统CPU使用率的方法是cpu_percent(),其有两个参数，分别是interval和percpu；
# interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率；
for x in range(10):
    print(psu.cpu_percent(interval=1))
for x in range(10):
    print(psu.cpu_percent(interval=1,percpu=True))


