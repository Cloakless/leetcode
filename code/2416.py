class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        counter = defaultdict(int)
        for word in words:
            for i in range(1, len(word)+1):
                counter[word[:i]] += 1
        ans = []
        for word in words:
            tot = 0
            for i in range(1, len(word)+1):
                tot += counter[word[:i]]
            ans.append(tot)
        return ans
