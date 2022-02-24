class Base:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age
    
    def getage(self):
        return self.age

class grandchild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self,name,age)
        self.address = address

    def getaddress(self):
        return self.address

obj = grandchild('rishav', 24, 'jassur')
print(obj.getname(), obj.getage(), obj.getaddress())
