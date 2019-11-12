class Animal(object):
     def out(self):
         print("Animal run...")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def out(self):
        print("Dog run...")

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def out(self):
        print("Cat run...")

animal = Animal()
def run_twice(animal):
    animal.out()

dog = Dog("name")
run_twice(Dog("name"))