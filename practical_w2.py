# 1
prices = [12.50, 8.99,15.00, 6.75, 22.30]
total = 0

for i in prices:
    total = total + i

print(prices)
print(total)

# 2
celsius = [0, 10, 20, 30, 40]
for i in celsius:
    print(f"{i}°C = {i* 9/5 +32}°F")

# 3

numbers = [5,10,15,20]
doubled = []
for i in range(len(numbers)):
    doubled.append(numbers[i]*2)

print(doubled)

# 4
countdown=[]
counter = 10
while counter > 0:
    countdown.append(counter)
    counter -=1
print(countdown)

# 5

items = ['bread', 'milk', 'eggs', 'butter']
prices = [2.50, 3.99, 4.25, 5.50]
for i in range(len(items)):
    print(f"{items[i]} costs ${prices[i]}")

# 6

grades = [4, 3, 4, 2, 3]
total = 0
count = 0

for i in grades:
    total = total +i
    count +=1
gpa = round(total/count,2)
print(gpa)

# 7

seconds = [245, 183, 312, 267, 198]
minutes = []
remaining_seconds = []

for i in seconds:
    minutes.append(i//60)
    remaining_seconds.append(i%60)
print(f"Seconds: {seconds}")
print(f"Minutes: {minutes}")
print(f"Remaining: {remaining_seconds}")

# 8

word = 'PYTHON'
for i in range(1,7):
    print(word[0:i])

# 9

scores = [85, 92, 78, 90, 88, 95, 83]
total = 0
count = 0

for i in scores:
    total = total+i
    count +=1
Average = total/count
print(f"Sum: {total}")
print(f"Count: {count}")
print(f"Average: {Average}")

# 10

matrix =  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        print(f"Row {y}, Col {x}: {matrix[y][x]}")

# 11

numbers = [1,2,3,4,5,6,7,8]
last_three = []

for i in range(len(numbers)-3, len(numbers)):
    last_three.append(numbers[i])

result = last_three
for i in range(len(numbers)-3):
    result.append(numbers[i])

print(f"Original:{numbers}")
print(f"Rotated:{result}")

# 12

values = [5, 3, 8, 2, 7]
prefix_sums = []
running_total = 0

for i in values:
    running_total = running_total+i
    prefix_sums.append(running_total)

print(f"Original: {values}")
print(f"Prefix Sums: {prefix_sums}")

# 13

matrix = []

for row in range(4):
    current_row = []
    for col in range(5):
        current_row.append(row * 5 + col)
    matrix.append(current_row)

for i in matrix:
    print(i)

# 14

words = ['the', 'quick', 'brown', 'fox']
length = []
first_letters = []

for i in words:
    length.append(len(i))
    first_letters.append(i[0])

print(f"Words:{words}")
print(f"Length:{length}")
print(f"First Letters:{first_letters}")

# 15

numbers = [2,3,4,5]
product = []
running_product = 1

for i in numbers:
    running_product = running_product * i
    product.append(running_product)

print(f"Original:{numbers}")
print(f"Running Product:{product}")

# 16

matrix = []
num = 0
MAX = 5

for i in range(MAX):
    ls = []
    for x in range(MAX):
        num +=1
        ls.append(num)
    matrix.append(ls)

for i in matrix:
    print(i)

# 17

table = []

for i in range(1,11):
    ls = []
    for x in range(1,11):
        ls.append(i*x)
    table.append(ls)

for y in range(len(table)):
    for x in range(len(table[y])):
        print(f"{table[y][x]}\t",end="")
    print()

# 18

count = 1
staircase = []
for y in range(1,7):
    row = []
    count +=1
    for x in range(1,count):
        row.append(x)
    staircase.append(row)

for i in staircase:
    print(i)

# 19

result = []

for block in range(1, 4):
    for num in range((block - 1) * 5 + 1, block * 5 + 1):
        for repeat in range(block):
            result.append(num)
print(result)