# the idea is to keep track the max product and the min product up to the num that we iterating
# the reason why we need to keep track the min product because if the number in the list are all positive
# we will just need to keep multiplying them
# but when there is a negative number in the list => we will have lots of problem
# the corner cases is that sometime the max product can be the number that we are iterating
def maxProduct(nums):
    # result will be the maximum number in the list
    result = max(nums)
    currMax, currMin = 1, 1
    for n in nums:
        # corner case when the number is 0 => we gonna reset our curr Max and curr Min to 1
        if n == 0:
            currMax, currMin = 1, 1
            continue
        # store the current max product because we are about to change it
        tmp = currMax * n
        currMax = max(n * currMax, n * currMin, n)
        currMin = min(tmp, n * currMin, n)
        result = max(result, currMax)
    return result

print(maxProduct([-2, 0, -1]))

