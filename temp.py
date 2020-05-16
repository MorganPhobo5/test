result = []

for A in range(100):
    T = True
    for x in range(100):
        for y in range(100):
            if (2 * x + 3 * y > 30) and (x + y <= A):
                pass
            else:
                T = False
    if T:
        result.append(A)
print(min(result))
