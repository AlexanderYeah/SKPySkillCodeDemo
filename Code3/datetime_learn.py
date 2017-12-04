#coding=utf-8;
from datetime import datetime,timedelta,timezone


"""
    datetime 是python 内部处理时间的标准库
    datetime 还包括一个datetime的类，如果要只导入datetime的，则需要import datetime.datetime

"""

#1 获取当前的时间
now_str = datetime.now();
# 打印结果  2017-12-04 21:29:18.664763
print(now_str);

#2 获取指定日期的时间 构造时间
dt_str = datetime(2017,12,4,20,22);
# 打印结果 2017-12-04 20:22:00
print(dt_str);

# 3 转换为时间戳 python的时间戳是一个浮点数，如果小小数位，则代表毫秒数
# 1512390120.0
dt_stamp = dt_str.timestamp()
print(dt_stamp);

# 4 时间戳转换
print(datetime.fromtimestamp(dt_stamp));

# 5 用户输入的日期和时间是字符串，要处理时间和日期，必须把str 转化为 datetime
# datetime.strptime()
# 规定了 %Y-%m-%d %H:%M:%S 日期和时间的部分格式
cur_str = datetime.strptime('2017-12-4 21:25:38','%Y-%m-%d %H:%M:%S');
print(cur_str);

# 6 将datetime 对象格式化字符串展示给用户
show_str = now_str.strftime('%Y-%m-%d %H:%M:%S');
# 打印结果 2017-12-04 21:44:29
print(show_str);

# 7 对datetime 进行+ 或这个 -,需要使用timedelta这个类
# 当前时间
now = datetime.now();
# 1小时之后的时间
ten_hours_later = now + timedelta(hours=1);
# 打印结果 2017-12-04 22:48:17.524844
print(ten_hours_later);

# 一天之前的时间
two_hours_ago = now  - timedelta(days=1);
# 打印结果 2017-12-03 21:49:43.132842
print(two_hours_ago);







