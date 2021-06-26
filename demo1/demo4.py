# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/26 18:51

# for i in range(5):
#     print(i)

# 从0开始，到10结束，步进值为3  (每次加3)
# for i in range(0, 10, 3):
#     print(i)

# for i in range(-10, -100, -30):
#     print(i)

# name = "chengdu"
#
# for x in name:
#     print(x, end="\t")

# a = ["aa", "bb", "cc", "dd"]
# for i in range(len(a)):
#     print(i, a[i])


# i = 0
# while i < 5:
#     print("当前是第%d次执行循环" % (i + 1))
#     print("i=%d" % i)
#     i += 1

# n = 100
# result = 0
# counter = 1
# while counter <= n:
#     result += counter
#     counter += 1
#
# print("1到 %d 的和为：%d" % (n, result))

# count = 10
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于或等于5")


# i = 0
# while i < 10:
#     i += 1
#     print("-"*30)
#     if i == 5:
#         # 结束整个while循环
#         break
#     print(i)


# i = 0
# while i < 10:
#     i += 1
#     print("-"*30)
#     if i == 5:
#         # 结束本次循环
#         continue
#     print(i)


# 九九乘法表
for i in range(1, 10, 1):
    for j in range(1, i + 1, 1):
        if j == i:
            print("%d*%d=%d" % (i, j, i * j), end="\n")
        else:
            print("%d*%d=%d" % (i, j, i * j), end="\t")
