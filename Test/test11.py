myList = list(range(1500, 2701))
ansList = []
for x in myList:
    if(x % 7 == 0):
        ansList.append(x)
print(ansList)

# print([x for x in range(1500, 2700) if x % 7 == 0])
