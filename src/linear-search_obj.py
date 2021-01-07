# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        cur_num = arr[i]
        if cur_num == target:
            return i

    return -1

# recursion - a big problem broken down to similar sub-problems that can be solved
def linear_search2(arr, item, cur_idx):
    if cur_idx >= len(arr):     #base case - do not recurse
        return -1
    if arr(cur_idx) == item:    #base case - do not keep going 
        return cur_idx
        # wherever you are, find the next location cur_idx + 1
    return linear_search2(arr, item, cur_idx + 1) # still have items to look for - recursive case
    # change of state - move the index along until you exit the loop - the recursion

our_array = [1, 2, 3, 5, 7, 8, 9, 11, 13, 15, 16]

print(linear_search(our_array, 14))

result = linear_search(our_array, 13)


# When running recursion - it goes up the stack, finds the targeted index, then it goes back all the way down the stack to return the target.