class Solution:
    def nearestPalindromic(self, n: str) -> str:
        special_cases = {'9': '8', '10': '9', '11': '9'}
        if n in special_cases:
            return special_cases[n]
        if len(n) == 1:
            return str(int(n)-1)
        # 99, 999, etc.
        if len(n) < len(str(int(n)+1)):
            return str(int(n)+2)
        # 100, 1000, etc.
        if len(n) > len(str(int(n)-1)):
            return str(int(n)-1)
        # 101, 1001, etc.
        if len(n) > len(str(int(n)-2)):
            return str(int(n)-2)
        num_digits = len(n)
        is_even = bool((num_digits + 1) % 2)
        cands = []
        stem = int(n[:num_digits//2])
        if is_even:
            # Mirror the stem, or go one above or below
            cands.append(int(str(stem) + str(stem)[::-1]))
            cands.append(int(str(stem + 1) + str(stem + 1)[::-1]))
            cands.append(int(str(stem - 1) + str(stem - 1)[::-1]))
        else:
            middle = n[num_digits//2]
            cands.append(int(str(stem) + middle + str(stem)[::-1]))
            above = int(str(stem) + middle) + 1
            below = int(str(stem) + middle) - 1
            cands.append(int(str(above) + str(above)[:-1][::-1]))
            cands.append(int(str(below) + str(below)[:-1][::-1]))
        diff = 10000000000
        best = diff
        for cand in cands:
            if abs(cand-int(n)) <= diff and int(n) != cand:
                if cand < best or abs(cand-int(n)) < diff:
                    best = cand
                    diff = abs(cand-int(n))
        return str(best)
