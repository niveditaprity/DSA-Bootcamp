class RandomizedSet:

    def __init__(self):
        self.indexes = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        else: 
            self.values.append(val)
            self.indexes[val] = len(self.values)-1
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.indexes:
           last = len(self.values)-1
           idx, last = self.indexes[val], self.values[-1]
           self.values[idx], self.indexes[last] = last, idx
           del self.indexes[val]
           self.values.pop()
           return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()