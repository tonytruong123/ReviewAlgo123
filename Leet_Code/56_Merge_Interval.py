def merge(intervals):
    # sort the list first
    intervals.sort(key=lambda x: x[0])
    # have something in it to compare
    ans_list =  [intervals[0]]
    for start,end in intervals[1:]:
        # set the newest end point to compare
        lastEnd = ans_list[-1][1]
        # if it is in range
        if start <= lastEnd:
            # for example we may have [1,5],[2,4] or [1,5],[2,6]
            # => need to choose the max end point
            ans_list[-1][1] = max(end,lastEnd)
        # if the start not in the previous range
        else:
            # end the list of that start
            ans_list.append([start,end])
    return ans_list

print(merge([[1,3],[2,9],[7,10],[15,18]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,4],[2,3]]))
print(merge([[1,3],[8,10],[15,18],[2,6]]))
print(merge([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]))
# expected result [[1,6]]



