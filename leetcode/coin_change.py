# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
#     Input: coins = [1,2,5], amount = 11
#     Output: 3
#     Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#     Input: coins = [2], amount = 3
#     Output: -1
#
# Example 3:
#     Input: coins = [1], amount = 0
#     Output: 0
#
# Example 4:
#     Input: coins = [1], amount = 1
#     Output: 1
#
# Example 5:
#     Input: coins = [1], amount = 2
#     Output: 2
#
# Constraints:
#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        if amount == 0:
            return 0
        queue = [(0,0)]
        visited_sums = set()
        while len(queue) > 0:
            coin_sum, coin_count = queue.pop(0)
            if coin_sum == amount:
                return coin_count
            for c in coins:
                new_sum = coin_sum + c
                if new_sum <= amount and new_sum not in visited_sums:
                    queue.append((new_sum, coin_count + 1))
                    visited_sums.add(new_sum)
        return -1
