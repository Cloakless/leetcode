class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num = 0
        for i in range(1,n+1):
            if n % i == 0:
                num += 1
                if num == k:
                    return i
        return -1
