class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        leftover = 0
        n = len(fruits)
        taken = [False] * n
        for fruit in fruits:
            for i in range(n):
                if baskets[i] >= fruit and taken[i] != True:
                    taken[i] = True
                    break
        return n - sum([int(b) for b in taken])
