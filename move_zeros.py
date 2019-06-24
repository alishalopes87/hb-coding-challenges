# Keep track of an index and a stop index. Move 0 items from the index
# as you go along the array to the back. Decrement the stopping index
# as you remove items from the list to prevent infinite loop. 

def move_zeros(nums):
    stop_idx = len(nums) - 1
    idx = 0

    while idx < stop_idx:
        if nums[idx] == 0:
            nums.append(nums.pop(idx))
            stop_idx -= 1
        else:
            idx += 1

print(move_zeros([0,1,0,3,12]))