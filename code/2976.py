class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        letter_costs = [[1000000000 for _ in range(26)] for _ in range(26)]
        for a in range(n):
            # Convert into char index
            x = ord(original[a]) - 97
            y = ord(changed[a]) - 97
            c = cost[a]
            letter_costs[x][y] = min(letter_costs[x][y], c)

        for letter in range(26):
            letter_costs[letter][letter] = 0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    letter_costs[i][j] = min(letter_costs[i][j], letter_costs[i][k] + letter_costs[k][j])
        tot = 0
        for i, letter in enumerate(source):
            conv = letter_costs[ord(letter)-97][ord(target[i])-97]
            if conv == 1000000000:
                return -1
            else:
                tot += conv
        return tot
