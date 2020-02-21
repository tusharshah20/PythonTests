#finding greatest number in the list
numbers = [10,3,6,2,8,4]
print(max(numbers))

#
#assuming number at 0 index is max
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f" max is {max}")

#