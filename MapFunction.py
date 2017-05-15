listItems = [1,2,3,4,5,6,7]
print(listItems)

# Without map
tempList= []
for item in listItems:
    tempList.append(item*2)
print(tempList)

# With map Multiply by 2
tempList2 = list(map(lambda x:x*2,listItems))
print(tempList2)

# with map add 3

tempList3 = list(map(lambda x:x+3,listItems))
print(tempList3)
