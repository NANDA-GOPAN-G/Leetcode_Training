def moveZeroes(nums):
    p = 0
    for i in range(len(nums)):
        if nums[i] != 0:   #moves zeroes to right. if used nums[i] == 0, zero moves to left
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))