#coding=utf-8;

import os,time,random
import subprocess

from multiprocessing import Process,Pool,Queue



print("---------Section 1  Python 实现多进程--------");
"""
    Python 实现多进程，首先要知道操作系统的相关知识：
    简单来讲：
    Unix/Linux 操作系统提供了一个fork()的系统调用。普通的书调用，调用一次，返回一次.
    但是fork的调用时调用一次，返回两次，因为操作系统自动把当前的进程（父进程）复制一份为子进程，然后分别在
    父进程和子进程中进行返回。

    子进程 永远返回0 ，而父进程返回子进程的ID。这样的话，一个父进程可以fork 出很多子进程。所以父进程要记下
    每一个子进程的ID，而子进程调用getppid() 就可以获取父进程的ID

    Python os 模块封装了常见的系统调用，包括fork
"""

# print('Process %s start...'%os.getpid());

# 而父进程返回子进程的ID
# pid = os.fork();
# if pid == 0:
#     # 返回值为0 证明有开启子进程
#     print("this is process %s and my parrent is %s"%(os.getpid(),os.getppid()));
# else:
#     # 不为0 证明没有开启进程
#     print("i %s just create a child process %s"%(os.getpid(),pid));

"""
打印结果:
i 81622 just create a child process 81623
this is process 81623 and my parrent is 81622
"""


print("---------Section 2 Process--------");
"""
    multiprocessing 模块提供了一个Process 类 来代表一个进程对象
"""

# def run_process(name):
#     print("Run child process %s (%s)..."%(name,os.getpid()));
#
# if __name__ == '__main__':
#     print("parrent process %s"%os.getpid());
#     # 创建多进程 传入执行的函数 以及函数的参数
#     p = Process(target=run_process,args=('test',));
#     print("child process will start");
#     # 启动
#     p.start();
#     # 等待子进程执行完毕 接着往下执行
#     p.join();
#
#     print('child process end');

"""
    打印结果
    parrent process 81851
    child process will start
    Run child process test (81852)...
    child process end
"""

print("---------Section 3 Pool--------");

"""
    如果需要大量对的子进程，可以用进程池的方式批量创建子进程

    Pool 的默认大小是核数

"""

def long_time_task(name):
    print("Run task is %s %s..." % (name,os.getpid()));
    start = time.time();
    time.sleep(random.random() * 3);
    end = time.time();
    print('Task %s runs %0.2f seconds' %(name,(end - start)));
# if __name__ == '__main__':
#     # 获悉父进程的ID
#     print("Parrent process %s,"%os.getpid());
#     p = Pool(4);
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,));
#     # 等待所有的子进程完成
#
#     # 调用close 之后就不能在添加新的process了
#     p.close();
#     # 等待所有的子进程执行完毕 调用join 之前必须先调用close
#     p.join();
#     print("All subprocess done");

"""
    打印结果 ：
    ---------Section 3 Pool--------
Parrent process 82100,
Run task is 0 82101...
Run task is 1 82102...
Run task is 2 82103...
Run task is 3 82104...
Task 3 runs 0.20 seconds
Run task is 4 82104...
Task 4 runs 1.21 seconds
Task 1 runs 1.61 seconds
Task 0 runs 1.83 seconds
Task 2 runs 1.89 seconds
All subprocess done



"""

print("---------Section 4 子进程--------");
"""
    subprocess 模块可以快速的启动一个县城 然后控制其输入和输出
    subprocess包主要功能是执行外部的命令和程序。比如说，我需要使用wget下载文件。我在Python中调用wget程序。从这个意义上来说，subprocess的功能与shell类似。

"""
# 执行nslookup 就是相当于打开了命令行 执行nslookup  www.python.org 命令
print('$ lookup www.python.org');
# call 函数，父进程等待子进程完成，返回退出信息
r  = subprocess.call(['nslookup','www.python.org']);
# 打印退出信息为 0
print('exit code:',r);

# 父进程等待子进程完成 返回0 检查退出信息，如果returncode不为0，则举出错误
r2 = subprocess.check_call('ls',shell=True);
print(r2);


print("---------Section 5 进程间的通信--------");
"""
    process 之间是需要通信的 ，有多种的通信机制 Queue Pips 等多种方式进行数据的交换
"""

# Queue

def write(q):
    print("Process to write:%s"%os.getpid());
    for value in ['A','B','C']:
        print('Put %s to queue ...'%value);
        # 将值放进queue
        q.put(value);
        time.sleep(random.random());

def read(q):
    print("Process to read:%s"%os.getpid());
    while True:
        # 将值从queue取出
        value = q.get(True);
        print('Get %s from queue',value);

if __name__ == '__main__':
    # 父进程创建Queue，并且传递给各个子进程
    q = Queue();
    process_w = Process(target=write,args=(q,));
    process_r = Process(target=read,args=(q,));
    # 启动子进程 写
    process_w.start();
    # 启动子进程 读
    process_r.start();
    # 等待写进程结束
    process_w.join();
    # pr 是 死循环 直接让其终止
    process_r.terminate();

"""
打印结果：

Process to write:83173
Put A to queue ...
Process to read:83174
Get %s from queue A
Put B to queue ...
Get %s from queue B
Put C to queue ...
Get %s from queue C

"""

