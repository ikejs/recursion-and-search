#!python

def linear_search(items, target):
    # return linear_search_iterative(items, target)
    return linear_search_recursive(items, target)
    


def linear_search_iterative(array, target):
    # loop over all array values until item is found
    index = 0
    for item in array:
        if item == target:
            return index  # found
        else:
            index+=1
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index == len(array):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array) - 1)


def binary_search_iterative(array, item):
    left = 0
    right = len(array)-1
    while(left<=right):
        mid = (left + right)//2
        if array[mid] == item:
            return mid
        else:
            if item < array[mid]:
                right = mid - 1
            else:
                left = mid + 1	
    return None



def binary_search_recursive(array, item, left=None, right=None):
    if left > right:
        return None
    mid = (left + right) // 2
    if array[mid] > item:
        return binary_search_recursive(array, item, left, mid - 1)
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, right)
    elif array[mid] == item:
        return mid
