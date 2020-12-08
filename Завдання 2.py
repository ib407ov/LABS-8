import math
def matimatik(x, y):
    return (math.pow(x, 2) + math.pow(y, 2))

a = float(input('a(for the first and second vektors) = '))
b = float(input('b(for the first vektor) = '))
c = float(input('c(for the second vektor) = '))

Rezult = 2 * matimatik(a, b) - 3 * matimatik(a, c)
print('REPLY : {0}' .format(Rezult))