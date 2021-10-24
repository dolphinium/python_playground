print("Sample quadratic equation: ax^2 + bx + c")

# take inputs from user
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))

# assign formula of discriminant
d = b * b - (4 * a * c)

# assign equation for printing equation easily.
equation = str(a) + "x^2+ " + str(b) + "x+ " + str(c)

if a != 0:  # if coefficient of x^2 is 0 the equation will not satisfy the definition!
    if d > 0:  # if d>0 there are 2 real roots which is x1 and x2
        x1 = (-b + d ** (1 / 2)) / (2 * a)  # x1 will be calculated with formula -b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)  # x2 will be calculated with formula -b - d ** (1 / 2)) / (2 * a)
        print("The equation " + equation + " have two real roots:")  # print equation
        print("x1=", x1, " and x2=", x2)
        print("Discriminant is: " + str(d))  # print discriminant just for curiosity
    elif d == 0:  # if d=0 there is only 1 root
        x = -b / (2 * a)  # x will be calculated with formula x = -b / (2 * a)
        print("The equation " + equation + " have two same roots:")
        print("x=", x)
        print("Discriminant is: " + str(d))
    elif d < 0:  # if d<0 there are 2 imaginary roots
        x1 = (-b + d ** (1 / 2)) / (2 * a)  # x1 will be calculated with formula -b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)  # x2 will be calculated with formula -b - d ** (1 / 2)) / (2 * a)
        print("The equation " + equation + " have two complex roots")
        # I use round function to use just 2 digit of exact numbers and when I tried to do that I had issues with
        # numbers so I divide the real part and imaginary part of numbers to fix it!
        print("x1=", round(x1.real, 2) + round(x1.imag, 2) * 1j, " and x2=", round(x2.real, 2) + round(x2.imag, 2) * 1j)
        print("Discriminant is: " + str(d))

else:
    print(equation + " is not quadratic equation!")
