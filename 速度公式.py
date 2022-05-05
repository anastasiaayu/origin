'''
first_velocity=int(input("please enter the first velocity: "))
time=int(input("please enter the time: "))
a=int(input("please enter a: "))
distant=first_velocity*time+a*time**2/2
print(distant)
'''
whole_second=int(input("please enter a number of second: "))
hour=whole_second//360
minute=whole_second//60
second=whole_second%60
print("this time is "+str(hour)+" hour "+str(minute)+" minute "+str(second)+" second")