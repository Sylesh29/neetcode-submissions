from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            s_o = ''.join(sorted(s))
            res[s_o].append(s)
        return list(res.values())
        