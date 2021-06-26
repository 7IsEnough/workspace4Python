# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/26 11:21

# # if True:
# if 1:
#     print("True")
#     print("Answer")
# else:
#     print("False")
# print("end")

# score = 67
#
# if 90 <= score <= 100:
#     print("本次考试·等级为A")
# elif 80 <= score < 90:
#     print("本次考试·等级为B")
# elif 70 <= score < 80:
#     print("本次考试·等级为C")
# elif 60 <= score < 70:
#     print("本次考试·等级为D")
# # else:    #else 和 elif一起使用
# elif 0 <= score < 60:
#     print("本次考试·等级为E")

# sex = 1  # 1代表男生，0代表女生
# single = 1  # 1代表单身，0代表有男/女朋友
#
# if sex == 1:
#     print("男生")
#     if single == 1:
#         print("我给你介绍一个吧?")
#     else:
#         print("你给我介绍一个吧?")
# else:
#     print("女生")
#     print("...")

# 引入随机库
import random

# 随机生成[0,2]的随机数，包含0,1,2三个数字
x = random.randint(0, 2)
print(x)
