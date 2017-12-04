#coding=utf-8;

from collections import  deque

"""
    deque：

    list 按照索引访问数据很快，但是去增加删除元素就很慢了，因为list 是线性存储，数据量
    大的时候，插入和删除的效率很低。
     deque 是为了实现高速插入和删除的双向列表，适用于队列和栈

"""

q = deque(['a','b','c']);
# 末位添加一个元素
q.append('q');
# 向左添加元素
q.appendleft('o');

# 删除末位的元素
q.pop();
# 删除第一个元素
q.popleft()


# 结果为 (['a', 'b', 'c'])
print(q);