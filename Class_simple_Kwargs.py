class car:
    def __init__(self, **kwargs):
        print("Great Object")
        self.__Data = kwargs
    #Type
    def GetType(self):
        return self.__Data["Type"]
    #Model
    def GetModel(self):
        return self.__Data["Model"]
    #Price
    def GetPrice(self):
        return self.__Data["Price"]
    #Miles Drive
    def GetMilesDrive(self):
        return self.__Data["MilesDrive"]
    #Owner
    def GetOwner(self):
        return self.__Data["Owner"]

    # Another Get price
    def GetCurrentPrice(self):
        return self.GetPrice() - (self.GetMilesDrive() * 10)

def main():
    myCar = car(Type="BMW", Model=1999, Price=23000, MilesDrive=15, Owner="Mohanad")
    CurrentPrice = myCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(myCar.GetOwner(),CurrentPrice))
    # Another Car
    AlexCar = car(Type="GMC", Model=1994, Price=34000, MilesDrive=8, Owner="Alex")
    CurrentPrice1 = AlexCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(AlexCar.GetOwner(), CurrentPrice1))


if __name__ == '__main__': main()
