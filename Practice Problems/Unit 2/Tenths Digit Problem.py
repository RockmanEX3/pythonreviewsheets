# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = input()
wanted = ""
for i in range(0,len(a)):
    if a[i] == ".":
        wanted = a[i+1]
if len(wanted) == 0:
    wanted = "0"
print(wanted)