class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        if k == n:
            return True
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        odd_counter = 0
        for c in counter:
            if counter[c] % 2 != 0:
                odd_counter += 1
        if odd_counter > k:
            return False
        return True
