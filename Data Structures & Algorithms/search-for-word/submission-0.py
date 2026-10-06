from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board or not board[0] or not word:
            return False
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True                            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            board[r][c] = '#'                          
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1)
                 or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            board[r][c] = word[i]                      
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


        