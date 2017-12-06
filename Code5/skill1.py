#coding=utf-8;

import socket
import pdb
import sys
print("---------Section 1 使用三元操作符--------");
""" 1 使用三元操作符 赋值
    [表达式为真的返回值] if [表达式] else [表达式为假的返回值]

"""
# 1
b1 = 8
a1 = 15 if(b1 == 10) else 20;
print(a1);

# 1.1 链式求最小值
def get_small(a2,b2,c2):
    return a2 if(a2<b2 and a2 < c2) else (b2 if(b2 < c2) else c2);

print(get_small(1,5,8));

# 1.2 列表推导中使用三元运算符：
# 前边等于是筛选的条件
list1 = [a3*2 if (a3 < 5) else a3 * 4 for a3 in range(5)];
print(list1);

print("---------Section 2 多行字符串使用技巧--------");

# 2.0 普通的多行可以使用三个引号
str2 = """this
is
me""";
print(str2);
#分为多行并且将整个字符串包含在括号中
print("this"
      "is"
      "me"
      "test");

print("---------Section 3 使用列表初始化多个变量--------");
list3 = [9,6,3];
x3,y3,z3 = list3;
# 打印结果：x3=9,y3=6,z3=3
print("x3=%s,y3=%s,z3=%s"%(x3,y3,z3));

print("---------Section 4 打印引入模块的文件路径--------");
# 如果要知道引入模块的路径
# <module 'socket' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py'>
print(socket);

print("---------Section 5 断点调试--------");
"""
    引入pdb 模块
"""
# 设置断点
#pdb.set_trace();
print("break there")

print("---------Section 6 运行时检测 Python 版本--------");
# sys.version_info(major=3, minor=5, micro=0, releaselevel='final', serial=0)
# 代表3.5 版本的
print(sys.version_info);