class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        # Odd left, even right
        ans += ((n + 1) // 2) * (m // 2)
        # Even left, odd 
        ans += ((m + 1) // 2) * (n // 2)
        return ans
