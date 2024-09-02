class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        tot = 0
        word_list = list(map((lambda x: 2**(ord(x) - 97)), list(word)))
        mask = 0
        masks = [0] * 1024 # all possible masks
        masks[0] = 1 # if prefix is whole length and 0s that's wonderful
        for i in range(n):
            mask = mask ^ word_list[i]
            tot += masks[mask]
            # Also maybe we differ by 1 from something already seen
            for j in range(10):
                new_mask = mask ^ (1 << j)
                tot += masks[new_mask]
            masks[mask] += 1
        return tot
