class RandomizedSet:
    from collections import defaultdict
    from random import randint

    def __init__(self):
        self.values = defaultdict(int)
        self.val_list = []

    def insert(self, val: int) -> bool:
        # print(self.values)
        if val in self.values:
            return False
        self.val_list.append(val)
        self.values[val] = len(self.val_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        i = self.values[val]
        self.val_list[i], self.val_list[-1] = self.val_list[-1], self.val_list[i]
        self.values[self.val_list[i]] = i
        del self.values[self.val_list.pop()]
        return True
        

    def getRandom(self) -> int:
        return self.val_list[randint(0, len(self.val_list)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
