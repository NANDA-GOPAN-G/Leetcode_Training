def sortedSquares(nums):

    res = [None]*len(nums)
    p = len(nums) - 1

    a = 0
    b = len(nums) - 1

    while a <= b:
        
        if nums[a]**2 < nums[b]**2:
            res[p] = nums[b]**2
            b = b - 1

        else:
            res[p] = nums[a]**2
            a = a + 1

        p -= 1

    return res
        

nums = [-4,-1,0,3,10] #input array musted be a sorted array
print("Sorted squared array: ",sortedSquares(nums))