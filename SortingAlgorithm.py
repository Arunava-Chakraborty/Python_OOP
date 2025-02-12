# Selection Sort algorithm in Python
#selection Sort
'''''
def selectionSort(array, size):
    for s in range(size):
        min_idx = s

        for i in range(s + 1, size):

            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])


# Driver code
data = [7, 2, 1, 6]
size = len(data)
selectionSort(data, size)

print('Sorted Array in Ascending Order is :')
print(data)
'''

# Creating a function for insertion sort algorithm
def insertion_sort(list1):
    # Outer loop to traverse on len(list1)
    for i in range(1, len(list1)):

        a = list1[i]

        # Move elements of list1[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1

        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = a

    return list1


# Driver code
list1 = [7, 2, 1, 6]
print("The unsorted list is Insertion Sort:", list1)
print("The sorted new list Insertion Sort is :", insertion_sort(list1))
