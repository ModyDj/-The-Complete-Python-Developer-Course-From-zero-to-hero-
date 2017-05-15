class car:
    def __init__(self, type, Model, price, milesDrive, owner):
        print("Great Object")
        self._Type = type
        self._Model = Model
        self._Price = price
        self._MilesDrive = milesDrive
        self._Owner = owner
    #Type
    def GetType(self):
        return self._Type
    #Model
    def GetModel(self):
        return self._Model
    #Price
    def GetPrice(self):
        return self._Price
    #Another Get price
    def GetCurrentPrice(self):
        return self._Price-(self._MilesDrive*10)
    #Miles Drive
    def GetMilesDrive(self):
        return self._MilesDrive
    #Owner
    def GetOwner(self):
        return self._Owner

def main():
    myCar = car("BMW",1999,23000,15,"Mohanad")
    CurrentPrice = myCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(myCar.GetOwner(),CurrentPrice))
    # Another Car
    AlexCar = car("GMC",1994,34000,8,"Alex")
    CurrentPrice1 = AlexCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(AlexCar.GetOwner(), CurrentPrice1))


if __name__ == '__main__': main()
