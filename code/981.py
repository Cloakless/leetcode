class TimeMap:
    import bisect

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or self.data[key][0][0] > timestamp:
            return ""
        if timestamp >= self.data[key][-1][0]:
            return self.data[key][-1][1]
        pos = bisect.bisect_right(self.data[key], (timestamp, ''))
        if self.data[key][pos][0] == timestamp:
            return self.data[key][pos][1]
        return self.data[key][pos-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
