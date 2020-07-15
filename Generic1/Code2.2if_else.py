#1
x = int(input('enter a number:'))
if x>100:
    print('x was greater than expected')
elif x<=100 and x>=50:
    print('x is lesser than 100 but greater than 50')
elif x<50 and x>20:
    print('x is as expected')
else:
    print('x is not in category')

#2
#checking boolean
name = "john"
age = 20
is_new = False
if(is_new):
    print(name + ' ' + str(age))
else:
    print("he is not new")



