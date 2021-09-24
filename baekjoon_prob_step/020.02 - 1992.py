from sys import stdin

n = int(input())
arr = []
strg = '('
for i in range(0, n):
    arr.append(stdin.readline().rstrip())

def recur(x, y, leng):
    acc = 0
    bstr = '('

    # if length of cell is 1
    if leng == 1:
        if arr[y][x] == '0':
            return '(0)'
        else:
            return '(1)'

    # traverse all cells in arr
    for i in range(y, y + leng):
        for j in range(x, x + leng):
            acc += int(arr[i][j])

    # decision logic
    if acc == (leng) ** 2:
        return '(1)'
    elif acc == 0:
        return '(0)'
    else:
        a = recur(x, y, leng // 2)
        b = recur(x + leng // 2, y, leng // 2)
        c = recur(x, y + leng // 2, leng // 2)
        d = recur(x + leng // 2, y + leng // 2, leng // 2)
        ar = [str(a),str(b),str(c),str(d)]
        for i in range(0,4):
            if len(ar[i]) == 3:
                ar[i] = ar[i][1]
        bstr += ar[0] + ar[1] + ar[2] + ar[3] + ')'
        return bstr


res = recur(0, 0, n)
if len(res) == 3:
    res = res[1]
print(res)
