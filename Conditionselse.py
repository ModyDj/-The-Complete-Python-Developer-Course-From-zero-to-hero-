Number = int(input("enter number:"))
if(Number>0):
    print("Number is positive")
elif (Number < 0):
    print("Number is negative")
else:
    print("Number is zero")
#print("App is done")

Degree = int(input("enter number:"))
if(Degree>=90):
    print("Your score is A")
elif (Degree >=80 and Degree < 90):
    print("Your score is B")
elif (Degree >= 70 and Degree < 80):
    print("Your score is C")
elif (Degree >=60 and Degree < 70):
    print("Your score is D")

else:
    print("You Fail")
print("App is done")