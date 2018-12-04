# My Solution

a = input()
wanted = ""
off = 0
for i in range(0,len(a)-1):
    if a[i+1] == ".":
      wanted += "0"
      off = 1
    elif off == 1:
      wanted += a[i]
wanted += a[len(a)-1]
dp = 0
for i in range(0,len(wanted)):
    if wanted[i] == ".":
        dp += 1
if dp == 0:
    wanted = 0
print(wanted)

# Intended Solution

x = float(input())
print(x - int(x))