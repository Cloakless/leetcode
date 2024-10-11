class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        empties, events = [i for i in range(len(times))], []
        heapq.heapify(empties)
        for i in range(len(times)):
            start, end = times[i]
            events.append((start, i + 1))
            events.append((end, -1*(i+1)))
        events.sort()
        seats = {}
        for time, person in events:
            if person > 0:
                seat = heappop(empties)
                if person == targetFriend + 1:
                    return seat
                seats[person] = seat
            else:
                seat = seats[-1*person]
                heappush(empties, seat)
