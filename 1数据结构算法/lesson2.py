#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@function:
@modify: chris.chen

"""
import heapq

"""
    源码解析
"""


class PriorityQueue:
    """
        PS: 优先级队列，以优先级对元素排序，每次pop返回优先级最高的
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print("Should be bar:", q.pop())
    print("Should be spam:", q.pop())
    print("Should be foo:", q.pop())
    print("Should be grok:", q.pop())


# Example use
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


def finding_the_largest_or_smallest_n_items():
    """
        PS: 找出最大或者最小的N个元素
        todo: 很多计算类函数(max,min等)中，都支持key参数传入一个函数
    """
    cheap = heapq.nsmallest(5, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(5, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)


if __name__ == '__main__':
    # a = [6, 0, 1, 3, 5]
    # """
    #     heapify()方法，通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）
    # """
    # heapq.heapify(a)
    # while True:
    #     print(heapq.heappop(a))

    # 优先队列
    test_priority_queue()

    # 找到最大or最小的n个元素
    finding_the_largest_or_smallest_n_items()
