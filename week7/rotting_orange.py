from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh_num = 0
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if curr == 1:
                    fresh_num += 1
                elif curr == 2:
                    q.append((i, j))

        while True:
            new_q = deque()
            while len(q) > 0:
                i, j = q.popleft()
                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:
                        fresh_num -= 1
                        grid[i - 1][j] = 2
                        new_q.append((i - 1, j))
                if i + 1 < m:
                    if grid[i + 1][j] == 1:
                        fresh_num -= 1
                        grid[i + 1][j] = 2
                        new_q.append((i + 1, j))
                if j - 1 >= 0:
                    if grid[i][j - 1] == 1:
                        fresh_num -= 1
                        grid[i][j - 1] = 2
                        new_q.append((i, j - 1))
                if j + 1 < n:
                    if grid[i][j + 1] == 1:
                        fresh_num -= 1
                        grid[i][j + 1] = 2
                        new_q.append((i, j + 1))
            if len(new_q) == 0:
                break
            q = new_q
            res += 1
        if fresh_num > 0:
            return -1
        return res