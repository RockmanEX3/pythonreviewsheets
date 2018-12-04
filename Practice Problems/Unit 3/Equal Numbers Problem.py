# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())
counter = 0
if a==b:
    counter+=1
if a==c:
    counter+=1
if b==c:
    counter+=1
if counter==1:
    print(2)
else:
    print(counter)