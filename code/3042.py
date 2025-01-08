class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix(a,b):
            if len(a) > len(b):
                return False
            return all([a[idx] == b[idx] for idx in range(len(a))])

        def is_suffix(a,b):
            return is_prefix(a[::-1], b[::-1])

        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_prefix(words[i], words[j]) and is_suffix(words[i], words[j]):
                    ans += 1
        return ans
