i=1
while(i<=10):
    if (i%2==1):
    #if (i % 2 == 0):
      print("number{}".format(i))
    #i+=1
    i+=2
print("App is done")

print("-------------------")

#for i in range(5):
#    print(i)

l = [1,2,3,"hi",55,92]
for item in range(6):
    #print(item)
    #print(l[0])
    print("index.[{}]={}".format(item,l[item]))
    #print(l[item])

print("App is done")

print("-------------------")

print("Nested Loop")

i=0
while(i<5):
    print("i={}".format(i))
    i+=1
    j=0
    while(j<5):
        if(i==j):
        #print("j={}".format(j))
         print("(i,j)=({},{})".format(i,j))
        j+=1
    i+=1


print("-------------------")

print("Control loops")

word="Python"
for letter in word:
    #print(letter)
    if(letter=='t'):
        #break;
        continue;
    print(letter)
print("App is done")

l =[1,33,45,32,55,22,23,100]
for item in l:
    if(item==55):
        print("number is found")
        break;