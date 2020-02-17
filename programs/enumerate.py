# import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

print("All the enum values are : ")
for animal in Animal:
    print(animal)

print(Animal.dog)
print(repr(Animal.dog))
print(Animal.dog.name)
print(Animal(2))
print(Animal['lion'])

mem = Animal.dog
print(mem.value)
print(mem.name)

if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")

# Another example
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
