import sys

def upHeapify(idx):
    global heap
    parent = idx // 2
    while parent >= 1:
        if heap[parent] > heap[idx]:
            return
        # Swap
        temp = heap[parent]
        heap[parent] = heap[idx]
        heap[idx] = temp

        idx = parent
        parent = idx // 2

def downHeapify(idx):
    global size, heap

    # idx: downHeapify의 시작 지점
    # left: 삽입이 될 위치
    left_idx = idx * 2
    while(left_idx <= size):
        right_idx = left_idx+1
        # 삽입이 될 위치를 오른쪽으로 바꿀 수 있는 경우
        if right_idx <= size:
            if heap[left_idx] < heap[right_idx]:
                left_idx = right_idx
        # 최대힙의 조건이 만족되고 있다면 리턴
        if heap[left_idx] < heap[idx]:
            return
        # Swap
        temp = heap[idx]
        heap[idx] = heap[left_idx]
        heap[left_idx] = temp
        # root와 삽입 위치를 갱신
        idx = left_idx
        left_idx = idx * 2

def addNode(data):
    global size, heap
    heap.append(data)
    size += 1
    upHeapify(size)

def pop():
    global size, heap
    root = heap[1]
    heap[1] = heap[size]
    size -= 1
    downHeapify(1)
    heap.pop()
    return root

size = 0
n = int(input())
heap = [0]
for i in range(0, n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if size == 0:
            print('0')
        else:
            print(pop())
    else:
        addNode(x)
