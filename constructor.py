class A:

    def __init__(self):
        # init is the initializer or constructor 
        # constructor always be defined whenever class is created 
        self.a = 'hello'
    
    def main(self):
        print(self.a)

# obj = A()
# obj.main()



class Addition:
    first = 0
    second = 0
    answer = 0
    
    def __init__(self,f,s) -> None:
        self.first = f
        self.second = s
    
    def display(self):
        print('first value = ',self.first)
        print('second value = ',self.second)
        print('answer = ',self.answer)
    
    def calculate(self):
        self.answer = self.first + self.second
        print(self.answer)

obj = Addition(20,50)
obj.display()
obj.calculate()

