from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class Dog(animal):
    def move(self):
        print("Dog  can walk and run ")

class Lion(animal):
    def move(self):
        print("Lion  can walk and run ")

class cat(animal):
    def move(self):
        print("Cat  can walk run,jump ")

class Human(animal):
    def move(self):
        print("It can walk and run on two leg ")
K=Dog()
K.move()
L=Lion()
L.move()
M=cat()
M.move()
N=Human()
N.move()