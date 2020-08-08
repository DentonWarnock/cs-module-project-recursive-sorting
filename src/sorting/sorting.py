# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # iterate both left and right pre sorted arrays and compare items to create new single sorted array (result)
    result = []
    left_index = 0
    right_index = 0
    # start loop, continue until there are no more items in left or right
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])    
            right_index += 1
    # add any remaining items from left then right arrays to results
    result += left[left_index:]
    result += right[right_index:]

    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # continually split array into halves until each array contains 1 item, then call merge
    # base case - array of 1 item = return array
    if len(arr) < 2:
        return arr
    # find midpoint with int divide
    mid = len(arr) // 2
    # continually split left and right until len == 1
    left = merge_sort(arr[:mid]) # left = first:mid
    right = merge_sort(arr[mid:]) # right = mid:last
        
    # return merged list using helper function
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
