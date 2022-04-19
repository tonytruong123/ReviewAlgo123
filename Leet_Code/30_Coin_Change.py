# we will use DP bottom up
# instead of solving directly the amount
# we will solve it from the bottom number which is 1
def coin_change(coins, amount):
    # dynamic programming problem
    # say we check the first count => the sum of amount of coin is equal to that amount of coin +
    # dp[coin - first count]
    # list to keep track of no of coin used for i'th amount
    # keeping the values max to get the min coins neccessary

    dp = [amount + 1] * (amount + 1) #amount + 1 because we going from 0 to the amount
    # default value is amount + 1 ( max value)

    # base case: if we want to compute the amount of coin need for 0 amount => 0
    dp[0] = 0
    # technically still brute force method
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                # we will store the no. of coin used at a'th index
                # 1 is added to keep count of itself too
                # coin = 4
                # amount = 7
                # => dp[7] = 1 + dp[3]
                dp[a] = min(dp[a], 1 + dp[a-coin])
    # only return if the value that we store for the amount is not the defult val
    return dp[amount] if dp[amount] != amount + 1 else -1

# time complexity of O(amount * len(coins))
# space complexity of O(amount)

print(coin_change([1,3,4,5],7))
