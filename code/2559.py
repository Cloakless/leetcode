class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        num_vowels = 0
        v_count = []
        v_set = {'a','e','i','o','u'}
        for word in words:
            if word[0] in v_set and word[-1] in v_set:
                num_vowels += 1
            v_count.append(num_vowels)
        v_count.append(0) # So v_count[-1] == 0
        ans = []
        for li, ri in queries:
            ans.append(v_count[ri] - v_count[li-1])
        return ans
