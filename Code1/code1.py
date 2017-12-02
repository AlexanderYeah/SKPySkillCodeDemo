#coding=utf-8;

from collections import OrderedDict

a = [1,5,7,2,1,6,5];

# 1 去除list的重复元素,用set 方法可以实现去重，但是去重 之后代码无序了
resa =  list(set(a));
# 结果为 [1, 2, 5, 6, 7]
print(resa);

"""
    要实现去重且保持原有顺序，如下方式。
    collections是Python内建的一个集合模块，提供了许多有用的集合类。
    OrderedDict 就是保证dict 的顺序

"""
resb = list(OrderedDict.fromkeys(a));
# 结果为 [1, 5, 7, 2, 6] 保持原有顺序
print(resb);


# 2 OrderedDict 的key 会按照插入的顺序排列 不是key本身的顺序
od = OrderedDict();
od['z'] = 9;
od['x'] = 6;
od['y'] = 3;
# 会按照key 插入的顺序进行返回
print(od.values());
print(od.keys());

"""
    自定义一个上设置容量的字典，超出限制，删除第一个元素
"""

# 3 OrderedDict 可以实现一个FIFO的dict，当容量超出限制的时候，先删除最早添加的key

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__();
        self._capacity = capacity;

    #  实现父类的setitem 方法
    def __setitem__(self, key, value):
        # 最新进来的key 是否已经包含
        containsKey = 1 if key in self else 0;
        # 看是否超出自己定义的容量
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=True);
            print('remove:',last);
        if containsKey:
            del self[key];
            print('set:',(key,value));
        else:
            print('add:',(key,value));
        OrderedDict.__setitem__(self,key,value);

od2 = LastUpdatedOrderedDict(3);

od2['a'] = 5;
od2['b'] = 9;
od2['c'] = 8;
od2['d'] = 2;
#当 self.popitem(last=False); 结果为[9, 8, 2] 超出容量的时候，删除第一个
#当 self.popitem(last=True); 结果为[5, 9, 2] 超出容量的时候，删除最后一个，再去添加新添加的内容
print(od2.values());





od3  = dict();
od3['n'] = 5;
od3['m'] = 9;
od3['l'] = 8;
od3['t'] = 2;
print(od3.values());












