N = int(input())
i = 1
string = ""
while i**2 <= N:
    string += str(i**2) + " "
    i += 1
print(string)