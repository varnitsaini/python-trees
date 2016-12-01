"""
Illustrating the Max Heap Operations
Same can be achieved for min heaps just minf changes are required for the
Following are the operations which will be covered in this illustration

Find Max
    Time Complexity : O(1)

Delete Max
    Time Complexity : O(logn)

Insert
    Time Complexity : O(logn)

Increase
    Time Complexity : O(logn)

Where n is number of nodes
"""


def maxHeapify(arr, i):

    left = 2 * i + 1
    right = 2 * i + 2
    arrLen = len(arr) - 1

    if left <= arrLen and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right <= arrLen and arr[right] > arr[largest]:
        largest = right

    if i != largest:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, largest)


def buildMaxHeap(arr):

    for i in range(len(arr)/2, -1, -1):
        maxHeapify(arr, i)

def deleteMax(arr):

    maxElem = arr[0]
    arr[0] = arr[len(arr) - 1]
    arr.pop(len(arr) - 1)
    maxHeapify(arr, 0)

    return maxElem

def insertElem(arr, insertedValue):
    arr.append(insertedValue)

    i = len(arr) - 1
    while i >=0 and arr[i] > arr[i/2]:
        arr[i], arr[i/2] = arr[i/2], arr[i]
        i /= 2

def increaseValue(arr, increasedValue, index):
    arr[index] = increasedValue

    i = index
    while i >= 0 and arr[i] > arr[i/2]:
        arr[i], arr[i/2] = arr[i/2], arr[i]
        i /= 2


arr = [5, 1, 9, 2, 6, 8, 0, 7]

buildMaxHeap(arr)

"""Find max will be the first element of max heap"""
print "Max element is : %d" % arr[0]

"""Delete max"""
print "Deleted Maximum element is %d " % deleteMax(arr)

"""Inserting an element to the heap"""
insertElem(arr, 300)

"""Increase value of element at specific index"""
increaseValue(arr, 200, 3)

print arr