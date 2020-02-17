print("---------for---------")
a = 1
for i in range(a, 15):
    print("a =", i)
    print("2nd line in for")

# Another example having for-else condition
print("---------for-else---------")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            print("2nd line in if")
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
