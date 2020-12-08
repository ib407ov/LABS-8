def fiboNum(x):
    if x == 1 and x == 2:
        return 1
    A= [1, 1]
    for i in range(2, x):
        #print(i)
        A.append(A[i - 1] + A[i - 2])
    print(A)
    return (A[x - 1])

n = int(input('find the fibonacci number: '))
print(fiboNum(n))