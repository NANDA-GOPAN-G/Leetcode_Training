def monotonic_arr(nums):
    increase = decrease = 0

    for i in range(1,len(nums)):
        if nums[i] > nums[i - 1]:
            increase += 1
        elif nums[i] < nums[i - 1]:
            decrease += 1
    
    return increase == 0 or decrease == 0

nums = [1,2,2,3]
print(monotonic_arr(nums))