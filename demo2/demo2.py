# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/28 21:50

import random

# # 定义一个空的列表
# name = []
#
nameList = ["小张", "小王", "小李"]
#
# print(nameList[0])
# print(nameList[1])
# print(nameList[2])
#
# # 列表中可以存储混合类型
# testList = [1, "测试"]
#
# print(testList[0])
# print(testList[1])
# print(type(testList[0]))
# print(type(testList[1]))

# for name in nameList:
#     print(name)
#
# # len()可以得到列表的长度
# length = len(nameList)
# i = 0
# while i < length:
#     print(nameList[i])
#     i += 1


# # 增加：append
# print("----------增加前，名单列表的数据")
# for name in nameList:
#     print(name)
#
# nameTemp = input("请输入添加学生的姓名：")
# # 在末尾追加一个元素
# nameList.append(nameTemp)
#
#
# print("----------增加后，名单列表的数据")
# for name in nameList:
#     print(name)

# # 增加  extend
# a = [1, 2]
# b = [3, 4]
# # 将列表当做一个元素，加入到a列表中
# a.append(b)
# print(a)
#
# # 将b列表中的每个元素，逐一追加到a列表中
# a.extend(b)
# print(a)


# # 增加 insert
# a = [0, 1, 2]
# # 指定下标位置插入元素
# # 第一个变量表示下标，第二个变量表示对象
# a.insert(1, 3)
# print(a)

# # 删除：del  pop  remove
# movieName = ["加勒比海盗", "黑客帝国", "第一滴血", "指环王", "速度与激情", "指环王"]
#
# print("----------删除前，电影列表的数据")
# for name in movieName:
#     print(name)
#
# # 在指定位置删除一个元素
# # del movieName[2]
# # 弹出末尾最后一个元素
# # movieName.pop()
# # 直接删除指定内容的元素，有重复内容只删除第一个
# movieName.remove("指环王")
#
# print("----------增加后，电影列表的数据")
# for name in movieName:
#     print(name)


# # 修改：
#
# print("----------修改前，名单列表的数据")
# for name in nameList:
#     print(name)
#
# # 修改指定下标的元素内容
# nameList[1] = "小红"
#
#
# print("----------修改后，名单列表的数据")
# for name in nameList:
#     print(name)


# # 查询： in  not in
# findName = input("请输入你要查找的姓名：")
#
# if findName in nameList:
#     print("在学员名单中找到了相同的名字")
# else:
#     print("没有找到")


# myList = ["a", "b", "c", "a", "b"]
# # 可以查找指定下标范围的元素，并返回找到对应数据的下标
# print(myList.index("a", 1, 4))
# # 范围区间左闭右开，找不到就报错
# print(myList.index("a", 1, 3))

# # 统计某个元素出现几次
# print(myList.count("c"))


# # 排序和反转
# a = [1, 4, 2, 3]
# print(a)
# # 将列表所有元素反转
# a.reverse()
# print(a)
# # 升序排序
# a.sort()
# print(a)
# # 降序排序
# a.sort(reverse=True)
# print(a)


# 有三个元素的列表，每个元素都是一个空列表
# schoolNames = [[], [], []]

# schoolNames = [["北京大学", "清华大学"], ["南开大学", "天津大学", "天津师范大学"], ["山东大学", "中国海洋大学"]]
#
# print(schoolNames[0][0])
#
# offices = [[], [], []]
# names = ["A", "B", "C", "D", "E", "F", "G", "H"]
#
# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
#
# i = 1
# for office in offices:
#     print("办公室%d 的人数为：%d" % (i, len(office)))
#     i += 1
#     for name in office:
#         print("%s" % name, end="\t")
#     print("\n")
#     print("-" * 20)

# 案例
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]

# print("-"*6 + "商品列表" + "-"*6)
# i = 0
# for product in products:
#     print(str(i) + "\t" + product[0] + "\t"*2 + str(product[1]))
#     i += 1

productList = []


while True:
    number = input("请输入你想要的商品编号：")
    if number == "q":
        break
    else:
        productList.append(products[int(number)])

print("您购买的商品为：")
i = 0
price = 0
for product in productList:
    print(str(i) + "\t" + product[0] + "\t"*2 + str(product[1]))
    price += product[1]
    i += 1

print("总价为：%d" % price)

