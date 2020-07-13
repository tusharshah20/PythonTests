#Exception handling or error handling
age = int(input('Age:'))
print(age)
#ValueError: invalid literal for int() with base 10: 'asd' and exit code 1(program crashed)

print('*'*50)
#lets print proper error message
try:
    age = int(input('Age:'))
    print(age)
except ValueError:
    print('Invalid value')
print('*'*50)
#lets print proper error message
try:
    age = int(input('Age:'))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')


