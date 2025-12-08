class Solution:
    def countTriples(self, n: int) -> int:
        squares = set([i**2 for i in range(n+1)])
        ans = 0
        for i in range(1,n+1):
            for j in range(1, n+1):
                if i**2 + j**2 in squares:
                    ans += 1
        return ans
