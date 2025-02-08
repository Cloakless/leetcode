class NumberContainers:

    def __init__(self):
        self.idxs = defaultdict(list)
        self.idx = {}
        

    def change(self, index: int, number: int) -> None:
        self.idx[index] = number
        heappush(self.idxs[number], index)
        

    def find(self, number: int) -> int:
        success = False
        while not success:
            if number not in self.idxs or self.idxs[number] == []:
                return -1
            cand = heappop(self.idxs[number])
            if self.idx[cand] == number:
                heappush(self.idxs[number], cand)
                success = True
        return cand
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
