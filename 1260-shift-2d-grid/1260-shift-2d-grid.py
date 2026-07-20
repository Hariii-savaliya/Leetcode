class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not k:
            return grid
        row = len(grid)
        colum = len(grid[0])
        n = row * colum
        k %= n
        i = 0
        j = len(grid)

        def shift(i, j):
            while i < j:
                grid[i // colum][i % colum], grid[j // colum][j % colum] = grid[j // colum][j % colum], grid[i // colum][i % colum]
                i += 1
                j -= 1

        shift(0, n - 1)
        shift(0, k - 1)
        shift(k, n - 1)
        
        return grid
        