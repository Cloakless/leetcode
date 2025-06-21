class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = defaultdict(int)
        n = len(word)
        for c in word:
            counter[c] += 1
        best = n
        for c in counter:
            # Assume this is the smallest
            dels = 0
            for letter in counter:
                if counter[letter] < counter[c]:
                    dels += counter[letter]
                else:
                    dels += max(0, counter[letter] - counter[c] - k)
            best = min(best, dels)
        return best
