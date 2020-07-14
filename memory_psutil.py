from config import psutil as psu

# 使用psutil.virtual_memory() 获取系统内存的使用情况；
print("使用psutil.virtual_memory() 获取系统内存的使用情况；",psu.virtual_memory())

# 使用 psutil.swap_memory()获取系统交换内存的统计信息；
print("使用 psutil.swap_memory()获取系统交换内存的统计信息；",psu.swap_memory())


