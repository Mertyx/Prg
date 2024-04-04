def moje_funkce(x,y):
    a = ""
    for i in range(x,y + 1):
        if i == y:
            a += str(i)
        else:
            a += str(i) + ", "
    print(a)
moje_funkce(1,10)