class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        letter_heap = []
        for c in counter:
            heappush(letter_heap, (-ord(c), counter[c]))
        ans = ''
        repeating = 0
        while letter_heap:
            cand, count = heappop(letter_heap)
            if repeating < repeatLimit:
                ans += chr(-cand)
                repeating += 1
                if count > 1:
                    heappush(letter_heap, (cand, count-1))
                else:
                    repeating = 0
            else:
                repeating = 0
                if not letter_heap:
                    return ans
                else:
                    new_cand, new_count = heappop(letter_heap)
                    heappush(letter_heap, (cand, count))
                    ans += chr(-new_cand)
                    if new_count > 1:
                        heappush(letter_heap, (new_cand, new_count-1))
                        if cand > new_cand:
                            repeating = 1
        return ans
