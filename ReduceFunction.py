from functools import reduce
listItems=[1,2,3,4,5,6,7,8,9,10]
print(listItems)

sum = 0

for item in listItems:
    sum = sum + item
print(sum)

# With reduce

sum1 = reduce(lambda x,y:x+y,listItems)
print(sum1)

sum2 = list(map(lambda x:x+3, listItems))
print(sum2)
sum3 = list(filter(lambda x:x%2==1, listItems))
print(sum3)
