class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        counter = [defaultdict(int) for _ in range(len(words[0]))]
        for word in words:
            for idx, c in enumerate(word):
                counter[idx][c] += 1
        n = len(target)
        m = len(words[0])

        @cache
        def dp(i, j):
            # How many ways can you form target[i:] starting at the jth element of words
            if i > n-1 or j > m-1 or n-i > m-j:
                return 0
            if i == n-1 and j == m-1:
                return counter[j][target[i]]
            if counter[j][target[i]] > 0:
                if i == n - 1:
                    taken = counter[j][target[i]]
                else:
                    taken = counter[j][target[i]] * dp(i+1, j+1)
            else:
                taken = 0
            not_taken = dp(i, j+1)
            return (taken + not_taken) % 1000000007

        return dp(0,0)
        
