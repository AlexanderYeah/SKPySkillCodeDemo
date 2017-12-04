#coding=utf-8;

from collections import  deque,Counter,defaultdict

print("---------Section 1 deque--------");
"""
    一 deque：

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

print("---------Section 2  Counter--------");
"""
    Counter 是一个简单的计数器
    其本身也是Dict 的子类
"""
# 初始化 Counter
cnt = Counter();

for item in "Alexander":
    cnt[item] = cnt[item]+1;

print(cnt);

print("---------Section 3  defaultdict--------");
"""
    defaultdict属于内建函数dict的一个子类，调用工厂函数提供缺失的值。

"""
dd = defaultdict(lambda :'N/A')
dd['a'] = 1;
dd['b'] = 2;
# 如果对应的key 不存在 返回N/A
print(dd['c']);