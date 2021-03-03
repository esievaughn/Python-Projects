
#ENCAPSULATION

class Bike:
    def __init__(self):
        self._wheelCount = 2                #protected variable defined int
        self._tireType = "Mountain"         #private variable defined str
        self.__bikeRegistration = 234972    #private variable defined int

    def getbikeReg(self):
            print(self.__bikeRegistration)

    def setbikeReg(self, private):
        self.__bikeRegistration = private

obj = Bike()
obj._tireType = "road"
print(obj._tireType)                #changed protected variable outside of the class

obj.__bikeRegistration = 2983       #changed bike registration number outside of the class
obj.getbikeReg()                    #does not work becuase it is private, so registration number stays the same as the original input

obj.getbikeReg()            
obj.setbikeReg(2983)                #set and get methods to change private variable
obj.getbikeReg()                    #registration number is changed to input 2983


