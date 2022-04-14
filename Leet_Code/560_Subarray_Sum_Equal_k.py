def subarraySum(nums, k):
    # when we are at the prefix sum of the current number => the question is that can we get rid of the previous prefix sum
    # => to turn the current prefix sum into k
    # to find that prefix sum that we need to get rid of, we will take the current prefix sum - the k
    # the question is, does that prefix exist up to that number that we are iterating through?
    # to keep track of the previous sum => we need a hash map
    # we will make a hash map to keep track of the prefix sum at the current number that we are iterating
    # if that prefix sum that we need to subtract already exists (already in the hash) => the amount of subarray with k sum will be equal to the time that the subtracted prefix sum appear
    # if it is not, that mean there is no subarray up to that number
    # the corner case is that if the k sum subarray appear first, means that the difference will be = 0
    # we just need to add 0: 1 to the hash map first
    hash_map = {0: 1}
    curr_sum, appear, result = 0, 0, 0
    # looping through
    for i in range(len(nums)):
        # the prefix sum at current i in nums
        curr_sum += nums[i]
        # diff will be the prefix sum that we need to subtract from the current prefix to turn the current prefix sum in to k
        diff = curr_sum - k
        # if the prefix that we are looking in the map => that means there exists subarray with k sum up to the current i
        if diff in hash_map:
            # the amount of k sum subarray will be equal to the amount of subtracted prefix sum appear up to the current prefix
            result += hash_map[diff]
        # if the current prefix is not in hash_map =>
        if curr_sum not in hash_map:
            hash_map[curr_sum] = appear
        if curr_sum in hash_map:
            hash_map[curr_sum] += 1
    return result

print(subarraySum([1, 1, 1], 2))
print(subarraySum([1,2,3],3))
print(subarraySum([1, 1, 1, 1, 1, 1],3))