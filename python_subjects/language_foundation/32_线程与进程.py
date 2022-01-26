# -*- coding:utf8 -*-
"""
@author:natural
@file:32_线程与进程.py
@time:2022/01/24
"""

# 线程状态：
#
# New 创建
# Runnable 就绪。等待调度
# Running 运行
# Blocked 阻塞。阻塞可能在 Wait Locked Sleeping
# Dead 消亡

# 线程类型：
# 主线程
# 子线程
# 守护线程（后台线程）
# 前台线程

# 线程的创建
import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    print("End Main threading")


if __name__ == '__main__':
    main()

# join 方法：主线程结束后，子线程还在运行。那么我们需要主线程要等待子线程运行完后，再退出
import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    # 一次让新创建的线程执行 join
    for t in threads:
        t.join()

    print("End Main threading")


if __name__ == '__main__':
    main()

# 资源进行加锁：线程加载获取数据，通常都会造成数据不同步的情况

lock = threading.Lock()

# 线程中获取锁
lock.acquire()
# 释放锁
lock.release()

# 可重入锁（RLock）。RLock 内部维护着一个 Lock 和一个 counter 变量，counter 记录了 acquire 的次数，从而使得资源可以被多次 require。
# 直到一个线程所有的 acquire 都被 release，其他的线程才能获得资源
r_lock = threading.RLock()

# 生产者消费者模式

import threading
import time


class Consumer(threading.Thread):
    def __init__(self, cond, name):
        # 初始化
        super(Consumer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        # 确保先运行Seeker中的方法
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ': 我这两件商品一起买，可以便宜点吗')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我已经提交订单了，你修改下价格')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 收到，我支付成功了')
        self.cond.notify()
        self.cond.release()
        print(self.name + ': 等待收货')


class Producer(threading.Thread):
    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        # 释放对琐的占用，同时线程挂起在这里，直到被 notify 并重新占有琐。
        self.cond.wait()
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release()
        print(self.name + ': 发货商品')


cond = threading.Condition()
consumer = Consumer(cond, '买家（两点水）')
producer = Producer(cond, '卖家（三点水）')
consumer.start()
producer.start()

# 线程通信 一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列
from queue import Queue
from threading import Thread

isRead = True


def write(q):
    # 写数据进程
    for value in ['两点水', '三点水', '四点水']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)


def read(q):
    # 读取数据进程
    while isRead:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()

# Event 对象实现了简单的线程通信机制，它提供了设置信号，清除信号，等待等用于实现线程间的通信
import threading


class mThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        # 使用全局Event对象
        global event
        # 判断Event对象内部信号标志
        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName())
        else:
            print(self.getName())
            # 设置Event对象内部信号标志
            event.set()


# 生成Event对象
event = threading.Event()
# 设置Event对象内部信号标志
event.set()
t1 = []
for i in range(10):
    t = mThread(str(i))
    # 生成线程列表
    t1.append(t)

for i in t1:
    # 运行线程
    i.start()

# 后台线程 setDeamon

# multiprocessing 支持子进程、通信和共享数据、执行不同形式的同步，提供了 Process、Queue、Pipe、Lock 等组件

# 创建进程的类：Process([group [, target [, name [, args [, kwargs]]]]])
# target 表示调用对象
# args 表示调用对象的位置参数元组
# kwargs表示调用对象的字典
# name为别名
# group实质上不使用
import multiprocessing
import time


def worker(interval, name):
    print(name + '【start】')
    time.sleep(interval)
    print(name + '【end】')


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=(2, '两点水1'))
    p2 = multiprocessing.Process(target=worker, args=(3, '两点水2'))
    p3 = multiprocessing.Process(target=worker, args=(4, '两点水3'))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")

# 进程创建成一个类，当进程 p 调用 start() 时，自动调用 run() 方法。
import multiprocessing
import time


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()

# 进程中添加了 daemon 属性，那么当主进程结束的时候，子进程也会跟着结束
# 没有加 deamon 属性的例子
import multiprocessing
import time


def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print('【EMD】')

# 进程 p 添加 daemon 属性

import multiprocessing
import time


def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    print('【EMD】')

# join 方法的主要作用是：阻塞当前进程，直到调用 join 方法的那个进程执行完，再继续执行当前进程。

import multiprocessing
import time


def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print('【EMD】')

# 进程池的方法批量创建子进程
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))


if __name__ == '__main__':
    print('主进程的 PID：{0}'.format(os.getpid()))
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    # 等待所有子进程结束后在关闭主进程
    p.join()
    print('【End】')

# 进程通信:Process 之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python 的 multiprocessing 模块包装了底层的机制，提供了Queue、Pipes 等多种方式来交换数据

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    # 写数据进程
    print('写进程的PID:{0}'.format(os.getpid()))
    for value in ['两点水', '三点水', '四点水']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    # 读取数据进程
    print('读进程的PID:{0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw
    pw.start()
    # 启动子进程pr
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

