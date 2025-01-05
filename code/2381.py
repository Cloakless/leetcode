class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = []
        for start, end, direction in shifts:
            if direction == 1:
                heappush(changes, (start, 1))
                heappush(changes, (end + 1, -1))
            else:
                heappush(changes, (start, -1))
                heappush(changes, (end + 1, 1))
        tot = 0
        ans = ''


        def shift(letter, idx):
            c = ord(letter) - 97
            c += idx
            c %= 26
            return chr(c + 97)

        for idx, c in enumerate(s):
            while changes and changes[0][0] <= idx:
                _, move = heappop(changes)
                tot += move
            ans += shift(c, tot)
        return ans
