# in order for a string to be palindrome, there can only be maximum 1 character in that string that has an odd amount of appearance
# for k amount of palindrome to exist, there must be k or less than k odd characters exist in the given string
def canConstruct(s, k) :
    if k > len(s):
        return False
    counter = {}
    count = 0
    for i in range(len(s)):
        counter[s[i]] = 1 + counter.get(s[i],0)
    for i in counter:
        if counter[i] % 2 != 0:
            count += 1
    if count > k:
        return False
    return True

print(canConstruct("annabelle",2))
print(canConstruct("leetcode",3))
print(canConstruct("true",4))