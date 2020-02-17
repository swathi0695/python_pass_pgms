print("Enter i :")
i = int(input())
if i < 0:
    print("Enter a num :")
    num = int(input())
    print("Inside if")
    if num > 0:
        print("num is positive")
    elif num == 0:
        print("Num is zero")
    else:
        print("num is negative")
elif i > 0:
    for a in range(0, i):
        print("i :", a)
    while i:
        print("i :", i)
        i -= 1
else:
    print("Inside Else")
    print(d.get(0))
    print(d.get(1))
    print(d.get(2))

