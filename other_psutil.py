
# 参考博文： https://blog.csdn.net/qq_38684504/article/details/87956015
from config import psutil as psu
import datetime
import random

print("获取系统开机时间，转换为自然格式:",datetime.datetime.fromtimestamp(psu.boot_time()).strftime("%Y-%m-%d %H: %M: %S"))

# 获取链接系统的用户列表
print("获取连接系统的用户列表:",psu.users())

# 获取系统全部进程的id
print("获取系统全部进程的id: ",psu.pids())

# 获取单个进程的信息,随机获取一个id号~
pid_m=psu.pids()
# random_pid = random.randint(0,len(pid_m)-1)
# print(random_pid)
# p = psu.Process(pid_m[random_pid])
# print("进程名字：",p.name())
# print("进程bin的路径:",p.exe())
for t_p_num in pid_m[:11]:
    if t_p_num == 0: continue  # TODO: 还没搞懂为什么0号 进程不能访问
    # print(t_p_num)
    try:
        t = psu.Process(t_p_num)
        print("##################################################################")
        print("进程ID:%s 进程名字:%s, 进程路径:%s" % (t_p_num, t.name(), t.exe()))
        print("父进程:%s,子进程:%s,进程状态:%s,进程用户名%s"%(t.parent(),t.children(),t.status(),t.username()))
        print("进程创建时间:%s,进程使用CPU的时间：%s,进程使用的内存：%s,进程使用的数量%s"
              %(datetime.datetime.fromtimestamp(t.create_time()).strftime("%Y-%m-%d %H: %M: %S"),t.cpu_times(),t.memory_info(),t.num_threads()))
        print("进程工作的绝对路径:%s, 进程的命令行:%s" % (t.cwd(),t.cmdline()))
    except psu.AccessDenied:
        print("%s 进程不能被访问"%t.name())



