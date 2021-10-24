print("Sample quadratic equation: ax^2+bx+c")

a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))

d = b * b - (4 * a * c)

equation = str(a) + "x^2+ " + str(b) + "x+ " + str(c)

if a != 0:
    if d > 0:
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        print("The equation " + equation + " have two real roots:")
        print("x1=", x1, " and x2=", x2)
        print("Discriminant is: "+str(d))
    elif d == 0:
        x = -b / (2 * a)
        print("The equation " + equation + " have two same roots:")
        print("x=", x)
        print("Discriminant is: " + str(d))
    elif d < 0:
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        print("The equation " + equation + " have two complex roots")
        print("x1=", round(x1.real, 2) + round(x1.imag, 2) * 1j, " and x2=", round(x2.real, 2) + round(x2.imag, 2) * 1j)
        print("Discriminant is: " + str(d))

else:
    print(equation + " is not quadratic equation!")
