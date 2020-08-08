# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # check for base case
    if start <= end:
        # set mid point index
        mid = (start + end) // 2
        
        # check if target == mid - if so return mid
        if arr[mid] == target:
            return mid
        
        # if target < mid 
        # target can only be in left tree
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1) # recursively call search on left tree, excluding old mid
        
        # target can only be in right tree
        else:
            return binary_search(arr, target, mid + 1, end) # recursively call search on right tree, excluding old mid
        
    # if we get here element is not in the array, retunr -1
    else: 
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    first_value = arr[0]
    last_value = arr[len(arr) - 1]
    start = 0
    end = len(arr) - 1
    # check if arr is sorted asc or desc
    if first_value < last_value:
        # asc sorted
        if start <= end:
            # set mid point index
            mid = (start + end) // 2
            
            # check if target == mid - if so return mid
            if arr[mid] == target:
                return mid
            
            # if target < mid 
            # target can only be in left tree
            elif target < arr[mid]:
                return agnostic_binary_search(arr[start:mid-1], target) # recursively call search on left tree, excluding old mid
            
        # target can only be in right tree
            else:
                return agnostic_binary_search(arr[mid+1:end], target) # recursively call search on right tree, excluding old mid
        
    # if we get here element is not in the array, retunr -1        
            return -1
    else:
        # desc sorted - reverse/flip operators above
        if start >= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return target
            elif target < arr[mid]:
                return agnostic_binary_search(arr[mid + 1:end], target)   
            else:
                return agnostic_binary_search(arr[start:mid -1], target)
        return -1