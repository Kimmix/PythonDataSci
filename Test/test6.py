input_string = input("Enter a list separated by space => ")
myList = input_string.split()
even_list = []
for x in myList:
    if (int(x) % 2) == 0:
        even_list.append(x)
print(even_list)
