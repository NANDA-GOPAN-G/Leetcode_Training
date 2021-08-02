def containsDuplicate(nums):
    hashnum = {}
        
    for val in nums:
            
        if val not in hashnum:
            hashnum[val] = 1
            
        else:
            return True
            
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))