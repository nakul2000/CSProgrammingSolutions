
import math

f = open("input.txt")
print(f.readline())
g = open("outputme.txt", 'w')



for read in f:
    readarr = read.split(",")
    a = int(readarr[0])
    b = int(readarr[1])
    c = int(readarr[2])
    discriminant = (b*b)-(4*a*c)
    solution = ""
    if discriminant > 0:
        disc = math.sqrt(discriminant)
        b2 = 0 - b
        quada = (b2 + disc) / (2*a)
        quadb = (b2 - disc) / (2*a)
        quadb = round(quadb,2)
        quada = round(quada,2)
        solution = "The quadratic equation with coefficients A = " + str(a) + ", B = " + str(b) + ", C = " + str(c) + " has roots x = " + str(quada) + " and x = " + str(quadb) + " ."
        g.writelines(solution + "\n")
        print(solution)

    else:
        solution = "The quadratic equation with coefficients A = " + str(a) + ", B = " + str(b) + ", C = "+ str(c) + " has no real roots."
        g.writelines(solution + "\n")
        print(solution)


