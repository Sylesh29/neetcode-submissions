# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        q = deque([root])
        
        while q:
            level = []
            for i in range(len(q)):
                v = q.popleft()
                if v:
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
            if level:
                res.append(level)
        return res
        

        