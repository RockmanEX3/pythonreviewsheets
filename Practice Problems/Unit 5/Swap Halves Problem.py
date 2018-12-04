import math

word = input()
string = ""
string += word[math.ceil(len(word)/2)::1]
string += word[0:math.ceil(len(word)/2)]
print(string)

'''
2 --> 1
5 --> 3
6 --> 3
7 --> 4
'''