# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/7/2 22:00

# # 打开文件 w模式(写模式)--文件不存在就新建
# f = open("text.txt", "w")
# # f = open("text.txt")
#
# # 将字符串写入文件中
# f.write("hello world,i am here!")
#
# # 关闭文件
# f.close()

# f = open("text.txt", "r")
#
# # read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
# content = f.read(5)
#
# print(content)
#
# content = f.read(10)
#
# print(content)
#
# f.close()

# f = open("text.txt", "r")
#
# # 一次性读取全部文件为列表，每行一个字符串元素
# content = f.readlines()
#
# # print(content)
#
# i = 1
# for temp in content:
#     print("%d:%s" % (i, temp))
#     i += 1
#
#
# f.close()

# f = open("text.txt", "r")
#
# content = f.readline()
# print("1:%s" % content, end=)
#
# content = f.readline()
# print("2:%s" % content)
#
# f.close()

import os

os.rename("text.txt", "text1.txt")
