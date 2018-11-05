# Calculation based on first reach time

h = float(input("Type h: "))
a = float(input("Type a: "))
b = float(input("Type b: "))

days = 1
height = 0
if a>b: # Prevent infinite loop
    while True:
      height += a
      if height >= h:
        break
      height -= b
      days += 1
    print(days)