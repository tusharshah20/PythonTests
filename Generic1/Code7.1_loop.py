#using for loop
for item in [1,2,3,4]:
    print(item)
print('#' * 30)

#example 2
stock_prices = [11,12,13,15,19]
total = 0
for price in stock_prices:
    total += price
print(f"Total: {total}")
avgprice = total/len(stock_prices)
print(f"Avgprice: {avgprice}")
print('#' * 30)

#Nested Loops
#Generating coordinates
for x in range(4):
    for y in range(2):
        print(f'({x},{y})')

print('#' * 30)

#Printing a pattern
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)
print('#' * 30)

#Printing a pattern using nested loops
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


