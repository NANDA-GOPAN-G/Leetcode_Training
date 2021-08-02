def twosum(nums,t):

    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[left] + nums[right] == t:
            return [left,right]

        elif nums[left] + nums[right] > t:
            right -= 1

        else:
            left += 1


nums = [2,7,11,15] #The input array must be sorted in ascending order
#If in descending, based on that, the implementation of the same concept changes.
target = 9
print(twosum(nums,target))