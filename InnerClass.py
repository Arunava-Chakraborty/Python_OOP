'''
Multiple Mul;tilevel inner classes are demonstrated here
'''

class Color:
    def __init__(self):
        self.name = 'Red'
        self.green = self.Green()
        self.blue = self.Blue()

    def print_(self):
        print(self.name)

    class Green:
        class Lightgreen:
            def __init__(self):
                self.color = 'LightGreen'
            def show(self):
                print(self.color)

        def __init__(self):
            self.lg = self.Lightgreen()
            self.name = 'Green'
            self.code = 'o0567dfr'
        def show(self):
            print('Inner class name',self.name)
            print('Inner class code',self.code)

    class Blue:
        def __init__(self):
            self.navy = self.NavyBlue()
            self.name = 'Blue'
            self.code = 'odjd09890jnksd'

        def show(self):
            print(self.name)
            print(self.code)

        class NavyBlue:
            def __init__(self):
                self.name = 'NavyBlue'
                self.code = 'fgn0348xlvjkn'
            def show(self):
                print(self.name)
                print(self.code)

obj1 = Color()
obj1.print_()

obj2 = obj1.Blue.NavyBlue()
obj2.show()