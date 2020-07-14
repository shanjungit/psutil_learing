from config import psutil as psu

# 使用 psutil.disk_partitions() 获取磁盘分区的信息；
print("使用 psutil.disk_partitions() 获取磁盘分区的信息；",psu.disk_partitions())

# 使用psutil.disk_usage('/')获取磁盘的使用情况；
print("使用psutil.disk_usage('/')获取磁盘的使用情况；",psu.disk_usage('/'))

# 使用psutil.disk_io_counters() 获取磁盘的IO统计信息（读写速度等）；
print("使用psutil.disk_io_counters() 获取磁盘的IO统计信息（读写速度等）；", psu.disk_io_counters())

