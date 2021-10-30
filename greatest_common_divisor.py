x = int(input("Please insert x "))
y = int(input("Please insert y "))


def gcd(x, y):
    if y == 0:
        return x
    else:
        print(x % y)
        return gcd(y, x % y)


print(gcd(x, y))
