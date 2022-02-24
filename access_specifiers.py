# public a = 10
# protected _a = 20
# private __a = 30

class A:
    a = 10  #public
    _b = 20 #protected
    __c = 30 #private

    def a1(self): #public function
        print('a1') 
    
    def _b1(self):   #protected function
        print('b1')
    
    def __c1(self):  #private function
        print('c1')
    
    def _display(self): #private variables and function can be when called inside the public or protected functions
        print(self.__c)
        self.__c1()


obj = A()
print(obj.a, obj._b)
obj._display()

