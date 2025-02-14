arr = [4,3,7,1,5,2]
start = 0
end = len(arr)-1

def Partition(arr , start, end):
    i = start -1
    pivot = arr[end]

    for j in range(start , end):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, end)
    return i + 1


def Quicksort(arr , start , end):
    if start < end:
        # pi is the partition return index of pivot
        pi = Partition(arr, start , end)

        # Recursion calls for smaller elements
        # and greater or equals elements
        Quicksort(arr, start, pi - 1)
        Quicksort(arr, pi + 1, end)
    return arr
def swap(arr , i, j):
    arr[i], arr[j] = arr[j], arr[i]


print(Quicksort(arr,start,end))