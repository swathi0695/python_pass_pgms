# Implementing Polymorphism with class methods
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi the primary language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


# Implementing Polymorphism with a Function
def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()
print("-----Implementing Polymorphism with class methods----")
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
print("-----Implementing Polymorphism with a Function----")
func(obj_ind)
func(obj_usa)
