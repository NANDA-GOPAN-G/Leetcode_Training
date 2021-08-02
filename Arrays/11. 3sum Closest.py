def threeSum_closest(nums,target):
    nums.sort()
    res = sum(nums[:3])
        
    for a in range(len(nums) - 2):
        l = a + 1
        r = len(nums) - 1
            
        while l < r:
            three_sum = nums[a] + nums[l] + nums[r]
                
            if abs(three_sum - target) < abs(res - target):
                res = three_sum
                    
            if three_sum < target:
                l += 1
            else:
                r -= 1
                    
    return res

nums = [-1,2,1,-4]
target = 1
print(threeSum_closest(nums,target))