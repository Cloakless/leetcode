class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        obtainable = 0
        ans = 0
        for coin in coins:
            while obtainable < coin - 1:
                # Add a single coin of the next value we need to reach
                ans += 1
                obtainable += obtainable + 1
            obtainable += coin
        while obtainable < target:
            ans += 1
            obtainable += obtainable + 1
        return ans
    
