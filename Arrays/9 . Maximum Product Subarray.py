
def maxProduct(nums):
        
    res = max(nums)
    curMax = curMin = 1
        
    for n in nums:
            
        if n == 0:
            curMax = curMin = 1
            continue
            
        temp = curMax * n
        curMax = max(temp, curMin * n, n)
        curMin = min(temp, curMin * n, n)
        res = max(res, curMax)
            
    return res

nums = [2,3,-2,4]    #output will be 6
print(maxProduct(nums))

