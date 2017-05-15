#Immutable:
#1-Integer:

print("Immutable")
print()
print("1- Integer")
print()
x = 10
print(id(x))
print(type(x))

x = 11
print(id(x))
print(type(x))
print()
print("---")
print()
#2- Float
print("2- Float")
print()
x = 1.0
print(id(x))
print(type(x))

x = 1.1
print(id(x))
print(type(x))
print()
print("---")
print()
#3- Strings
print("3- Strings")
print()
x= "Mohanad"
print(id(x))
print(type(x))
x= "Mohanad Djaber"
print(id(x))
print(type(x))
print()
print("---")
print()
#4- Tuples
print("4- Tuples")
print()
x= ("Mohanad", "x", "Rock")
print(id(x))
print(type(x))
x= ("Mohanad", "x", "Rock", "Star")
print(id(x))
print(type(x))
print()
print("---------------------------------------------------------------------------------------")
print()
#Mutable:
#1-Dictionary:

print("Mutable")
print()
print("1- Dictionary")
print()
x =dict(Name=3, Age=4, Salary=5)
print(id(x))
print(type(x))

x =dict(Name=3, Age=4, Salary=5)
print(id(x))
print(type(x))
print()
print("---")
print()
#2- List
print("2- List")
print()
x = [1, 4, 5, 6]
print(id(x))
print(type(x))

x = [1, 4, 5, 6]
print(id(x))
print(type(x))
print()
print("---")
print()