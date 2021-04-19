#!usr/bin/env python
# _*_ coding:utf_8 _*_
"""
@function:
@modify: chris.chen
"""


def common_key():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print('Common keys:', a.keys() & b.keys())
    print('Keys in a not in b:', a.keys() - b.keys())
    print('(key,value) pairs in common:', a.items() & b.items())

    item = zip([1, 2, 3], ['a', 'b', 'c'])
    print(dict(item))


def grouping_reNcords_together_based_on_a_field():
    """
        数据分组
        将数据列表数据根据某个字段值，进行分组
    """
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    from itertools import groupby
    sorted(rows, key=lambda a: a["date"])
    iter = groupby(rows, key=lambda a: a["date"])
    for i in iter():
        print(i)


if __name__ == '__main__':
    grouping_reNcords_together_based_on_a_field()
