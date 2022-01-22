class RecentCounter:

    def __init__(self):
        self.recentRequests=[]
        

    def ping(self, t: int) -> int:
        self.recentRequests.append(t)
        self.recentRequests.reverse()
        while self.recentRequests[-1]<t-3000:
            self.recentRequests.pop()
        self.recentRequests.reverse()
        return len(self.recentRequests)
