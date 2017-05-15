

class Mercedes:
     def SetName(self, name):
         self.__name = name
     def GetName(self):
         return self.__name

def main():
    u1= Mercedes()
    u1.SetName('Benz')
    print(u1.GetName())



if __name__ == '__main__':main()
