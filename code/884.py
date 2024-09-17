class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = defaultdict(int)
        words1 = s1.split()
        words2 = s2.split()
        for word in words1:
            counter[word] += 1
        for word in words2:
            counter[word] += 1
        ans = []
        for word in counter:
            if counter[word] == 1:
                ans.append(word)
        return ans
