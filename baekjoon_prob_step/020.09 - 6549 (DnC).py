# parameters are index of input array
def solve(start, end):
    global input_arr
    mid = (start + end) // 2

    # max heights of the left partition and the right partition
    left_area = 0
    right_area = 0
    mid_area = 0

    if start == end:
        return input_arr[start]
    else:
        # calculating max area of left partition
        width = 0
        height_max = input_arr[start]
        for i in range(0, end+1):
            if input_arr[i] >= height_max:
                width += 1
            elif input_arr[i] < height_max:
                left_area = height_max * width
                break

        # calculating max area of right partition
        width = 0
        height_max = input_arr[end]
        for i in range(end, -1, -1):
            if input_arr[i] >= height_max:
                width += 1
            elif input_arr[i] < height_max:
                right_area = height_max * width
                break

        # calculating local mid here
        height_max = input_arr[mid]
        left_idx = right_idx = mid
        while True:
            if input_arr[left_idx] >= height_max:
                height_max = input_arr[left_idx]
                left_idx -= 1
            elif input_arr[left_idx] < height_max:
                break
        height_max = input_arr[mid]
        while True:
            if input_arr[right_idx] >= height_max:
                height_max = input_arr[right_idx]
                right_idx += 1
            elif input_arr[right_idx] < height_max:
                break
        if left_idx == right_idx:
            mid_area = input_arr[left_idx]
        else:
            width = right_idx - left_idx + 1
            mid_area = width * height_max
        return max([left_area, mid_area, right_area])

input_arr = []
while True:
    arr = list(map(int, input().split()))
    input_arr = arr[1:]
    if arr[0] == 0:
        break
