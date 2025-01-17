class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for d in derived:
            ans ^= d
        return ans == 0
