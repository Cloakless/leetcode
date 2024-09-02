class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num_players = n
        position = 0
        players = [i for i in range(n)]
        while num_players > 1:
            position = (position + k - 1) % num_players
            loser = players.pop(position)
            num_players -= 1
        return players[0] + 1
