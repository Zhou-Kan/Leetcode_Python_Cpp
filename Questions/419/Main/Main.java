public class Main {
    int[][] dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    public void dfs(int i, int j, char[][] board) {
        if (board[i][j] == '.') return;
        board[i][j] = '.';

        for (int[] d : dir) {
            int dx = d[0] + i;
            int dy = d[1] + j;
            if (dx >= 0 && dx < board.length && dy >= 0 && dy < board[0].length && board[dx][dy] == 'X') {
                dfs(dx, dy, board);
            }
        }
    }

    public int countBattleShips(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        int ans = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'X') {
                    dfs(i, j, board);
                    ans++;
                }
            }
        }
        
        return ans;
    }
    public static void main(String[] args) {
        char[][] board = {
            {'X','.','.','X'}, 
            {'.','.','.','X'}, 
            {'.','.','.','X'}
        };
        Main main = new Main();
        int ans = main.countBattleShips(board);
        System.out.println(ans);
    }
}
