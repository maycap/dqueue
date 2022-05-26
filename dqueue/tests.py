import random
import threading
import time

from dqueue import QueueElement, DelayQueue


def consumer(d):
    while 1:
        task = d.get()
        print("thread: %s consumer: %s, now: %s" % (threading.current_thread().native_id, task, time.time()))


def start_consumer(d, n):
    for _ in range(n):
        t = threading.Thread(target=consumer, args=(d,))
        t.start()


def producer(d):
    tid = threading.current_thread().native_id
    for i in range(1000):
        ts = random.random()
        d.put(QueueElement(ele='%s_%s' % (tid, i), delay=ts))
        time.sleep(0.001)


def start_producer(d, n):
    for _ in range(n):
        t = threading.Thread(target=producer, args=(d,))
        t.start()


if __name__ == '__main__':
    d = DelayQueue()
    start_consumer(d, 4)
    start_producer(d, 2)
