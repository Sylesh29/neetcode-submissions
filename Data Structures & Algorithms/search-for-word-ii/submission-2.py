class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word
        
        ROWS, COLS = len(board), len(board[0])
        res = []
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            nxt = node[char]
            if '#' in nxt:
                res.append(nxt.pop('#'))
            
            board[r][c] = '*'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc, nxt)
            board[r][c] = char
        
            if not nxt:
                node.pop(char)
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res