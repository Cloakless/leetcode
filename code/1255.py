class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = {}
        for letter in letters:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1

        def score_words(words, scores):
            tot = 0
            for word in words:
                for letter in word:
                    tot += scores[ord(letter) - 97]
            return tot
        def is_possible(words):
            counter = letter_count.copy()
            longword = "".join(words)
            for letter in longword:
                if letter not in counter:
                    return False
                elif counter[letter] == 0:
                    return False
                else:
                    counter[letter] -= 1
            return True
        def subsets(nums: List[int]) -> List[List[int]]:
            tot = sets = []
            n = len(nums)
            for i in range(2**n):
                subset = []
                curr = 0
                bin_strin =  str(bin(i)[2:])[::-1]
                digs = len(bin_strin)
                while digs < n:
                    bin_strin += '0'
                    digs += 1

                for index, digit in enumerate(bin_strin):
                    if digit == '1':
                        subset.append(nums[index])
                sets.append(subset)
            return sets
        cands = subsets(words)
        best = 0
        for cand in cands:
            if is_possible(cand):
                tot = score_words(cand, score)
                best = max(best,tot)
        return best 

        
        
