def SpiralMatrix(nums):
    arr = []
    rbeg = 0
    rend = len(nums) - 1
    cbeg = 0
    cend = len(nums[0])-1
    while (rbeg <= rend) and (cbeg <= cend):
        for i in range(cbeg, cend + 1):
            arr.append(nums[rbeg][i])
        
        for i in range(rbeg + 1, rend + 1):
            arr.append(nums[i][cend])
        
        for i in range(cend - 1, cbeg - 1, -1):
            if rbeg == rend:
                break
            arr.append(nums[rend][i])
        
        for i in range(rend - 1, rbeg, -1):
            if cbeg == cend:
                break
            arr.append(nums[i][cbeg])
        
        rbeg += 1
        rend -= 1
        cbeg += 1
        cend -= 1
    
    return arr

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(SpiralMatrix(matrix))
