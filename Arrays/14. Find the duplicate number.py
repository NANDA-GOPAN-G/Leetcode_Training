def duplicate(nums):

    for val in nums:
        abs_val = abs(val)

        if nums[abs_val - 1] < 0:
            return abs_val
        else:
            nums[abs_val - 1] *= -1

nums = [3,1,1,4,2]
print(duplicate(nums))