import math

def matimatik(x,y):
    if x > y:
        return ((x ** 3) * math.sqrt((x ** 2) + (y ** 4)))
    else:
        return ((((x ** 2) - (2 * x) + math.sqrt(x))) / (math.pow(math.pow(x,2), 1/5)))

a = int(input('a = '))
b = int(input('b = '))

Rezult = matimatik(a, b) + matimatik(2, a) + 2

print('REPLY : {0}' .format(Rezult))



