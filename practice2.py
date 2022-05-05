#列表
'''
1.创建列表

'''
list01 = ["齐天大圣", 100, True]
list02=list("我是齐天大圣")

'''
获取元素
1 索引
2 切片
append 追加
insert 插入
添加元素
删除
remove
'''

print(list01[2])
print(list02[2:6])

list02.append("坐骑")
print(list02)
list02.insert(2,"True")
print(list02)
list02.remove("True")
print(list02)
del list02[0]
print(list02)
list02.remove("是")
print(list02)
del list02[-1]
print(list02)
list02[0:2]=["a","b"]

print(list02)