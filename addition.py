def addition(x):
    if x <= 1:
        return 1
    return x + sum(x - 1)


a = int(input("Enter an Integer: "))

print(addition(a))
