import time


class QueueElement(object):

    def __init__(self, ele, delay=0):
        self.ele = ele
        self.delay = delay
        self.expire = time.time() + delay

    def __str__(self):
        return 'Element: %s expire: %s' % (self.ele, self.expire)

    def __eq__(self, other):
        return self.expire == other.expire

    def __lt__(self, other):
        return self.expire < other.expire

    def ready(self):
        return self.expire <= time.time()
