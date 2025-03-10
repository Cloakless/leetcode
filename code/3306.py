class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def isVowel(c):
            return c in ['a','e','i','o','u']

        def countSubsK(word, k):
            ans = 0
            l, r = 0, 0
            n = len(word)
            vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            consonants = 0
            while r < n:
                new_c = word[r]
                if isVowel(new_c):
                    vowels[new_c] += 1
                else:
                    consonants += 1
                while min(vowels.values()) > 0 and consonants >= k:
                    ans += n - r
                    old_c = word[l]
                    if isVowel(old_c):
                        vowels[old_c] -= 1
                    else:
                        consonants -= 1
                    l += 1
                r += 1
            return ans
        return countSubsK(word, k) - countSubsK(word, k+1)
      
