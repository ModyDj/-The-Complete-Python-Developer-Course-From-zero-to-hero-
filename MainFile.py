import datetime

def main():
   #main code function
   #print("Hello")
   #import datetime
   DOB = int(input('Enter your DOB:'))
   CurrentYear = datetime.datetime.now().year
   Age = CurrentYear - DOB
   print('Your age is: {}'.format(Age))
if __name__ == '__main__':main()
