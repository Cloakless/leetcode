class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        top, bot, acc = 0, 0, 0
        for diff in differences:
            acc += diff
            top = max(top, acc)
            bot = min(acc, bot)
        return max(0, upper - lower + 1 + bot - top)
