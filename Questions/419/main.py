
def count_battle_ships(board: list[list[int]]) -> int:

    m, n = len(board), len(board[0])

    ans = 0

    def dfs(i: int, j: int) -> None:
        if board[i][j] == '.':
            return 

        board[i][j] = '.'

        for dx, dy in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= dx < m and 0 <= dy < n and dfs(dx, dy) == 'X':
                dfs(dx, dy)


    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                dfs(i, j)
                ans += 1

    return ans
                






print(count_battle_ships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))