from collections import Counter
from typing import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        res = 0
        l = 0
        maxf = 0

        for r, ch in enumerate(s):
            count[ch] += 1
            maxf = max(maxf, count[ch])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res