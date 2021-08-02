def productExceptSelf(nums):

    product_array = [1] * len(nums)
    left = right = 1

    for i in range(len(nums)):
        product_array[i] *= left
        left *= nums[i]
    
    for i in range(len(nums)-1,-1,-1):
        product_array[i] *= right
        right *= nums[i]
    
    return product_array


nums = [1,2,3,4]
#nums1 = [-1,1,0,-3,3]
print(productExceptSelf(nums))
#print(productExceptSelf(nums1))