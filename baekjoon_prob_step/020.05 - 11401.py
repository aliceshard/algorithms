def bin_prov(p):
    temp = []
    while p != 0:
        if p % 2 == 0:
            p //= 2
            temp.append(0)
        elif p % 2 == 1:
            p //= 2
            temp.append(1)
    temp.reverse()
    return temp

def power_p(b, p):
    res = 1
    temp = 1
    p_real = p + 2
    bin_str = bin_prov(p)
    bin_str.reverse()
    for i in range(0, len(bin_str)):
        if i == 0:
            temp = b
        else:
            temp = (temp ** 2) % p_real
        if bin_str[i] == 1:
            res *= temp
            res %= p_real
    bin_str.reverse()
    return res

def facto(n, p):
    res = 1
    for i in range(n,0,-1):
        res *= i
        res %= p
    return res

n,k = list(map(int,input().split()))
p = 1000000007

a = facto(n, p)
b = (facto(k, p) * facto(n-k, p)) % p
b_res = power_p(b, p-2) % p
result = (a * b_res) % p
print(result)

'''
p = int(input('p: '))
bin_str = bin_prov(p)
b = int(input('b: '))
print(power_p(b,p,bin_str))
fact = int(input('facto: '))
print(facto(fact,p))'''