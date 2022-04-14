# say we have s = "aabccbb", k = 2
# we gonna do a sliding window
from collections import Counter

def characterReplacement(s,k):
    count = {}
    res = 0
    l = 0
    for r in range(len(s)):
        # we gonna keep track the appearance of the character up to s[r]
        count[s[r]] = 1 + count.get(s[r], 0)
        # if the amount of characters that can be replaced > k
        # because there is no point of keeping checking that substring when it exceed k amount of characters that can be replaced
        if (r - l + 1) - max(count.values()) > k:
            # because we increment the left so we need to subtract 1 from the hash map
            count[s[l]] -= 1
            # increment the left by 1
            l += 1
        res = max(res, r - l + 1)
    return res

print(characterReplacement("aabccbb",2))