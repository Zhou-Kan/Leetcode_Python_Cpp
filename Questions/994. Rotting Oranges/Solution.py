# using BFS 
from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    fresh = 0
    q = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    if fresh == 0: return 0
    
    ret = 0
    while q and fresh > 0:

        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                    q.append((dx, dy))
                    grid[dx][dy] = 2
                    fresh -= 1

        ret += 1

    return ret if fresh == 0 else -1



