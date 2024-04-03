cols, rows = 2, 4
n = [[0] * cols] * rows
n[3][0] = 2
print(n)
m = [[0 for i in range(cols)] for j in range(rows)]
m[3][0] = 2
print(m)
o = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    o.append(col)
o[3][0] = 2
print(o)