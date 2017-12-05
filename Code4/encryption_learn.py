#coding=utf-8;
import  base64
import hashlib
print("---------Section 1 base64--------");

bs_str = b"alexanderishandsome";
# 编码
bs_res = base64.b64encode(bs_str);
# b'YWxleGFuZGVyaXNoYW5kc29tZQ=='
print(bs_res);
# 解码
bs_decode_res = base64.b64decode(bs_res);
print(bs_decode_res);

#由于标准的base64编码可能出现 + /，在URL 中不能直接作为参数
# 在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
# url safe 的编码格式

bs_str2  = b'\xb7\x1d\xfb\xef\xff';
# b'tx377/8='
print(base64.b64encode(bs_str2));
# b'tx377_8='
print(base64.urlsafe_b64encode(bs_str2));
# b'\xb7\x1d\xfb\xef\xff'
print(base64.urlsafe_b64decode(base64.urlsafe_b64encode(bs_str2)));

print("---------Section 2 hashlib--------");
"""
    Python 的hashlib 提供了常见的摘要算法  MD5 SHA1
    摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
    md5(), sha1(), sha224(), sha256(), sha384(), and sha512()
"""
# 2.1 创建对象 md5
md5 = hashlib.md5();
# 2.2 更新 update
md5.update('what a day'.encode('utf-8'));
# 2.3 hexdigest 结果
print(md5.hexdigest());

# 如果内容过多 可以分多次进行update
md5_2 = hashlib.md5();
md5_2.update("what a wonderful sunny day".encode('utf-8'));
md5_2.update("let's to out to have a walk".encode('utf-8'));
print(md5_2.hexdigest());

