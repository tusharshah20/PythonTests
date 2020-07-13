def greet_user2(fname,lname):
    print(f'Hi {fname} {lname}!')
    print('Welcome aboard')
#arguments to be passed are positional arguments
greet_user2("john","smith")
print('*'*40)
#keyword arguments imporve readability and order doesnt matter

#==================================
greet_user2(lname="john",fname="smith")
print('*'*40)
#keyword arguments always come after positional arguments
greet_user2("smith",lname="johny")


#calc_cost(total=50,shipping=5,discount=0.10)

