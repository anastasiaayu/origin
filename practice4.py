month= int(input("please enter a month: "))
if month>12 or month<1:
    print("please enter the correct number")
elif 1<=month<=3:
    print("spring")
elif 4 <= month <= 6:
    print("summer")
elif 7<=month<=9:
    print("autumn")
else:
    print("winter")