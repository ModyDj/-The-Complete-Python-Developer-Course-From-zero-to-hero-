class car:
    def __init__(self):
        print("Great Object")
    #Type
    def SetType(self, type):
        self._Type=type
    def GetType(self):
        return self._Type

    #Model
    def SetModel(self, Model):
        self._Model=Model
    def GetModel(self):
        return self._Model

    #Price
    def SetPrice(self, price):
        self._Price=price
    def GetPrice(self):
        return self._Price
    #Another Get price
    def GetCurrentPrice(self):
        return self._Price-(self._MilesDrive*10)

    #Miles Drive
    def SetMilesDrive(self, milesDrive):
        self._MilesDrive=milesDrive
    def GetMilesDrive(self):
        return self._MilesDrive

    #Owner
    def SetOwner(self, owner):
        self._Owner=owner
    def GetOwner(self):
        return self._Owner

def main():
    myCar = car()
    myCar.SetType("BMW")
    myCar.SetModel("1999")
    myCar.SetPrice(23000)
    myCar.SetMilesDrive(15)
    myCar.SetOwner("Mohanad")
    CurrentPrice = myCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(myCar.GetOwner(),CurrentPrice))

    AlexCar = car()
    AlexCar.SetType("GMC")
    AlexCar.SetModel("1994")
    AlexCar.SetPrice(34000)
    AlexCar.SetMilesDrive(8)
    AlexCar.SetOwner("Alex")
    CurrentPrice1 = AlexCar.GetCurrentPrice()
    print("{}'s car, New Price {}".format(AlexCar.GetOwner(), CurrentPrice1))


if __name__ == '__main__': main()
