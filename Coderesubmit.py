inp = input()
inputlist = list(inp)



length = len(inputlist) - 1
newlist = []



while length >= 0:
    newlist.append(inputlist[length])
    length = length - 1

if inputlist == newlist:
    print("palindrome")
    print(inputlist)
    print(newlist)

else:
    print("Not A Palindrome")
    print(inputlist)
    print(newlist)