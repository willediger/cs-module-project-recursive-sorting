# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    if elements > 1:
        if len(arrA) == 0:
            return arrB
        elif len(arrB) == 0:
            return arrA
        elif arrA[0] <= arrB[0]:
            return [arrA[0]] + merge(arrA[1:], arrB)
        elif arrA[0] > arrB[0]:
            return [arrB[0]] + merge(arrA, arrB[1:])
    else:
        return arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    return merge(left, right)

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    l_start = start
    l_end = mid
    r_start = mid+1
    r_end = end

    # if last element in our "first array" is less than
    # the first element in our "second array", we're done
    if arr[l_end] <= arr[r_start]:
    return arr
    while l_start <= l_end and r_start <= r_end:

        # if first element in our "first array" is less than 
        # the first element in our "second array", that element is
        # in place, and so we exclude that element from our "first array"
        if arr[l_start] <= arr[r_start]:
            l_start += 1

        # if first element in our "second array" is less than 
        # the first element in our "first array", that element is
        # we need to move the first element from the "second array"
        # to the front, and then shift everything else one element to
        # the right.
        else:
            temp = arr[r_start]

            for i in range(r_start, l_start, -1):
                arr[i] = arr[i - 1]

            arr[l_start] = temp
            l_start += 1
            l_end += 1
            r_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
