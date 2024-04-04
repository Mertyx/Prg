import math

for i in range(0,8):
    a = ""
    for k in range(0,8):
        x = math.fmod(k + i,2)
        if x == 0:
            a += str(0)
        if x == 1:
            a += str(1)
    print(a)
 