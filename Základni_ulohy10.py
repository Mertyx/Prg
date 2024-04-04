def asd(n):
    if n == 1:
        print(1)
        return
    for i in range(2,n):
        b = False
        for j in range(2,i):
            if (i % j) == 0:
                b = True
                break
        if b == False:
            print(i)
asd(15)      