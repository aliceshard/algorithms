from sys import stdin, stdout

n = int(input())
arr = [0] + list(map(int, input().split()))
result = []
st = []

#init
st.append(arr[-1])
result.append(-1)
globalmax = arr[-1]

for i in range(n-1, 0, -1):
    # is bigger than globalmax? need to update globalmax
    if globalmax <= arr[i]:
        result.append(-1)
        st = []
        st.append(arr[i])
        globalmax = arr[i]
        continue
    # if increasing...
    if st[-1] < arr[i]:
        for j in range(len(st)-1,-1,-1):
            if st[j] > arr[i]:
                result.append(st[j])
                break
        st.pop()
        st.append(arr[i])
    # if decreasing...
    elif st[-1] >= arr[i]:
        for j in range(len(st)-1,-1,-1):
            if st[j] > arr[i]:
                result.append(st[j])
                break
        st.append(arr[i])

# print result
for i in range(n-1,-1,-1):
    print(result[i], end=' ')