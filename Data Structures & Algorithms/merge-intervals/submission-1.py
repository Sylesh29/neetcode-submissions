class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i,j in intervals[1:]:
            last=res[-1][1]
            if i<=last:
                res[-1][1]=max(last,j)
            else:
                res.append([i,j])
        return res