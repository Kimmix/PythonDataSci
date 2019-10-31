def unique(inputList):
    unique_list = []
    for x in inputList:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


input_string = input("Enter a list separated by space => ")
myList = input_string.split()
print(unique(myList))
