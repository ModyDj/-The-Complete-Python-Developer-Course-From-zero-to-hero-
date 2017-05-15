class User:
    def __init__(self, userName, Age):
        print("Great Job")
        self.__UserName= userName
        self.__Age = Age
    def GetUserName(self):
        return self.__UserName
    def GetAge(self):
        return self.__Age


def main():
    u1 = User("Mohanad", 25)
    u2 = User("Loshi", 7)
    print("{}'s has {} Years Old".format(u1.GetUserName(), u1.GetAge()))
    print("{}'s has {} Years Old".format(u2.GetUserName(), u2.GetAge()))

if __name__ == '__main__': main()
