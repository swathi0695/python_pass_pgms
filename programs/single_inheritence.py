class Animal:
    def speak(self):
        print("Animal Speaking")


# child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")


# child class Cat inherits the base class Animal
class Cat(Animal):
    def meows(self):
        print("cat meows")


d = Dog()
c = Cat()
d.bark()
d.speak()
c.speak()
c.meows()
