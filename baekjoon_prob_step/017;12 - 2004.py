n, k = list(map(int, input().split()))
def fact0(n):
    a, b = 0, 0
    t = 2
    while t <= n:
        i = 1
        while t * i <= n:
            a += 1
            i += 1
        t *= 2

    t = 5
    while t <= n:
        i = 1
        while t * i <= n:
            b += 1
            i += 1
        t *= 5
    return [a,b]

a = fact0(n)
b = fact0(n-k)
c = fact0(k)
bc = [b[i]+c[i] for i in range(0,2)]
result = [a[i]-bc[i] for i in range(0,2)]

print(min(result))