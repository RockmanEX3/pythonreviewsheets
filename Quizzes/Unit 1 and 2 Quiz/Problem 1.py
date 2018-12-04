name = input("Type name: ")
shape = input("Type pool shape (rectangular prism or cylinder): ")
if shape == "rectangular prism":
  length = float(input("Type length"))
  width = float(input("Type width"))
  height = float(input("Type height"))
  volume = 7.5 * length * width * height
  print(name + " needs " + str(volume) + " gallons")
if shape == "cylinder":
  radius = float(input("Type radius"))
  height = float(input("Type height"))
  volume = 5.875 * 3.14 * radius * radius * height
  print(name + " needs " + str(volume) + " gallons")