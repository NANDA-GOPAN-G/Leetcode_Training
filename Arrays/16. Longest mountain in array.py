def longestMountain(nums):
    size = 0

    for peak in range(1,len(nums)-1):
        if nums[peak - 1] < nums[peak] > nums[peak + 1]:
            l = r = peak
        
            while l > 0 and nums[l] > nums[l - 1]:
                l -= 1
        
            while r + 1 < len(nums) and nums[r] > nums[r + 1]:
                r += 1
    
            size = max(size, (r - l + 1))

    return size


nums = [2,1,4,7,3,2,5]
print(longestMountain(nums))