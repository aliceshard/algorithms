import sys

def swap(a, b, heap_type):
    global left_heap, right_heap
    heap = []
    if heap_type == 'left':
        heap = left_heap
    elif heap_type == 'right':
        heap = right_heap
    temp = heap[a]
    heap[a] = heap[b]
    heap[b] = temp

def upHeapify(idx, heap_type):
    global left_size, right_size, left_heap, right_heap
    heap = []
    size = 0
    if heap_type == 'left':
        heap = left_heap
        size = left_size
    elif heap_type == 'right':
        heap = right_heap
        size = right_size

    parent = idx // 2
    if heap_type == 'left': #Max Heap
        while parent >= 1:
            if heap[parent] > heap[idx]:
                return
            swap(parent, idx, heap_type)
            idx = parent
            parent = parent // 2
    elif heap_type == 'right': #Min Heap
        while parent >= 1:
            if heap[parent] < heap[idx]:
                return
            swap(parent, idx, heap_type)
            idx = parent
            parent = parent // 2

def downHeapify(idx, heap_type):
    global left_size, right_size, left_heap, right_heap
    heap = []
    size = 0
    if heap_type == 'left':
        heap = left_heap
        size = left_size
    elif heap_type == 'right':
        heap = right_heap
        size = right_size

    left = idx * 2
    if heap_type == 'left': #Max Heap
        while left <= size:
            right = left + 1
            if right <= size:
                if heap[left] < heap[right]:
                    left = right
            if heap[left] < heap[idx]:
                return
            swap(left, idx, heap_type)
            idx = left
            left = left * 2
    elif heap_type == 'right': #Min Heap
        while left <= size:
            right = left + 1
            if right <= size:
                if heap[left] > heap[right]:
                    left = right
            if heap[left] > heap[idx]:
                return
            swap(left, idx, heap_type)
            idx = left
            left = left * 2

def addNode(data, heap_type):
    global left_size, right_size, left_heap, right_heap
    heap = []
    size = 0
    if heap_type == 'left':
        heap = left_heap
        left_size += 1
        size = left_size
    elif heap_type == 'right':
        heap = right_heap
        right_size += 1
        size = right_size

    heap.append(data)
    upHeapify(size, heap_type)

def pop(heap_type):
    global left_size, right_size, left_heap, right_heap
    heap = []
    size = 0
    if heap_type == 'left':
        heap = left_heap
        left_size -= 1
        size = left_size
    elif heap_type == 'right':
        heap = right_heap
        right_size -= 1
        size = right_size

    root = heap[1]
    heap[1] = heap[size + 1]
    downHeapify(1, heap_type)
    heap.pop()
    return root

left_size = 0
right_size = 0
n = int(input())
left_heap = [0]
right_heap = [0]
for i in range(0, n):
    x = int(sys.stdin.readline().rstrip())
    # initial conditional process
    if len(left_heap) == 1 and len(right_heap) == 1:
        addNode(x, 'left')
        print(left_heap[1])
        continue
    elif len(left_heap) == 2 and len(right_heap) == 1:
        if x < left_heap[1]:
            temp = pop('left')
            addNode(temp, 'right')
            addNode(x, 'left')
        else:
            addNode(x, 'right')
        print(left_heap[1])
        continue

    # conditional processes
    if len(left_heap) == len(right_heap):
        if right_heap[1] < x:
            temp = pop('right')
            addNode(temp, 'left')
            addNode(x, 'right')
        elif x < left_heap[1]:
            addNode(x, 'left')
        else:
            addNode(x, 'left')
    elif len(left_heap) > len(right_heap):
        if x < left_heap[1]:
            temp = pop('left')
            addNode(temp, 'right')
            addNode(x, 'left')
        elif x > right_heap[1]:
            addNode(x, 'right')
        else:
            addNode(x, 'right')
    elif len(left_heap) < len(right_heap):
        if x > right_heap[1]:
            temp = pop('right')
            addNode(temp, 'left')
            addNode(x, 'right')
        elif x < left_heap[1]:
            addNode(x, 'left')
        else:
            addNode(x, 'left')
    print(left_heap[1])
