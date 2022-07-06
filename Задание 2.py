from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)
        
class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5

class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3



a = Coat(54)
b = Suit(180)
print(a)
print(a.expense)
print(b.expense)