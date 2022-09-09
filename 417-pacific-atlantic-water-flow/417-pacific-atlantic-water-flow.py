class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        columns = len(heights[0])
        reachedAtl = set()
        reachedPac = set()
        
        def dfs(r, c, reachedOcean, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= columns or prevHeight > heights[r][c] or (r, c) in reachedOcean:
                return
            reachedOcean.add((r, c))
            dfs(r+1, c, reachedOcean, heights[r][c])
            dfs(r-1, c, reachedOcean, heights[r][c])
            dfs(r, c+1, reachedOcean, heights[r][c])
            dfs(r, c-1, reachedOcean, heights[r][c])
            
        for r in range(rows):
            dfs(r, 0, reachedPac, heights[r][0])
            dfs(r, columns-1, reachedAtl, heights[r][columns-1])
            
        for c in range(columns):
            dfs(0, c, reachedPac, heights[0][c])
            dfs(rows-1, c, reachedAtl, heights[rows-1][c])
        
        for node in reachedAtl:
            if node in reachedPac:
                res.append(list(node))
        return res