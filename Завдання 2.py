n = int(input('n = '))

import math
def matimatik(x, y):
    a = []
    for i in range(n):
        a.append(x[i] * y[i])
    Rez = 0
    for i in range(n):
        Rez += a[i]
    return (Rez)


A = [int(input('A[{0}] = '.format(i)))for i in range(n)]
print()

B = [int(input('B[{0}] = '.format(i)))for i in range(n)]
print()

C = [int(input('C[{0}] = '.format(i)))for i in range(n)]
print()

Rez = 2 * matimatik(A,B) - 3 * matimatik(A,C)
print('REZULT = ', Rez)

