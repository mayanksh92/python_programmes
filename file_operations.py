import sys
import os

f1 = open('file1.txt','r+')
print(f1.name)
print(f1.readline())

#print(type(f1.read()))
# print(f1.read(10))
# print(f1.readlines(10))
#
# print(f1.read(10))

# print(f1.readline())
# print(f1.readline())
# print(f1.readline())

# for i in range(10):
#     print(f1.readline())
#
# for i in range(10):
#     # print(type(i))
#     print(f1.readline())

# with open('file1.txt','r') as f1:
#     print(f1.readline())

# for i in f1:
#     print(i)
#     print('#######')

#
#
# with open('file1.txt','r') as f2:
#     print(type(f2.read()))

# dict = {}
# for words in f1.read().split(' '):
#     if words in dict:
#         dict[words] += 1
#     else:
#         dict[words] = 1
# print(dict)


# dict = {}
# for words in f1.readlines():
#     for word in words.split(' '):
#         if word in dict:
#             dict[word] += 1
#         else:
#             dict[word] = 1
# print(dict)
#
# with open('file1.txt', 'r') as f:
#     for line in f.readline():
#         print (line)


# for i in f1.readlines():
#     print(i)


# while True:
#     print(f1.readline())
#     if not (f1.readline()):
#         break

# f2 = f1.read().split(' ')
# old = 'a'
# new = '######'
# print(f2.count('a'))
#
# for i in f2:
#     if i == old:
#         f2[f2.index(old)] = new
#         continue
# f3 = " ".join(f2)
# f1.seek(0)
# f1.write(f3)


l1 = ['a','b','c','d','e']
en = enumerate(l1,1)
print(type(en))
print(list(en))


for i,line in enumerate(f1,1):
    print(i,line)
    print(line.index(i))









