print(1+3)
print(1+3-2)
x=1
y=3
print(x+y)
print(x)
print(y-x)
# Bitwise {By logic Gates (Or, And)}
x = 0b101
y = 0b111
print(x+y)
print(x&y)
print(x|y)
# Formula of the converting from number to 0 and 1 Language
def f (n): return (print('{:08b}'.format(n)))

print(f(5))
print(f(5<<2))

print("------------------")

print(True)
x= True
y = False
print(x and y)
print("1 ---")
print(x & y)
print("2 ---")
print(x or y)
print("3 ---")
print(x | y)
print("4 ---")
print(True and False)
print("5 ---")
print(True and True)
print("6 ---")
print(False and False)
print("7 ---")
print(True or True)
print("8 ---")
print(True or False)
print("9 ---")
print(3<5)
print("10 ---")
print(3>5)
print("11 ---")
print(3<=5)
print("12 ---")
print(3>=5)
print("13 ---")
x= 5
print(x <=1)
print("14 ---")
print(x <=10)
print("15 ---")
print((x >=1)and (x <=10))
print((x <=1)and (x <=10))
print("16 ---")
x=0b101
y=0b111
print(y and x )
print(f(x and y))
print(f(x or y))