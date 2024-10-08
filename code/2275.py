class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = [0] * 25
        for cand in candidates:
            for i in range(25):
                if 2**i & cand != 0:
                    counter[i] += 1
        return max(counter)
