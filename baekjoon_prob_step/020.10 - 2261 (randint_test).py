import random as r

def dist_cal(point1, point2):
    x_dist = (point1[0] - point2[0]) ** 2
    y_dist = (point1[1] - point2[1]) ** 2
    return x_dist + y_dist

def solve(start, end):
    global inf, arr
    # print('start:{}, end:{}'.format(start, end))
    if start == end:
        # print('returned: {}'.format(inf))
        return inf
    mid_idx = (end + start) // 2
    min_dist = min(solve(start, mid_idx), solve(mid_idx + 1, end))

    # calculate candidates respect to x_pos
    arr2 = []
    left_idx = right_idx = mid_idx
    lborder_flag = rborder_flag = False

    arr2.append(arr[mid_idx])
    while right_idx != end:
        right_idx += 1
        if (arr[mid_idx][0] - arr[right_idx][0]) ** 2 < min_dist:
            arr2.append(arr[right_idx])
        else:
            break
    while left_idx != start:
        left_idx -= 1
        if (arr[mid_idx][0] - arr[left_idx][0]) ** 2 < min_dist:
            arr2.append(arr[left_idx])
        else:
            break

    # calculate candidates respect to y_pos
    arr2 = sorted(arr2, key=lambda x: x[1])

    for i in range(0, len(arr2)):
        for j in range(i+1, len(arr2)):
            if arr2[i][0] == arr2[j][0] and arr2[i][1] == arr2[j][1]:
                return 0

            if (arr2[i][1] - arr2[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, dist_cal(arr2[i], arr2[j]))
            else:
                break

    # print('arr2: {}'.format(arr2))
    # print('returned: {}'.format(min_dist))
    return min_dist


def exhaust_solve():
    global arr, inf
    min_dist = inf
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            min_dist = min(min_dist, dist_cal(arr[i], arr[j]))
    return min_dist

def input_routine():
    global arr, inf
    #n = int(input())
    # calculate respect to x_pos
    '''
    for i in range(0, n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    '''
    arr = sorted(arr, key=lambda x: [x[0], x[1]])
    #arr = [[-8, 3], [-7, 9], [-6, -4], [-5, -7], [2, -5], [5, -10]]
    print(arr)
    ans = solve(0, len(arr) - 1)
    # change x_pos and y_pos
    for i in range(0, n):
        temp = arr[i][0]
        arr[i][0] = arr[i][1]
        arr[i][1] = temp
    arr = sorted(arr, key=lambda x: [x[0], x[1]])
    #print(arr)
    # calculate respect to y_pos
    ans = min(ans, solve(0, len(arr) - 1))

    return ans

inf = 4000000001
arr = []
ans = exh_ans = 0
n = 5
itr = 0

while ans == exh_ans:
    arr = []
    for i in range(0, n):
        a = r.randint(-10, 10)
        b = r.randint(-10, 10)
        arr.append([a,b])
    #print(arr)
    ans = input_routine()
    exh_ans = exhaust_solve()
    #exh_ans = ans
    itr += 1

#############################
# Exhasutive implementation #
#############################

print('calculated: {}'.format(ans))
print('true answer: {}'.format(exh_ans))
print('iteration: {}'.format(itr))