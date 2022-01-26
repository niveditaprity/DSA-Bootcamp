class TimeMap:

    def __init__(self):
        self.timeMap = {}
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[(timestamp,key)] = value
        self.keys[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if (timestamp,key) in self.timeMap:
            return self.timeMap[(timestamp,key)] 
        if not key in self.keys:
            return ""
        i = bisect.bisect(self.keys[key], timestamp)
        return self.timeMap[(self.keys[key][i-1],key)] if i else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)