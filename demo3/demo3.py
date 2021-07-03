# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/7/3 15:24

# # 捕获异常
# try:
#     print("-------test------1----")
#     # 用只读模式打开了一个不存在的文件，报错，发生异常
#     f = open("123.txt", "r")
#     # 这句代码不会被执行
#     print("-------test------2----")
#
# # 文件没找到，属于IO异常(输入输出异常)
# except IOError:
#     # 捕获异常后执行的代码
#     pass


# try:
#     print(num)
# # except IOError:
# # 异常类型想要被捕获，需要一致
# except NameError:
#     print("产生错误了")


# try:
#     print("-------test------1----")
#     # 用只读模式打开了一个不存在的文件，报错，发生异常
#     f = open("123.txt", "r")
#     # 这句代码不会被执行
#     print("-------test------2----")
#
#     print(num)
# # except IOError:
# # 异常类型想要被捕获，需要一致
# # 将可能产生的所有异常类型，都放到下面的小括号中
# except (NameError, IOError):
#     print("产生错误了")


# # 获取错误描述
# try:
#     print("-------test------1----")
#     # 用只读模式打开了一个不存在的文件，报错，发生异常
#     f = open("123.txt", "r")
#     # 这句代码不会被执行
#     print("-------test------2----")
#
#     print(num)
# # except IOError:
# # 异常类型想要被捕获，需要一致
# # 将可能产生的所有异常类型，都放到下面的小括号中
# except (NameError, IOError) as result:
#     print("产生错误了")
#     print(result)


# # 捕获所有的异常
# try:
#     print("-------test------1----")
#     # 用只读模式打开了一个不存在的文件，报错，发生异常
#     f = open("123.txt", "r")
#     # 这句代码不会被执行
#     print("-------test------2----")
#
#     print(num)
# # except IOError:
# # Exception可以承接任何异常
# except Exception as result:
#     print("产生错误了")
#     print(result)


# # try。。finally  和嵌套
# import time
#
# try:
#     f = open("123.txt", "r")
#
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
#         print("文件关闭")
#
# except Exception as result:
#     print("发生异常...")
#     print(result)


def function1():
    try:
        f = open("gushi.txt", "w", encoding="utf-8")
        f.write("床前明月光\n")
        f.write("疑是地上霜\n")
        f.write("举头望明月\n")
        f.write("低头思故乡\n")
    except Exception as result:
        print("出现异常")
        print(result)
    finally:
        f.close()


def function2():
    try:
        f1 = open("gushi.txt", "r", encoding="utf-8")

        f2 = open("copy.txt", "w", encoding="utf-8")

        try:
            while True:
                content = f1.readline()
                if len(content) != 0:
                    print(content)
                    f2.write(content)
                else:
                    break
            print("复制完毕")
        finally:
            f1.close()
            f2.close()
    except Exception as result:
        print("出现异常")
        print(result)


# function1()
function2()
