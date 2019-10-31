input_string = input("Enter a list separated by space => ")
myList = input_string.split()
sorted_list = []

for i in range(len(myList)):
    minIndex = i
    for j in range(i+1, len(myList)):
        if myList[minIndex] > myList[j]:
            minIndex = j

    tmp = myList[i]
    myList[i] = myList[minIndex]
    myList[minIndex] = tmp
print(myList)
