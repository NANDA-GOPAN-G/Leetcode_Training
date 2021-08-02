def two_sum(arr,target):

    d = {}

    for i in range(len(arr)):

        if (target-arr[i])not in d:
            d[arr[i]] = i

        else:
            return [d[target-arr[i]],i]


nums = [2,7,11,15]
Target = 9
print(two_sum(nums,Target))