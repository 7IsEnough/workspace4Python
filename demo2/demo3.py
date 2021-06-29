# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/29 22:09


# # 创建空的元组
# tup1 = ()
#
# # 这个不是元组，这个是整型
# # tup2 = (50)
# # tup2 = (50,)
# tup2 = (50, 60, 70)
#
# print(type(tup1))
# print(type(tup2))

# tup1 = ("abc", "def", 2000, 2020, 333, 444, 555, 666)
#
# print(tup1[0])
# # 访问最后一个元素
# print(tup1[-1])
# # 左闭右开，进行切片
# print(tup1[1:5])


# # 增加(连接)
# tup1 = (12, 34, 56)
# tup2 = ("abc", "xyz")
# tup = tup1 + tup2
# print(tup)


# # 删除
# tup1 = (12, 34, 56)
# print(tup1)
# # 删除了整个元组变量
# del tup1
# print("删除后：" + tup1)

# 修改 不能改
# tup1 = (12, 34, 56)
# # 报错，不允许修改
# tup1[0] = 100


# 字典的定义
info = {"name": "明凯", "age": 18}

# # 字典的访问
# print(info["name"])
# print(info["age"])
#
# # 访问了不存在的键
# # 直接访问会报错
# # print(info["gender"])
# # 使用get方法没有找到对应的键，默认返回None
# # print(info.get("gender"))
# # 没找到可以设定默认值
# print(info.get("age", 20))
# print(info.get("gender", "m"))


# # 增加
# newID = input("请输入新的学号：")
# info["id"] = newID
# print(info["id"])

# 删除
# del

# print("删除前：%s" % info["name"])
#
# del info["name"]

# 删除了指定键值对后，再次访问会报错
# print("删除后：%s" % info["name"])

# print("删除前：%s" % info)
#
# del info

# 删除字典后再访问，报错
# print("删除后：%s" % info)

# clear 清空
# print("清空前：%s" % info)
#
# info.clear()
#
#
# print("清空后：%s" % info)


# 修改

# info["age"] = 20
# print(info["age"])


# 查询
# # 得到所有的键(列表)
# print(info.keys())
#
# # 得到所有的值(列表)
# print(info.values())
#
# # 得到所有的项(列表)，每个键值对是一个元组
# print(info.items())

# # 遍历所有的键
# for key in info.keys():
#     print(key)


# # 遍历所有的值
# for value in info.values():
#     print(value)


# # 遍历所有的键值对
# for key, value in info.items():
#     print("key=%s, value=%s" % (key, value))


# 使用枚举函数，同时拿到列表中的下标和元素内容
myList = ["a", "b", "c", "d"]

for i, x in enumerate(myList):
    print(i+1, x)







