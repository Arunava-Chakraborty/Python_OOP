#Public Members
class Public:
    def __init__(self):
        self.name = 'john'
    def display_name(self):
        print(self.name)

obj = Public()
obj.display_name()
print(obj.name)

#protected Members
class Protecte_Mebers:
    def __init__(self):
        self.__age = 40
    def display(self):
        print(self.__age)

class subclass(Protecte_Mebers):
    def display_(self):
        print(self.__age)

obj1 = Protecte_Mebers()
obj1.display()

#Private Members
