class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        best = letters[0]
        for c in letters:
            if c > target:
                return c
        return best
