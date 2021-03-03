#ABSTRACTION

from abc import ABC, abstractmethod


class Subscriber(ABC):
    def purchasePrice(self, amount):
        print("Your intial processing fee: ",amount)

    @abstractmethod                 #function tells us to pass in an argument, but not what kind of data it will be
    def price(self, amount):        #abstract class not instantiated, requires subclasses
        pass                    
                                    
class Monthly(Subscriber):          #subclass inherits Subscriber attributes 
    def price(self, amount):        #utilizes @abstractmethod with price function from parent class
        print('Your monthly order of: {}.'.format(amount))

class Yearly(Subscriber):         
    def price(self, amount):
        print('Your discounted yearly order of: {}'.format(amount))

    

              
obj = Monthly()
obj.purchasePrice("$10")
obj.price("$50")

obj = Yearly()
obj.purchasePrice("$10")
obj.price("$500")



