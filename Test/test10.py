ppap = {'Apple': 1.5, 'Pine Apple': 3, 'Pen': 1}
print(sorted(ppap.items(), key=lambda x: x[1]))
print(sorted(ppap.items(), key=lambda x: x[1], reverse=True))
