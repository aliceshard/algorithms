def vec_mul(vec1, vec2, n):
    # print('calculating...')
    result = []
    md = 1000000007
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            acc = 0
            for k in range(0, n):
                acc += (vec1[i][k] * vec2[k][j]) % md
            acc %= md
            temp.append(acc)
        result.append(temp)
    return result

def factor_bin(b):
    temp = []
    while (b != 0):
        if b % 2 == 0:
            temp.append(0)
            b //= 2
        elif b % 2 == 1:
            temp.append(1)
            b //= 2
    # print('factored bin: {}'.format(temp))
    return temp

def init_idv(n):
    idv = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        idv.append(temp)
    return idv


def vec_proc(vec, n):
    bin_str = factor_bin(n)
    acc_vec = vec
    res_vec = init_idv(2)
    for i in range(0, len(bin_str)):
        if bin_str[i] == 1:
            # print('bit is one...')
            res_vec = vec_mul(res_vec, acc_vec, 2)
        acc_vec = vec_mul(acc_vec, acc_vec, 2)
    # print(acc_vec)
    return res_vec

# print('getting vector input...')
n = int(input())
vec = [[0,1],[1,1]]
mod = 1000000007
final_result = 0

if n == 1 or n == 2:
    final_result = 1
elif n == 3:
    final_result = 2
else:
    result = vec_proc(vec, n-3)
    fibo_num1 = (result[0][0] + result[0][1])%mod
    fibo_num2 = (result[1][0] + result[1][1])%mod
    final_result = (fibo_num1 + fibo_num2)%mod

# print
print(final_result)