# we have a list [-2,2,5,-11,6]
# we gonna check what is the maximum sum up to 2, up to 5, up to -11, ....
# and then we gonna decide whether we gonna add the current val to the previous sum or start the new sum with that current val

def Kadane(nums):
    max_sum, curr_sum = nums[0],nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(Kadane([-2,2,5,-11,6]))