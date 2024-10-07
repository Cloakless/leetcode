class UndergroundSystem:

    def __init__(self):
        self.current_entries = {}
        self.journies = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current_entries[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        entry, time = self.current_entries[id]
        if (entry, stationName) not in self.journies:
            self.journies[(entry, stationName)] = [1, t-time]
        else:
            m, n = self.journies[(entry, stationName)]
            self.journies[(entry, stationName)] = [m+1, n + t-time]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        [n, m] = self.journies[(startStation, endStation)]
        return m/n

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
