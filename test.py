a = 10
b = [1, 2, 3]

def tmp():
    global a
    a += 1
    b[0] += 1

tmp()
print(a)
print(b)