import threading
import time
from heapq import heappush, heappop, heapify

from dqueue.element import QueueElement


class DelayQueue(object):

    def __init__(self):
        self.queue = []
        self.mutex = threading.Lock()
        self.ready = threading.Condition(self.mutex)

    def peek(self):
        if len(self.queue):
            return self.queue[0]
        return None

    def put(self, ele):
        if ele.delay < 0:
            raise ValueError("'delay' must be a non-negative number")

        with self.ready:
            first = self.peek()
            heappush(self.queue, ele)
            min_ele = self.peek()
            if not first or first != min_ele:
                self.ready.notify()

    def put_msg(self, msg, delay=0):
        if delay < 0:
            raise ValueError("'delay' must be a non-negative number")

        ele = QueueElement(msg, delay)
        with self.ready:
            first = self.peek()
            heappush(self.queue, ele)
            min_ele = self.peek()
            if not first or first != min_ele:
                self.ready.notify()

    def get(self, only_msg=False):
        while 1:
            with self.ready:
                first = self.peek()
                if not first:
                    self.ready.wait()
                first = self.peek()
                if first.ready():
                    heappop(self.queue)
                    return first.ele if only_msg else first
                else:
                    self.ready.wait(first.expire - time.time())

    def remove(self, ele):
        with self.mutex:
            if ele in self.queue:
                self.queue.remove(ele)
                heapify(self.queue)

    def clear(self):
        with self.mutex:
            self.queue.clear()
