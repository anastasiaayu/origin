'''
#获取列表中所有元素
list02=list("我是齐天大圣")
for i in list02:
    print(i)
#不建议
#重新创建列表
for i in list02[::-1]:
    print(i)


for i in range(5,-1,-1):
    print(list02[i])
'''
list_name=[]
while True:
    name=input("请输入你在西游记中最喜欢的角色： ")
    if name=="":
        print("'孙悟空"
          "猪八戒"
          "唐僧"
          "沙和尚"'')
        break
    else:
        list_name.append(name)
        print(list_name)
