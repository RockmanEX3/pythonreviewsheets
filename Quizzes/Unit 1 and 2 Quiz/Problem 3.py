# Assuming numbers have leading zeroes (10 results in 01 not 1)

given = input("Type two digit number: ")
if len(given) == 2:
  print(given[1] + given[0])