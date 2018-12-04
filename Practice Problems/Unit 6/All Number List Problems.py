# Length

length = 0
while int(input()) != 0:
    length += 1
print(length)

# Sum

sum = 0
a = int(input())
while a != 0:
    sum += a
    a = int(input())
print(sum)

# Average

length = 0
sum = 0
a = int(input())
while a != 0:
    sum += a
    length += 1
    a = int(input())
print(sum/length)

# Maximum

highest = 0
a = int(input())
while a != 0:
    if a > highest:
        highest = a
    a = int(input())
print(highest)

# Index of Maximum

index = 1
highest = 0
wanted = 1
a = int(input())
while a != 0:
    if a > highest:
        highest = a
        wanted = index
    a = int(input())
    index += 1
print(wanted)

# Number of Evens

counter = 0
a = int(input())
while a != 0:
    if a % 2 == 0:
        counter += 1
    a = int(input())
print(counter)

# Number of Elements Greater than Previous

counter = 0
a = int(input())
b = int(input())
while b != 0:
    if b > a:
        counter += 1
    a = b
    b = int(input())
print(counter)

# Second Highest

highest = 0
secondhighest = 0
a = int(input())
while a != 0:
    if a > highest:
        secondhighest = highest
        highest = a
    elif a > secondhighest and a < highest:
        secondhighest = a
    a = int(input())
print(secondhighest)

# Number of Elements Equal to Maximum

highest = 0
counter =0 
a = int(input())
while a != 0:
    if a > highest:
        highest = a
        counter = 1
    elif a == highest:
        counter += 1
    a = int(input())
print(counter)

# Max Number of Consecutive Equal Elements

highest = 1
counter = 1
a = int(input())
b = int(input())
while b != 0:
    if b == a:
        counter += 1
    else:
        if counter > highest:
            highest = counter
        counter = 1
    a = b
    b = int(input())
    if b == 0:
        if counter > highest:
            highest = counter
print(highest)