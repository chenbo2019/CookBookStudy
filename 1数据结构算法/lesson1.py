#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@function:
@modify: chris.chen
"""
import heapq
from collections import deque

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


def limited_history_data():
    """
        PS: 有限长度队列，保存有限的历史记录
        deque,maxlen定义了固定长度队列，有新记录加入时会自动移除老的记录
    """
    previous_lines = deque(maxlen=5)
    for i in range(10):
        previous_lines.append(i)
    print(previous_lines)


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter


def determine_the_top_n_items_occurring_in_a_list():
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)
    # outputs [('eyes', 8), ('the', 5), ('look', 4)]

    # 合并数据
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords)
    print(word_counts.most_common(3))


if __name__ == '__main__':
    # limited_history_data()
    determine_the_top_n_items_occurring_in_a_list()
