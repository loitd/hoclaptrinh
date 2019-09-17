from abc import ABC, abstractmethod
class Person():
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def sayHello(self):
        pass
    
    def shakehands(self):
        print("I am shaking hands")
    
class Asian(Person):
    def __init__(self):
        super().__init__()
    
    def sayHello(self):
        print("Hello, I am Asian")

class African(Person):
    def __init__(self):
        super().__init__()
    
    def sayHello(self):
        print("Hello, I am African")

class AsiAfrican(Asian, African):
    def __init__(self):
        super().__init__()

class AfriAsian(African, Asian):
    def __init__(self):
        super().__init__()
    
if __name__ == "__main__":
    a1 = AsiAfrican()
    a2 = AfriAsian()
    a1.sayHello()
    a2.sayHello()
    a1.shakehands()
    a2.shakehands()