def fiboNum(x):
    if x == 1 and x == 2:
        return 1
    A= [1, 1]
    for i in range(2, x):
        A.append(A[i - 1] + A[i - 2])
    return (A[x - 1])

def Rezult():
    Rez = fiboNum(3) + fiboNum(8)
    return Rez

print(Rezult())