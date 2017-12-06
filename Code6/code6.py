#coding=utf-8;

import itertools

"""
    itertools提供了非常有用的用于操作迭代对象的函数。

"""
print("---------Section 1 count()--------");
# 1 count 会创建一个无限迭代器 打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
# base = itertools.count(1);
# for n in  base:
#     print(n);
print("---------Section 2 cycle()--------");
# 2 cycle 会将传入的一个序列无线重复下去
# cl = itertools.cycle("ALEX"); # 字符串也是序列的一种形式
# for c2 in cl:
#     print(c2);
print("---------Section 3 repeat()--------");
# 3 repeat 负责把一个元素无线重复下去，第二个参数可以限制重复次数
# 打印3次d
r3 = itertools.repeat('d',3);
for i in r3:
    print(i);
print("---------Section 4 chain()--------");
#4 chain 可以把一组对象串联起来，形成一个强大的迭代器
# 4.1 将字符串拼接起来
chain4 = itertools.chain('YSK','ALEX');
for i in  chain4:
    print(i);
# 4.2 将list 拼接起来
for i in itertools.chain([1,2,3],[9,8,7]):
    print(i);

print("---------Section 4 groupby()--------");
# 5 groupby 把迭代器相邻的重复元素跳出来放在一起

for key,group in itertools.groupby('yyySSSkkk'):
    """
y ['y', 'y', 'y']
S ['S', 'S', 'S']
k ['k', 'k', 'k']
    """
print(key,list(group));












