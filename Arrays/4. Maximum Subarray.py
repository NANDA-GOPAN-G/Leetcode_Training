def maximumSubarray(nums):
    res = nums[0]
    dup_sum = 0
    for val in nums:
        if dup_sum < 0:
            dup_sum = 0
        dup_sum += val
        res = max(dup_sum,res)
    return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))