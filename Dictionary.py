person=dict(Name="Mohanad", Age=25, Salary=8000)# mutable

print(person)
print(person["Name"])
print("Update Name")
person["Name"] = "Mohanad Djaber"
print(person["Name"])
print("add Insurance key")
person["Insurance"] = "Yes"
print(person)
print("delete age")
del person["Age"]
#person.pop("Age")
print(person)
#Print salary
print(person["Salary"])