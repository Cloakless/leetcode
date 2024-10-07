class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        latest = 0
        j = 0
        
        for bus in buses:
            cap = capacity
            while cap > 0 and j < len(passengers) and passengers[j] <= bus:
                if passengers[j] - 1 not in passenger_set:
                    latest = passengers[j] - 1
                j += 1
                cap -= 1
            if cap > 0 and bus not in passenger_set:
                latest = bus
        
        return latest
