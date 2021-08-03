def merge_intervals(intervals):
    intervals = sorted(intervals,key = lambda x:x[0])
    ar = []

    for i in range(len(intervals)):
        
        if ar and intervals[i][0] <= ar[-1][1]:
            ar[-1][1] = max(intervals[i][1],ar[-1][1])
        else:
            ar.append(intervals[i])
    
    return ar
            

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))