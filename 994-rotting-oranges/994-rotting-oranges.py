class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        assumes allowed to manipulate original data
        '''
        time = 0
        freshOranges = 0
        rows = len(grid)
        columns = len(grid[0])
        
        queue = deque([])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    freshOranges +=1
        
        while queue and freshOranges > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                row = node[0]
                column = node[1]
                for r, c in [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]:
                    if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append([r, c])
                    freshOranges -= 1
            time += 1
            
        if freshOranges:
            return -1
        return time
                
        
                
        