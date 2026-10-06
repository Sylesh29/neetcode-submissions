import heapq
class MedianFinder:

    def __init__(self):
        self.s , self.l = [],[]

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.s,-1 * num)
        if (self.s and self.l and (-1 * self.s[0]) > self.l[0]):
            v = heapq.heappop(self.s) * -1
            heapq.heappush(self.l,v)
        if len(self.s) > len(self.l) + 1:
            v = heapq.heappop(self.s) * -1
            heapq.heappush(self.l, v)
        if len(self.l) > len(self.s) + 1:
            v = heapq.heappop(self.l)
            heapq.heappush(self.s, v * -1)

        

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return self.s[0] * -1
        if len(self.l) > len(self.s):
            return self.l[0]
        return (-1 * self.s[0] + self.l[0])/2.0

        
        