class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(z-x), abs(z-y)
        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return 2
