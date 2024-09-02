class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        last_seen = {}

        def reachable(t, k):
            letters = set()
            for num in range(max(97, ord(t) - k), min(123, ord(t) + 1 + k)):
                letters.add(chr(num))
            return letters

        best = [1 for x in range(len(s))]
        for i in range(len(s)):
            # Find longest ideal subsequence ending here
            candidates = reachable(s[i], k)
            best_len = 1
            for letter in candidates:
                if letter in last_seen:
                    best_len = max(best_len, best[last_seen[letter]] + 1)
            last_seen[s[i]] = i
            best[i] = best_len
        return max(best)
