class A:
    # syntax of destructor
    def __del__(self):
        return 

class Employee:
    def __init__(self):
        print("init employee")
    
    def __del__(self):
        print('Employee deleted')


obj = Employee()

