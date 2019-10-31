input_string = input("Enter a list separated by space => ")
myList = input_string.split()
listSum = 0

for x in myList:
    listSum += int(x)
print(listSum)
