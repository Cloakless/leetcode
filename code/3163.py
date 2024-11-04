class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        streak = 0
        buffer = '!'
        for char in word:
            # Save off
            if char != buffer or streak == 9:
                if streak > 0:
                    ans.append(str(streak) + buffer)
                buffer = char
                streak = 1
            # Keep the streak
            else:
                streak += 1
        ans.append(str(streak) + buffer)
        return "".join(ans)
                
        
