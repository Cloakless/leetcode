class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = defaultdict(int)
        ans = 0
        for domino in dominoes:
            a, b = min(domino[0], domino[1]), max(domino[0], domino[1])
            ans += seen[(a, b)]
            seen[(a, b)] += 1
        return ans
