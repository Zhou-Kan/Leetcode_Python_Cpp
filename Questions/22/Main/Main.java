import java.util.*;

public class Main {
    private List<String> ans;

    private void backTrack(int left, int right, int n, StringBuffer path) {
        if (left == n && right == n) {
            ans.add(path.toString());
        }
        if (left < n) {
            path.append('(');
        }

        if (left < right) {
            path.append(')');
        }

    }

    public List<String> generateParenthesis(int n) {
        backTrack(n, n, n, new StringBuffer());
        return ans;
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.generateParenthesis(3));
    }
}
