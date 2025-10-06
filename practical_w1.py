# Practical W1

# 1. User Profile Generator

name = "Kevin"
age = 24
is_Student = True

str = "My name is " + name + ", I am "+str(age)+" years old, and my student status is "+ str(is_Student)+"."
print(str+"\n")

# 2. Dynamic Welcome Message

name = input("What is your name? ")
print(f"Hello, {name}, and welcome to Programming 1!\n")

# 3. String Repetition for Banners

token = input("input some characters: ")
# user can only input integers, otherwise re-enter
while True:
    try:
        time = int(input("input repetition: "))
        break
    except:
        print("integers only!")
print(token*time+"\n")

# 4. Course Information Display

course_code = "CS1032"
course_year = 2025
print(f"Current Course: {course_code}, Year: {course_year}\n")

# 5. Simple "Mad Libs" Game

noun = input("Please give a noun: ")
verb = input("Please give a verb: ")
adjective = input("Please give a adjective: ")

print(f"The {adjective} {noun} will {verb} tomorrow.")

# 6. Age Projection Calculator

while True:
    try:
        age = int(input("What is your age? "))
        break
    except:
        print("integers only!")
print(f"Your age in 10 years is {age+10}\nYour age 5 years ago is {age-5}")

# 7. Coffee Shop Bill Calculator

coffe_price = 2.8
while True:
    try:
        quantity = int(input("How many cups of coffee would you like? "))
        break
    except:
        print("integers only!")
print(f"The total cost for {quantity} coffees is £{coffe_price*quantity}.")

# 8. Celsius to Fahrenheit Converter

while True:
    try:
        Celsius = float(input("Enter a temperature in Celsius: "))
        break
    except:
        print("floats only!")

Fahrenheit = (Celsius * 1.8) + 32
print(f"{Celsius}℃ = {Fahrenheit}℉")

# 9. Restaurant Tip and Total

while True:
    try:
        meal = float(input("Enter the cost of meal: "))
        break
    except:
        print("floats only!")

tip = round(meal*0.2,2)     # Round to the second decimal
total = round(meal+tip,2)   # Round to the second decimal
print(f"Meal Cost: {meal}£\nTip: {tip}£\nTotal:{total}£")

# 10. Circle Geometry

PI = 3.14159
while True:
    try:
        radius = float(input("enter a radius: "))
        break
    except:
        print("float only!")
area = radius**2*PI
circumference = 2*PI*radius

print(f"The circle with a radius of {radius} has an area of {area} and a circumference of {circumference}.\n")

# 11. Seconds to Time Converter

while True:
    try:
        seconds = int(input("Enter a time in seconds: "))
        break
    except:
        print("integers only!")

H = seconds//3600
M = (seconds%3600)//60
S = (seconds%3600)%60

print(f"H:{H}, M:{M}, S:{S}")

# 12. Simple Compound Interest Calculator

init_amount = float(input("What is your initial amount? "))
interest = float(input("What is your annual interest (in %)? "))
interest = interest * 0.01
years = int(input("How many years are you saving?"))
final = round(init_amount*((1+interest)**years),2)

print(f"The final amout would be: {final}£.")

# 13. Body Mass Index (BMI) Application

height = float(input("What is your height in metres?"))
weight = float(input("What is your weight in kilograms?"))
BMI = round(weight/(height*height),1)
print(f"Your BMI is {BMI}")

# 14

A_PAINT = 11

length = float(input("What is the length of the wall?"))
width = float(input("What is the width of the wall?"))
wall_area = length*width

can_needed = int(wall_area//A_PAINT)
if wall_area%A_PAINT > 0:
    can_needed = can_needed +1
left_over = can_needed*A_PAINT-wall_area

print(f"A {wall_area} square metres wall requires {can_needed} cans of paint and {left_over} square metres of paint will be left.")

# 15. Three-Digit Number Reversal

while True:
    try:
        num = int(input("Enter a 3 digit integer:"))
        if num < 100 or num > 999:
            raise ValueError()
        break
    except:
        print("Only takes from 100~999")
first = num//100
second = ((num%100)*10)//100
third = ((num%100)*10)%100*10//100

print(f"{num} becomes {third}{second}{first}")

# 16. Road Trip Cost and Logistics

EFFICIENCY_PER_LITRE = 14   #km
CAPACITY = 55               #litre
FUEL_COST= 1.68             #£ per litre

distance = float(input("How many kms are you traveling?"))

Fuel_Needed = distance/14
Fuel_Needed = round(Fuel_Needed,4)
print(f"Fuel needed for {distance} km travel is {Fuel_Needed} litres")

Full_Tanks_Needed = int(Fuel_Needed//CAPACITY)
if Fuel_Needed%CAPACITY > 0:
    Full_Tanks_Needed = Full_Tanks_Needed+1
print(f"{Full_Tanks_Needed} full tanks needed for the travel.")

Cost = round(FUEL_COST*CAPACITY*Full_Tanks_Needed,2)
print(f"The total fuel cost is {Cost}£.")

# 17. Automated Recipe Scaler

FLOUR_FOR_12 = 250
SUGAR_FOR_12 = 175
BUTTER_FOR_12 = 110

num = int(input("How many cookies do you want?"))

flour = round(FLOUR_FOR_12/12*num,1)
sugar = round(SUGAR_FOR_12/12*num,1)
butter = round(BUTTER_FOR_12/12*num,1)

print(f"You will need {flour}g flour, {sugar}g sugar, and {butter}g butter for {num} cookies.")

# 18. 24-Hour Modular Clock

while True:
    try:
        time = int(input("Enter current hour: "))
        if time > 23 or time < 0:
            raise ValueError()
        break
    except:
        print("takes only from 0~23.")

while True:
    try:
        add = int(input("How many hours are you to add?"))
        if add < 0:
            raise ValueError()
        break
    except:
        print("takes only positive integers and 0!")
new_time = (add%24 + time)%24
print(f"It is {time}:00, and you add {add} hours, the new time is {new_time}:00")

# 19. Investment Doubling Time (Rule of 72)

init_amount = float(input("What is your initial amount?"))
annual_interest = float(input("Annual Interest Rate:"))
Current = 2025
Time = int(72//annual_interest)
print(f"Your £{init_amount} investment at {annual_interest}% will double in approximately {Time} years, in the {Current+Time}.")

# 20. Multi-Currency Exchange Desk
EUR = 1.18
USD = 1.27
JPY = 191.50

gbp = float(input("Enter a Sterling amount:"))

eur = round(gbp*EUR,2)
usd = round(gbp*USD,2)
jpy = round(gbp*JPY,2)

print(f"£{gbp} is equivalent to {eur} EUR, {usd} USD, and {jpy} JPY")

# Practical W2

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