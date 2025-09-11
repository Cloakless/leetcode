class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U'}
        extracted = []
        for c in s:
            if c in vowels:
                extracted.append(c)
        extracted.sort()
        ans = []
        i = 0
        for c in s:
            if c not in vowels:
                ans.append(c)
            else:
                v = extracted[i]
                i += 1
                ans.append(v)
        return "".join(ans)
