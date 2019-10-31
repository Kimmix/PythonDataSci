def maxThree(inputList):
    inputList.sort(reverse=True)
    return inputList[0:3]


input_string = input("Enter a list separated by space => ")
myList = input_string.split()
print(maxThree(myList))
