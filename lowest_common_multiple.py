x = int(input("Please give x: "))
y = int(input("Please give y: "))


def lcm(x, y):  # 40 and 12  x = 40 y = 12
    if x > y:  # 40>12
        greater = x  # greater is 40
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):  # first part = true but second part is false
            lcm = greater
            break
        greater += 1  # 40++ >> 41 on first iteration line 12 is false until both conditions true
        # when greater goes 120 both conditions are true so lcm of 40 and 12 is 120

    return lcm


print("Least common multiple of " + str(x) + " and " + str(y) + " is " + str(lcm(x, y)))
