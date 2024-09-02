class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        tot = 0
        for i in range(n):
            tot += abs(seats[i] - students[i])
        return tot
