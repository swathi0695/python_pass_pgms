class MyClass:
    a = 10

    def func(self):
        print('Hello')


print(MyClass)
del MyClass

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del my_list[1:4]
print(my_list)