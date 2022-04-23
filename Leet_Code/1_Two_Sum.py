def twoSum(nums, target):
    ans_list = {}
    answer = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in ans_list:
            answer.append(ans_list[diff])
            answer.append(i)
            return answer
        ans_list[nums[i]] = i

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))