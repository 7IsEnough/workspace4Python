# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/30 21:23


# # 函数的定义
# def printInfo():
#     print("-------------------------")
#     print("   人生苦短，我用Python   ")
#     print("-------------------------")
#
#
# # 函数的调用
# printInfo()

# # 带参数的函数
# def add2Num(a, b):
#     c = a + b
#     print(c)
#
#
# add2Num(11, 22)

# # 带返回值的函数
# def add2Num(a, b):
#     # 通过return返回计算结果
#     return a + b
#
#
# print(add2Num(11, 22))

# # 返回多个值的函数
# def divid(a, b):
#     shang = a / b
#     yushu = a % b
#     # 多个返回值用逗号分隔
#     return shang, yushu
#
# # 需要使用多个值来保存返回内容
# shang, yushu = divid(5, 2)
# print("商：%d, 余数：%d" % (shang, yushu))

# # 打印一条线
# def function1():
#     print("-" * 20)
#
#
# # 根据用户输入的数字，打印相应数量的线条
# def function2(lineNumber):
#     for i in range(1, lineNumber + 1):
#         function1()
#
#
# # 求3个数的和
# def function3(a, b, c):
#     return a + b + c
#
#
# # 求3个数的平均值
# def function4(a, b, c):
#     return function3(a, b, c) / 3
#
#
# # function1()
# # function2(int(input("请输入打印行数：")))
# # print(function3(1, 2, 3))
# print(function4(1, 2, 3))


# 全局变量和局部变量

# def test1():
#     # 局部变量
#     a = 300
#     print("test1-----修改前：a=%d" % a)
#     a = 100
#     print("test1-----修改后：a=%d" % a)
#
#
# def test2():
#     # 不同的函数可以定义相同的名字，彼此无关
#     a = 500
#     print("test2-----：a=%d" % a)
#
#
# test1()
# test2()


# # 全局变量
# a = 100
#
#
# def test1():
#     print(a)
#
#
# def test2():
#     # 调用全局变量a
#     print(a)
#
#
# test1()
# test2()

# 全局变量和局部变量相同名字

# a = 100
#
#
# def test1():
#     # 局部变量优先使用
#     a = 300
#     print("test1-----修改前：a=%d" % a)
#     a = 100
#     print("test1-----修改后：a=%d" % a)
#
#
# def test2():
#     # 没有局部变量，默认使用全局变量
#     print("test2-----：a=%d" % a)
#
#
# test1()
# test2()


# 在函数中修改全局变量

a = 100


def test1():
    # 声明全局变量在函数中的标识符
    global a
    print("test1-----修改前：a=%d" % a)
    a = 200
    print("test1-----修改后：a=%d" % a)


def test2():
    # 没有局部变量，默认使用全局变量
    print("test2-----：a=%d" % a)


test1()
test2()
