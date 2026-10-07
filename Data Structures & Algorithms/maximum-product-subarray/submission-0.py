class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for n in nums[1:]:
            candidates = (n, cur_max * n, cur_min * n)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best
        
    