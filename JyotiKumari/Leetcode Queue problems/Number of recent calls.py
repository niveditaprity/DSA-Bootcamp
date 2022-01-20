class RecentCounter:

    def __init__(self):
        self.recent = []
        self.front = 0

    def ping(self, t: int) -> int:
        self.recent.append(t)
        if(self.recent[self.front]>=t-3000):
            return len(self.recent)
        while(self.recent[self.front]<t-3000):
            self.recent.pop(0)
        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)