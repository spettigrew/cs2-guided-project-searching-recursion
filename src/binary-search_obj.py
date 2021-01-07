# Runtime - log(n)
# for each exponential increase, we're linearily increasing our number of steps
# 10 = 3 steph, 20 = 4 steps, 40 = 5 steps, etc. Input gets halved every time

our_array = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]

def binary_search(arr, target):
    start_index = 0
    end_index = len(arr) - 1

    # keep modifying our search space, until its either invalid, or we found our target
    while start_index <= end_index:
        # keep guessing, checking and shrinking our search space
        mid_index = (end_index + start_index) // 2
        # check if the guess is our value, or if it's greater or less than our value
        if arr[mid_index] == target:
            return mid_index
        
        # shrink our search space accordingly
        # the guess is smaller than your target
        if arr[mid_index] < target:
            # move the start_index to the middle
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1

        return -1


print(binary_search(our_array, 2)) # 9

our_string_array = ['a', 'b', 'c', 'd','e']

print(binary_search(our_string_array, 'e'))

