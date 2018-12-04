def capitalize(phrase):
    wordlist = phrase.split(" ")
    for i in range(0,len(wordlist)):
        wordlist[i] = wordlist[i][0].upper() + wordlist[i][1:]
    return " ".join(wordlist)
print(capitalize(input()))