def threeSum(nums):
    nums.sort()
    arr = []

    for a in range(len(nums) - 2):
        if a>0 and nums[a] == nums[a - 1]:
            continue
            
        l = a + 1
        r = len(nums) - 1

        while l < r:

            if nums[l] + nums[r] + nums[a] == 0:
                arr.append([nums[a],nums[l],nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r += 1
                l += 1
                r -= 1
            
            elif nums[l] + nums[r] + nums[a] < 0:
                l += 1
            
            else:
                r -= 1
        
    return arr
                        

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))