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
        self._age = 40
    def display(self):
        print(self._age)

class subclass(Protecte_Mebers):
    def display_(self):
        print(self._age)

obj1 = Protecte_Mebers()
obj1.display()

#Private Members
class Private:
    def __init__(self):
        self.__degree = 'Btech'
    def display(self):
        print(self.__degree)

class Private_subclass(Private):
    def modify(self):
        self.deg = self.__degree
    def display_modify(self):
        print(self.deg)

obj2 = Private()
obj3 = Private_subclass()




# Python code to illustrate how double
# underscore at the beginning works
class Geek:
    def __init__(self):
        self.g = self.Pyth()

    def _single_method(self):
        print("Single")
    def __double_method(self): # for mangling
        print("fgfsgs")
    class Pyth:
        def __init__(self):
            self.name = "arunava"
        def __double_method(self): # for mangling
            pass

mangling = Geek()
mangling._single_method()
print(mangling.g.name)