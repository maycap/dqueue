DelayQueue
~~~~~~~~~~

轻量级延迟队列，参考JAVA DelayQueue实现，采用Heap排序实现。


安装
~~~~

::

   pip install dqueue

使用
~~~~

队列并不限制元素类型，可以放入任何类型进行延迟消费

.. code:: commandline

    import time

    from dqueue import DelayQueue, QueueElement


    q = DelayQueue()
    e1 = QueueElement("study", 3.2)
    e2 = QueueElement("meet", 1.5)
    q.put(e1)
    q.put(e2)

    while 1:
        msg = q.get()
        print("%s consumer: %s" %(msg, time.time()))

测试验证
~~~~~~~~

.. code:: commandline

   python -m dqueue.tests
