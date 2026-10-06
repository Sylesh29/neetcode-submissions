class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_set = set(nums)
        for i in range(n+1):
            if i not in n_set:
                return i

        