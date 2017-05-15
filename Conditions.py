import datetime
DOB =int(input('Enter your DOB:'))
CurrentYear = datetime.datetime.now().year
Age =CurrentYear - DOB

if (Age>= 18):
 print('Your age is: {} and you are Adult'.format(Age))

#if (Age < 18):
# print('Your age is: {} and you are not Adult'.format(Age))
#print("App is done")

if (Age < 18):
 print('Your age is: {} and you are not Adult'.format(Age))
print("App is done")