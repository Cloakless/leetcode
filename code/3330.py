class Solution:
    def possibleStringCount(self, word: str) -> int:
        streaks = []
        last = '!'
        streak = 0
        for c in word:
            if c == last:
                streak += 1
            else:
                streaks.append(streak)
                streak = 0
                last = c
        streaks.append(streak)
        ans = 1
        for streak in streaks:
            ans += streak
        return ans
