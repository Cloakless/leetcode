class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def counter(string):
            chars = defaultdict(int)
            for c in string:
                chars[c] += 1
            return chars

        temp1 = []
        temp2 = []
        for word in words2:
            cand = "".join(sorted(word))
            temp2.append(cand)
        words2 = list(set(temp2))

        ans = []
        wordsets = [counter(word) for word in words2]
        for word in words1:
            is_univ = True
            cand = counter(word)
            for wordset in wordsets:
                for c in wordset:
                    if wordset[c] > cand[c]:
                        is_univ = False
            if is_univ:
                ans.append(word)
        return ans
        
