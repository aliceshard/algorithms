import sys
white, blue = [0,0]

def recur(row, col, leng):
    global white
    global blue

    if leng == 1:
        if arr[row][col] == 1:
            return 1
        else:
            return 0
    a = recur(row, col, leng // 2)
    b = recur(row + leng // 2, col, leng // 2)
    c = recur(row + leng // 2, col + leng // 2, leng // 2)
    d = recur(row, col + leng // 2, leng // 2)
    if a + b + c + d == 4:
        return 1
    elif a + b + c + d == 0:
        return 0
    else:
        for i in [a,b,c,d]:
            if i != 100:
                if i == 1:
                    blue += 1
                elif i == 0:
                    white += 1
        return 100

n=int(input())
arr = []
for i in range(0,n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(temp)

# main starts from here
res = recur(0,0,n)
if res==1:
    white = 0
    blue = 1
elif res ==0:
    white = 1
    blue = 0
print(white)
print(blue)

