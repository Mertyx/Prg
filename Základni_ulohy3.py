p = 0

while True:
    result = 2 ** p
    if result > 1024:
        break
    print(result)
    p += 1