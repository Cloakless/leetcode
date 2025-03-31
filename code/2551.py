class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        num_marbles = len(weights)
        pairs = []
        for i in range(num_marbles-1):
            pairs.append(weights[i]+weights[i+1])
        pairs.sort()
        min_cost = sum(pairs[:k-1])
        max_cost = sum(pairs[num_marbles-k:])
        return max_cost - min_cost
