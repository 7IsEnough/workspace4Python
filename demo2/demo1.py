# -*- coding = utf-8 -*-
# @Author: 97694
# @Time: 2021/6/27 12:42

# word = '字符串'
# sentence = "这是一个句子"
# paragraph = '''
#     这是一个段落
#     可以由多行组成
# '''
#
# print(word)
# print(sentence)
# print(paragraph)

# # my_str = "I'm a student"
# my_str = 'I\'m a student'
# print(my_str)


# # my_str = "Jason said \"I like you\""
# my_str = 'Jason said "I like you"'
# print(my_str)


str1 = "chengdu"

print(str1)
print(str1[0])
# [起始位置：结束位置：步进值]
print(str1[0:5])
print(str1[1:7:2])
print(str1[5:])
print(str1[:5])

print(str1 + ",你好")
print(str1 * 3)

# 使用反斜杠，实现转义字符的功能
print("hello\nchengdu")
# 字符串前面加r，字符串里的\不进行转义，直接输出
print(r"hello\nchengdu")
