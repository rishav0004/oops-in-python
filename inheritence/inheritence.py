# inheritence is the cpability of one class to derive 
# or inherit the properties of another class

class Person:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def isEmployee(self):
        return False


class Employee(Person):
    
    def isEmployee(self):
        return True


obj = Person('geek1')
print(obj.getname(),obj.isEmployee())

obj2 = Employee('geek2')
print(obj2.getname(),obj2.isEmployee())
