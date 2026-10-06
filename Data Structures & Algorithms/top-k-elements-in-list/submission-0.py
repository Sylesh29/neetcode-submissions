import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        c = Counter(nums)
        for key,val in c.items():
            heapq.heappush(h,(val,key))
            if len(h) > k:
                heapq.heappop(h)
        return [val for key,val in h]

        