class Base1:
    def __init__(self):
        self.str1 = 'Geek1'
        print('Base1 init function')

class Base2:
    def __init__(self):
        self.str2 = 'Geek2'
        print('Base2 init function')

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print('Classes Called')

    def printscrn(self):
        print(self.str1,self.str2)

obj = Derived()
obj.printscrn()
        
        