# find longest word in list of lists and find length

# example table
tableData = [['apples', 'oranges', 'cherries', 'banana', 'melon'],
             ['Alice', 'Bob', 'Carol', 'David', 'Chris'],
             ['dogs', 'cats', 'moose', 'goose', 'armadillo']]


'''main solution to find longest word in list of lists'''
colWidths = max((word for row in tableData for word in row), key=len)
print(colWidths)     

'''find the length of the longest word'''
colWidths = max(len(word) for row in tableData for word in row)
print(colWidths)

'''Alternative solution for finding longest word'''
colWidth = [len(max(col, key=len)) for col in tableData]
colWidth = max(colWidth)
print(colWidth)