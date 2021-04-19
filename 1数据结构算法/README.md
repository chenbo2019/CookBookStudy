## 场景

## lesson1
* 有限长度队列，保存有限的历史记录
```
from collections import deque
deque(maxlen={length})
```
* 计算列表中出现次数最多的元素(python计算器模块)
```
from collections import Counter
相关方法：
most_common(n)              统计出现最多次数的n个元素
elements()                  返回一个Counter计数后的各个元素的迭代器                           
update ({CounterObj})       类似集合的update,进行合并                                 
subtract ({CounterObj})     合并，但是是减法**           
```

## lesson2
### python 堆算法模块
```
    一种著名的数据结构是堆（heap），它是一种优先队列。优先队列让你能够以任意顺序添加对象，
并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。相比于列表方法min，这样做的效率要高得多。
特性：
    位置i处的元素总是大于位置i // 2处的元素（反过来说就是小于位置2 * i和2 * i + 1处的元素）。
    这是底层堆算法的基础，称为堆特征（heap property）。
python实现：
    heapq
    相关方法：
    heappush(heap, x)                                        将x压入堆中
    heappop(heap)                                      从堆中弹出最小的元素
    heapify(heap)                                           让列表具备堆特征
    heapreplace(heap, x)                            弹出最小的元素，并将x压入堆中
    nlargest(n, iter)                                       返回iter中n个最大的元素
    nsmallest(n, iter)                                   返回iter中n个最小的元素
```
* 找到最大或者最小的N个元素
```python
import heapq
heapq.nsmallest()
heapq.nlargest()
```
* 优先级队列 
```
import heapq
class PriorityQueue:
    """
        PS: 优先级队列，以优先级对元素排序，每次pop返回优先级最高的
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heappop(self._queue)[-1]                                   
```

## lesson3
* 查找字典共同key
```
a = {}
b = {}
a.keys() & b.keys()
```
* 列表数据根据某字段分组
```
from itertools import groupby
groupby(iterater, key=xxx)
```
* 多值字典
```
from collections import defaultdict
a = defaultdict(list)
a["a"].append("123")
a["a"].append("345")
```

