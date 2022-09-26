class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiagnol = set()
        negDiagnol = set()
        board = [["."]*n for i in range(n)]
        res = []
        
        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row)) 
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiagnol or (r-c) in negDiagnol:
                    continue
                col.add(c)
                posDiagnol.add(r+c)
                negDiagnol.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                
                col.remove(c)
                posDiagnol.remove(r+c)
                negDiagnol.remove(r-c)
                board[r][c] = "."
                
        backtrack(0)         
        return res
                
        