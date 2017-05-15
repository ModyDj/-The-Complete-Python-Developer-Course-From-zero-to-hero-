x = "Hanouchi"
print(type(x))
x = "10"
print(type(x))
print(x)
F = float(x)
print(type(F))
print(F)
x = 10
print(type(x))
z = str(x)
print(type(z))
print(z)

# str, int, float, long, list, set(), dict(), tuple()
print('---------------------')
# Slice:
print('Slice')
I =[1, 45, 11, 12, 123, 50]
print(I[0])
print(I[1])
print(I[0:2])
print(I[0:3])
print(I[0:])
print(I[:-1])
print(I[2:5])
I[:] = range(10)
print(I)
print(I[3:7])
I[:] = range(100)
print(I)
I[0:4] = (0, 0, 0, 0)
print(I)
x=10
print(type(x))
y=10.5
print(type(y))
z = int(y)
print(z)
print(type(z))
c = float(x)
print(type(c))
v = "1234"
print(v)
print(type(v))
print(complex(2,3))

print('---------------------')
# Slice:
print('Debug')

import datetime
DOB = input("Enter your DOB:")
CurrentYear = datetime.datetime.now().year
Age = CurrentYear - int(DOB)
print("Your Age is {}".format(Age))
