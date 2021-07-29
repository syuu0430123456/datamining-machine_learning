#関数定義と呼び出し

def nsum(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

#関数呼び出し
m = 10
ms = nsum(m)
print(ms)
m = 20
ms = nsum(m)
print(ms)