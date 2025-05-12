class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        for a in range(n):
            if digits[a] % 2 == 0:
                for b in range(n):
                    for c in range(n):
                        if digits[c] != 0 and a != b and b != c and a != c:
                            ans.add(int(str(digits[c]) + str(digits[b]) + str(digits[a])))
        return sorted(list(ans))
